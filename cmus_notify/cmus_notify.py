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

import sys

from .constants import DEFAULT_APPLICATION_NAME, ICONS_BY_STATUS
from .formatters import format_notification_message
from .notifications import Notifier
from .parsers import parse_status_information


def main():
    """Main entry point of the package."""
    information = parse_status_information(sys.argv[1])
    title, text = format_notification_message(information)
    notifier = Notifier(DEFAULT_APPLICATION_NAME)
    notifier.send_notification(
        title,
        text,
        icon_path=ICONS_BY_STATUS.get(information.status, '')
    )
