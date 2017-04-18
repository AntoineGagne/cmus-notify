"""Contains the main code of the package."""

from .configurations import parse_configuration_file
from .constants import ICONS_BY_STATUS
from .formatters import format_notification_message
from .notifications import Notifier
from .parsers import parse_status_information


def main():
    """Main entry point of the package."""
    arguments = parse_configuration_file()
    information = parse_status_information(arguments['parse'])
    title, text = format_notification_message(information,
                                              title=arguments['title'],
                                              body=arguments['body'])
    notifier = Notifier(arguments['application_name'])
    notifier.send_notification(
        title,
        text,
        icon_path=ICONS_BY_STATUS.get(information.status.lower(), '')
    )
