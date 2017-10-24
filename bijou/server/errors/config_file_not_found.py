import errno
import os

class ConfigFileNotFoundError(FileNotFoundError):
    """
    The optionally supplied configuration file was not found
    """
    def __init__(self, file):
        super(errno.ENOENT, os.strerror(errno.ENOENT), file)

class ConfigFileNotFoundWarning(Warning):
    """
    The default configuration file was not found (which is okay)
    """
    def __init__(self, file):
        self.file = file
