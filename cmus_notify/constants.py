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

"""Contains the constants used by the library."""

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
#: The default message body of the notifications
DEFAULT_MESSAGE_BODY = ('<b>Title:</b> {title}\n'
                        '<b>Artist:</b> {artist}\n'
                        '<b>Album:</b> {album}\n'
                        '<b>Date:</b> {date}\n'
                        '<b>Track:</b> {tracknumber}\n'
                        '<b>Disc:</b> {discnumber}\n'
                        '<b>Duration:</b> {duration}')
#: The default message title of the notifications
DEFAULT_MESSAGE_TITLE = 'Current Status: {status}'
