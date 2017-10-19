"""bijou-server (bijou)"""

from . import errors
from . import net
from . import plugins

import os
import argparse
import yaml
import warnings
from pydash import _

def main():
    """
    Command-line entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='configuration file location')
    parser.add_argument('--log-level', help='logging level')
    args = parser.parse_args()

    # Initialise the configuration object with sane defaults
    config = {
        'log': {
            'level': 'debug',
            'file': 'log.txt'
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
    if args.config:
        if os.path.isfile(args.config):
            pass
        else:
            raise(errors.ConfigFileNotFoundError(args.config))
    else:
        if os.path.isfile('bijou.yml'):
            pass
        else:
            warnings.warn(errors.ConfigFileNotFoundWarning('bijou.yml'))

    # Merge the configuration from the files (if any) with the configuration
    # from the command line arguments. This process is fairly manualy and
    # could probably be done with a split on underscores but for now it'll do
    for arg in vars(args):
        if arg == 'log_level':
            config['log']['level'] = getattr(args, arg)
        elif arg == 'log_file':
            config['log']['file'] = getattr(args, arg)

    print(args)
    print(config)
