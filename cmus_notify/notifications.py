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
