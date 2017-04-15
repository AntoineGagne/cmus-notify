# Copyright © 2017 Antoine Gagné
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Contains the main code of the package."""

from argparse import RawDescriptionHelpFormatter, ArgumentParser

from .constants import (DEFAULT_APPLICATION_NAME,
                        DEFAULT_MESSAGE_BODY,
                        DEFAULT_MESSAGE_TITLE,
                        ICONS_BY_STATUS)
from .formatters import format_notification_message
from .notifications import Notifier
from .parsers import parse_status_information


def main():
    """Main entry point of the package."""
    arguments = _parse_arguments()
    information = parse_status_information(arguments.parse)
    title, text = format_notification_message(information,
                                              title=arguments.title,
                                              body=arguments.body)
    notifier = Notifier(arguments.application_name)
    notifier.send_notification(
        title,
        text,
        icon_path=ICONS_BY_STATUS.get(information.status.lower(), '')
    )


def _parse_arguments():
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
                        default=DEFAULT_APPLICATION_NAME,
                        type=str,
                        help='The name of the application')
    parser.add_argument('-b',
                        '--body',
                        required=False,
                        metavar='BODY_FORMAT_STRING',
                        default=DEFAULT_MESSAGE_BODY,
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
                        default=DEFAULT_MESSAGE_TITLE,
                        type=str,
                        help='A format string that can be specified to tell the'
                             ' software how to format the title. The syntax is '
                             'the same as Python\'s. The available options are '
                             'specified at the end of this help message. (i.e. '
                             '\'Now playing: {title}\')')
    return parser.parse_args()
