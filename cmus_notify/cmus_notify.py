#! /usr/bin/env python3

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

"""Contains code to display current status of Cmus."""

import sys
from collections import defaultdict
from functools import reduce

import notify2


#: Default text for the display values
DEFAULT_STATUS_DISPLAY = 'N/A'
#: The various field contained in the metadata
FIELDS = (
    'status',
    'file',
    'artist',
    'album',
    'discnumber',
    'tracknumber',
    'title',
    'date',
    'duration'
)
#: The icons by the media player status
ICONS_BY_STATUS = {
    'paused': 'stock_media-pause',
    'playing': 'stock_media-play',
    'stopped': 'stock_media-stop'
}
#: The icon's path to be used by default
DEFAULT_ICON_PATH = ''
#: The default timeout for the notification to disappear
DEFAULT_TIMEOUT = 5000
#: The default name of the application
DEFAULT_APPLICATION_NAME = 'Cmus'


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
        notification = notify2.Notification(title, text, kwargs.get('icon_path', DEFAULT_ICON_PATH))
        notification.set_urgency(kwargs.get('urgency', notify2.URGENCY_LOW))
        notification.timeout = kwargs.get('timeout', DEFAULT_TIMEOUT)
        notification.show()


def _format_notification_message(status_information):
    """Format the :class:`StatusInformation` to be send.

    :param status_information: The information to be sent
    :type status_information: :class:`StatusInformation`
    """
    title = 'Current Status: {0}'.format(
        status_information.status.capitalize(),
    )
    text = ('<b>Title:</b> {0}\n'
            '<b>Artist:</b> {1}\n'
            '<b>Album:</b> {2}\n'
            '<b>Date:</b> {3}\n'
            '<b>Track:</b> {4}\n'
            '<b>Disc:</b> {5}\n'
            '<b>Duration:</b> {6}').format(
                status_information.title,
                status_information.artist,
                status_information.album,
                status_information.date,
                status_information.tracknumber,
                status_information.discnumber,
                status_information.duration,
            )
    return title, text


class StatusInformation:
    """The status information of Cmus"""

    def __init__(self, **kwargs) -> None:
        """Initialize a :class:`StatusInformation` object.

        :param kwargs: See below.

        :Keyword Arguments:
            * *album* (``str``) --- The name of the song's album
            * *artist* (``str``) --- The name of the song's artist(s)
            * *date* (``str``) --- The date at which the song was composed
            * *discnumber* (``int``) --- The disc's number
            * *duration* (``int``) --- The duration of the song
            * *file* (``str``) --- The place from which the song is read
            * *status* (``str``) --- Cmus current status
            * *title* (``str``) --- The song's title
            * *tracknumber* (``int``) --- The song's number
        """
        self.album = kwargs.get('album', DEFAULT_STATUS_DISPLAY)
        self.artist = kwargs.get('artist', DEFAULT_STATUS_DISPLAY)
        self.date = kwargs.get('date', DEFAULT_STATUS_DISPLAY)
        self.discnumber = kwargs.get('discnumber', DEFAULT_STATUS_DISPLAY)
        self.duration = kwargs.get('duration', DEFAULT_STATUS_DISPLAY)
        self.file = kwargs.get('file', DEFAULT_STATUS_DISPLAY)
        self.status = kwargs.get('status', DEFAULT_STATUS_DISPLAY)
        self.title = kwargs.get('title', DEFAULT_STATUS_DISPLAY)
        self.tracknumber = kwargs.get('tracknumber', DEFAULT_STATUS_DISPLAY)


def _parse_status_information(informations):
    """Parse the status informations from the informations list.

    :param informations: The list containing the various song's information
    :type informations: list<str>
    :returns: :class:`collections.defaultdict`
    """
    fields = set(FIELDS)
    status_information = defaultdict(list)
    current_status = None
    for word in informations:
        if word in FIELDS:
            current_status = word
            fields.remove(word)
        if current_status and word not in FIELDS:
            status_information[current_status].append(word)

    return status_information


def _format_status_information_fields(status_information, *formatters):
    """Format the status informations dictionary.

    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :param formatters: The formatters functions
    :type formatters: tuple<callable>
    :returns: A status information object containing the various information
    :rtype: :class:`StatusInformation`
    """
    return StatusInformation(
        **reduce(
            lambda information, formatter: formatter(information),
            formatters,
            status_information
        )
    )


def _format_artist_field(status_information):
    """Format the *artist* field.

    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :returns: The updated status informations
    :rtype: :class:`collections.defaultdict`
    """
    status_information['artist'] = ' '.join(status_information['artist'])
    return status_information


def _format_duration_field(status_information):
    """Format the *duration* field.

    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :returns: The updated status informations
    :rtype: :class:`collections.defaultdict`
    """
    try:
        duration = int(''.join(status_information['duration']))
        status_information['duration'] = '{0:02d}:{1:02d}'.format(
            duration // 60,
            duration % 60
        )
    except ValueError:
        status_information.pop('duration', None)

    return status_information


def _format_left_fields(status_information):
    """Format the unformatted fields.

    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :returns: The updated status informations
    :rtype: :class:`collections.defaultdict`
    """
    for key, value in status_information.copy().items():
        if isinstance(value, list):
            status_information[key] = ' '.join(value)
    return status_information


if __name__ == '__main__':
    INFORMATION_BY_FIELD_NAME = _parse_status_information(sys.argv[1].split())
    STATUS_INFORMATION = _format_status_information_fields(
        INFORMATION_BY_FIELD_NAME,
        _format_artist_field,
        _format_duration_field,
        _format_left_fields
    )
    TITLE, TEXT = _format_notification_message(STATUS_INFORMATION)
    NOTIFIER = Notifier(DEFAULT_APPLICATION_NAME)
    NOTIFIER.send_notification(TITLE, TEXT, icon_path=ICONS_BY_STATUS.get(STATUS_INFORMATION.status, ''))
