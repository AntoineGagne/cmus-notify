"""Contains the main code of the package."""

import importlib
import os
import sys

from .configurations import parse_configuration_file
from .parsers import parse_status_information


def main():
    """Main entry point of the package."""
    arguments = parse_configuration_file()
    information = parse_status_information(arguments['parse'])
    custom_notifier = load_notifier(arguments)
    custom_notifier(arguments, information)


def load_notifier(arguments):
    """Load the custom notification module.

    :param arguments: The parsed arguments
    :returns: The notifier to be used for the notifications
    """
    custom_notifier_path = arguments.get('custom_notification', None)
    if custom_notifier_path:
        sys.path.insert(0, os.path.expanduser(os.path.dirname(custom_notifier_path)))
        notifier_module = importlib.import_module(os.path.basename(custom_notifier_path))
        notifier = notifier_module.send_notification
    else:
        from .notifications import send_notification
        notifier = send_notification

    return notifier
