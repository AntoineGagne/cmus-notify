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

"""Contains code to format the current status of Cmus."""


def format_notification_message(status_information):
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
                status_information.duration)
    return title, text
