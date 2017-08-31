"""Contains code related to notifications."""

from .constants import (DEFAULT_ICON_PATH,
                        DEFAULT_TIMEOUT,
                        ICONS_BY_STATUS)
from .formatters import format_notification_message


def send_notification(arguments, information):
    """Send the notification to the OS with a Python library.

    :param arguments: The parsed arguments
    :param information: The various song informations
    """
    import notify2

    notify2.init(arguments['application_name'])
    title, text = format_notification_message(information,
                                              title=arguments['title'],
                                              body=arguments['body'])
    notification = notify2.Notification(
        title,
        text,
        ICONS_BY_STATUS.get('icon_path', DEFAULT_ICON_PATH)
    )
    notification.set_urgency(arguments.get('urgency', notify2.URGENCY_LOW))
    notification.timeout = arguments.get('timeout', DEFAULT_TIMEOUT)
    notification.show()
