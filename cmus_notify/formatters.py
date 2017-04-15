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

"""Contains code to format the current status of Cmus."""

from .constants import DEFAULT_MESSAGE_BODY, DEFAULT_MESSAGE_TITLE


def format_notification_message(status_information, **kwargs):
    """Format the :class:`StatusInformation` to be send.

    :param status_information: The information to be sent
    :type status_information: :class:`StatusInformation`
    """
    title = (kwargs.get('title', DEFAULT_MESSAGE_TITLE)
                   .format(**status_information.__dict__))
    text = (kwargs.get('body', DEFAULT_MESSAGE_BODY)
                  .format(**status_information.__dict__))
    return title, text
