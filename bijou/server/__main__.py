import os
import argparse
import yaml
import warnings
import logging
import coloredlogs
import verboselogs
from pydash import _
from schema import Schema, SchemaError, And, Use, Optional

from . import errors

# Create a logger for this script
logger = logging.getLogger(__name__)

def read_config(config_file: str) -> yaml.YAMLObject:
    """
    Read and parse a bijou configuration file

    Args:
        config_file: Path to a configuration file
    """
    with open(config_file, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)


def init_config(default_file: str = 'bijou.yml', opt_file: str = None) -> dict:
    """
    Initialise the configuration object with sane defaults and then attempt
    to load either the optional file or the default local config file.

    Args:
        default_file: Path to the default configuration file
        opt_file: Path to an optional file to load instead of the default
    """
    # Initialise with the default configuration - this is mutable and altered
    # depending on the config files being read below
    config = {
        'log': {
            'level': 'debug',
            'file': 'bijou.log'
        },
        'db': {
            'url': 'sqlite://'
        },
        'plugins': []
    }

    # If a configuration file is specified load that, however if the config
    # file has been specified but does not exist exit with an error. If no
    # config file is specified then try to load the local one but only
    # fail with a warning if it's not found
    if opt_file:
        if os.path.isfile(opt_file):
            _.merge(config, read_config(opt_file))
        else:
            raise(errors.ConfigFileNotFoundError(opt_file))
    else:
        if os.path.isfile(default_file):
            _.merge(config, read_config(default_file))
        else:
            logger.warning(errors.ConfigFileNotFoundWarning(default_file))

    return config


def validate_config(cfg: dict) -> bool:
    """
    Validate a configuration object against the configuration schema that
    bijou-server expects.

    Args:
        cfg: Potentially valid configuration object
    """
    try:
        schema = Schema({
            Optional('log'): {
                'level': And(str, len),
                Optional('file'): And(str, len),
                Optional('format'): And(str, len)
            },
            'db': {
                'url': And(str, len)
            },
            'plugins': [And(str, len)]
        })
        schema.validate(cfg)
        return True
    except SchemaError as exc:
        logger.error(exc)
        return False


def main():
    """
    Command-line entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='configuration file location')
    parser.add_argument('--log-level', help='logging level')
    args = parser.parse_args()

    # Create and configure a logger - automatically set it for warnings
    # and errors only (which can be thrown by the config process)
    coloredlogs.install(level='WARNING')

    # Initialise the config with the file optionally passed in from
    # command line or try to use the default file
    config = init_config(default_file='bijou.yml', opt_file=args.config)

    # Set the logging to what is in the config file
    coloredlogs.install(level='DEBUG')

    validate_config(config)

    # Debug out for the arguments and configuration
    logger.debug(args)
    logger.debug(config)

# If run as script also execute main function
if __name__ == "__main__":
    main()
