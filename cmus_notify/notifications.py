"""Contains code related to notifications."""

import asyncio

from .constants import DEFAULT_ICON_PATH, DEFAULT_TIMEOUT, ICONS_BY_STATUS
from .formatters import format_notification_message


def send_notification(arguments, information):
    """Send the notification to the OS with a Python library.

    :param arguments: The parsed arguments
    :param information: The various song informations
    """
    from desktop_notify.aio import Notify

    title, text = format_notification_message(
        information, title=arguments["title"], body=arguments["body"]
    )
    notification = Notify(title, text)
    notification.set_icon(
        ICONS_BY_STATUS.get(information.status.lower(), DEFAULT_ICON_PATH)
    ).set_timeout(arguments.get("timeout", DEFAULT_TIMEOUT))
    asyncio.run(notification.show())
