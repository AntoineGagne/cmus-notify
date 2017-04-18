"""Contains the main code of the package."""

from argparse import RawDescriptionHelpFormatter, ArgumentParser

from .constants import (DEFAULT_APPLICATION_NAME,
                        DEFAULT_MESSAGE_BODY,
                        DEFAULT_MESSAGE_TITLE,
                        ICONS_BY_STATUS)
from .formatters import format_notification_message
from .notifications import Notifier
from .options import parse_arguments
from .parsers import parse_status_information


def main():
    """Main entry point of the package."""
    arguments = parse_arguments()
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
