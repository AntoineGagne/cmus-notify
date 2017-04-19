===========
cmus-notify
===========

:Author: `Antoine Gagné <antoine.gagne.2@ulaval.ca>`_

.. contents::
    :backlinks: none

.. sectnum::

Requirements
============

To install this program, you must have the following:

- ``python 3.5+``
- The Python library ``notify2``
- ``notify-send``

Installation
============

To install this program, you can simply run the following command:

::

    python setup.py install

This program can also be found on `Pypi <https://pypi.python.org/pypi?:action=display&name=cmus-notify>`_ which means you can install it by downloading the wheel or by using the following command:

::

    pip install cmus-notify

You can check if it installed correctly by doing the following command:

::

    cmus_notify -h

It should display a message.

Hooking To Cmus
===============

To hook this program to ``cmus``, you have to create a shell script that have the following lines in it:

::

    #! /bin/sh

    cmus_notify "$*" &

Then, you must make the file executable by using the following command (assuming your script's name is ``cmus_notify.sh``):

::

    chmod +x cmus_notify.sh

Finally, once you are in ``cmus``, you can add the hook by using the following command:

::

    :set status_display_program=<path-to-the-shell-script>

Customization
=============

If you want you can specify the formatting of the notification by specifying format strings. For example:

::

    #! /bin/sh

    cmus_notify --title "Now playing: {title} by {artist}" --body "<b>Album:</b> {album}\n<b>Duration:</b> {duration}" "$*"

You can also specify a configuration to read these values from. By default, the program will search for a configuration file named ``~/.cmus-notify``. It has the following format:

::

    [notifications]
        application_name = Cmus

    [format]
        title = Now playing: {title} by {artist}
        body = <b>Album:</b> {album}
            <b>Duration:</b> {duration}

The options accepts the same values as their command-line options equivalent.

Options
=======

To view the full options, you can run the following command:

::

    cmus_notify --help

which will display the following prompt:

::

    usage: cmus_notify [-h] [-a APPLICATION_NAME] [-b BODY_FORMAT_STRING]
                       [-t TITLE_FORMAT_STRING] [-f CONFIGURATION_FILE]
                       INFORMATION

    Display a notification about Cmus's current status

    positional arguments:
      INFORMATION           Parse the given information

    optional arguments:
      -h, --help            show this help message and exit
      -a APPLICATION_NAME, --application_name APPLICATION_NAME
                            The name of the application
      -b BODY_FORMAT_STRING, --body BODY_FORMAT_STRING
                            A format string that can be specified to tell the
                            software how to format the body. The syntax is the
                            same as Python's. The available options are specified
                            at the end of this help message. (i.e. 'Artist:
                            {artist}')
      -t TITLE_FORMAT_STRING, --title TITLE_FORMAT_STRING
                            A format string that can be specified to tell the
                            software how to format the title. The syntax is the
                            same as Python's. The available options are specified
                            at the end of this help message. (i.e. 'Now playing:
                            {title}')
      -f CONFIGURATION_FILE, --configuration_file CONFIGURATION_FILE
                            The path to the configuration file. If it is not
                            specified, the program will use the default values of
                            the other options.

    Format String Parameters
    ========================

    The available arguments to the format strings are the following:

      - album: The song's album
      - artist: The song's artist
      - date: The song's release date
      - discnumber: The song's disc's number
      - duration: The song's duration
      - file: The song's file's path
      - status: Cmus current status
      - title: The song's title
      - tracknumber: The song's track number

Documentation
=============

The project's documentation can be found `here <http://pythonhosted.org/cmus-notify/>`_.
