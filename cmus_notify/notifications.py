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

"""Contains code related to notifications."""

import notify2

from .constants import DEFAULT_ICON_PATH, DEFAULT_TIMEOUT


class Notifier:
    """A notification to the Gnome notification system."""

    def __init__(self, application_name):
        """Initialize a :class:`Notification` object.

        :param application_name: The application's name
        :type application_name: str
        """
        self.application_name = application_name

    def send_notification(self, title, text, **kwargs):
        """Send the notification to the OS with a Python library.

        :param title: The message's title
        :type title: str
        :param text: The message's body
        :type text: str
        :raises ImportError: If the library :module:`notify` is not installed
        """
        notify2.init(self.application_name)
        notification = notify2.Notification(
            title,
            text,
            kwargs.get('icon_path', DEFAULT_ICON_PATH)
        )
        notification.set_urgency(kwargs.get('urgency', notify2.URGENCY_LOW))
        notification.timeout = kwargs.get('timeout', DEFAULT_TIMEOUT)
        notification.show()
