"""Contains the code related to parsing Cmus output."""

from collections import defaultdict
from functools import reduce, partial

from .constants import FIELDS
from .types import StatusInformation


def parse_status_information(informations):
    """Parse the status informations from the informations list.

    :param informations: The list containing the various song's information
    :type informations: str
    :returns: :class:`collections.defaultdict`
    """
    fields = set(FIELDS)
    status_information = defaultdict(list)
    current_status = None
    for word in informations.split():
        if word in fields:
            current_status = word
        if current_status and word not in fields:
            status_information[current_status].append(word)

    return _format_status_information_fields(
        status_information,
        partial(_format_artist_field, 'artist'),
        partial(_format_artist_field, 'albumartist'),
        _format_duration_field,
        partial(_format_integer_field, 'tracknumber'),
        partial(_format_integer_field, 'discnumber'),
        _format_status_field,
        _format_left_fields
    )


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


def _format_artist_field(field_name, status_information):
    """Format the *artist* field.

    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :returns: The updated status informations
    :rtype: :class:`collections.defaultdict`
    """
    status_information[field_name] = ' '.join(status_information[field_name])
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


def _format_status_field(status_information):
    """Format the *status* field.

    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :returns: The updated status informations
    :rtype: :class:`collections.defaultdict`
    """
    status_information['status'] = (' '.join(status_information['status'])
                                       .capitalize())
    return status_information


def _format_integer_field(field_name, status_information):
    """Format an integer field.

    :param field_name: The name of the field
    :type field_name: str
    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :returns: The updated status informations
    :rtype: :class:`collections.defaultdict`
    """
    try:
        status_information[field_name] = int(''.join(status_information[field_name]))
    except ValueError:
        status_information.pop(field_name, None)

    return status_information


def _format_left_fields(status_information):
    """Format the unformatted fields.

    :param status_information: The various fields information
    :type status_information: :class:`collections.defaultdict`
    :returns: The updated status informations
    :rtype: :class:`collections.defaultdict`
    """
    for key, value in status_information.copy().items():
        if isinstance(value, list) and value:
            status_information[key] = ' '.join(value)
        elif not value:
            status_information.pop(key, None)
    return status_information
