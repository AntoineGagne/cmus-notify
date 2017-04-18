"""Contains the code related to configuration file parsing."""

from configparser import ConfigParser

from .constants import CONFIGURATION_SECTIONS, DEFAULT_OPTIONS
from .options import parse_arguments


def parse_configuration_file():
    """Parse the configuration file. If there are any command-line arguments,
       override the configuration values with the one from the command line.

       :returns: The various options
       :rtype: dict
    """
    arguments = parse_arguments()
    configuration_parser = ConfigParser()
    options = {}
    if configuration_parser.read(arguments.configuration_file):
        for section in CONFIGURATION_SECTIONS:
            options.update(dict(configuration_parser.items(section)))
    else:
        options.update(DEFAULT_OPTIONS)

    options.update(vars(arguments))
    return options
