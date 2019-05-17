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
    'duration',
    'albumartist'
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
#: The default path of the configuration file
DEFAULT_CONFIGURATION_FILE = '~/.cmus-notify'
#: The various configuration sections
CONFIGURATION_SECTIONS = (
    'notifications',
    'format'
)
#: The various options
DEFAULT_OPTIONS = {
    'body': DEFAULT_MESSAGE_BODY,
    'title': DEFAULT_MESSAGE_TITLE,
    'application_name': DEFAULT_APPLICATION_NAME,
    'timeout': DEFAULT_TIMEOUT
}
