"""Contains the code related to options parsing."""

from argparse import (RawDescriptionHelpFormatter,
                      ArgumentParser,
                      SUPPRESS)

from .constants import DEFAULT_CONFIGURATION_FILE


def parse_arguments():
    """Create an :class:`argparse.ArgumentParser` and parse the command-line arguments."""

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            prog='cmus_notify',
                            description='Display a notification about Cmus\'s '
                                        'current status',
                            epilog='Format String Parameters\n'
                                   '========================\n\n'
                                   'The available arguments to the format '
                                   'strings are the following:\n\n'
                                   '  - album: The song\'s album\n'
                                   '  - artist: The song\'s artist\n'
                                   '  - date: The song\'s release date\n'
                                   '  - discnumber: The song\'s disc\'s number\n'
                                   '  - duration: The song\'s duration\n'
                                   '  - file: The song\'s file\'s path\n'
                                   '  - status: Cmus current status\n'
                                   '  - title: The song\'s title\n'
                                   '  - tracknumber: The song\'s track number')
    parser.add_argument('parse',
                        type=str,
                        metavar='INFORMATION',
                        help='Parse the given information')
    parser.add_argument('-a',
                        '--application_name',
                        default=SUPPRESS,
                        type=str,
                        help='The name of the application')
    parser.add_argument('-b',
                        '--body',
                        required=False,
                        metavar='BODY_FORMAT_STRING',
                        default=SUPPRESS,
                        type=str,
                        help='A format string that can be specified to tell the'
                             ' software how to format the body. The syntax is '
                             'the same as Python\'s. The available options are '
                             'specified at the end of this help message. (i.e. '
                             '\'Artist: {artist}\')')
    parser.add_argument('-t',
                        '--title',
                        required=False,
                        metavar='TITLE_FORMAT_STRING',
                        default=SUPPRESS,
                        type=str,
                        help='A format string that can be specified to tell the'
                             ' software how to format the title. The syntax is '
                             'the same as Python\'s. The available options are '
                             'specified at the end of this help message. (i.e. '
                             '\'Now playing: {title}\')')
    parser.add_argument('-f',
                        '--configuration_file',
                        required=False,
                        default=DEFAULT_CONFIGURATION_FILE,
                        type=str,
                        help='The path to the configuration file. If it is not '
                             'specified, the program will use the default '
                             'values of the other options.')
    parser.add_argument('-c',
                        '--custom_notification',
                        required=False,
                        default=SUPPRESS,
                        type=str,
                        help='The path to a custom implementation of the '
                             'notification class. If it is not specified, the '
                             'standard implementation will be used (the one using '
                             'notify2).')
    return parser.parse_args()
