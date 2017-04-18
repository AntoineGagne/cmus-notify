"""Contains code to format the current status of Cmus."""

from .constants import DEFAULT_MESSAGE_BODY, DEFAULT_MESSAGE_TITLE


def format_notification_message(status_information, **kwargs):
    """Format the :class:`cmus_notify.types.StatusInformation` to be send.

    :param status_information: The information to be sent
    :type status_information: :class:`cmus_notify.types.StatusInformation`
    """
    title = (kwargs.get('title', DEFAULT_MESSAGE_TITLE)
                   .format(**status_information.__dict__))
    text = (kwargs.get('body', DEFAULT_MESSAGE_BODY)
                  .format(**status_information.__dict__))
    return title, text
