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

"""Contains the types related to Cmus output."""

from .constants import DEFAULT_STATUS_DISPLAY


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
