===========
cmus-notify
===========

.. image:: https://travis-ci.org/AntoineGagne/cmus-notify.svg?branch=master
    :target: https://travis-ci.org/AntoineGagne/cmus-notify

.. image:: https://img.shields.io/pypi/v/cmus-notify.svg
        :target: https://pypi.python.org/pypi/cmus-notify

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

.. code-block:: sh

    python setup.py install

This program can also be found on `Pypi <https://pypi.python.org/pypi?:action=display&name=cmus-notify>`_ which means you can install it by downloading the wheel or by using the following command:

.. code-block:: sh

    pip install cmus-notify

You can check if it installed correctly by doing the following command:

.. code-block:: sh

    cmus_notify -h

It should display a message.

Hooking To Cmus
===============

To hook this program to ``cmus``, you have to create a shell script that have the following lines in it:

.. code-block:: sh

    #! /bin/sh

    cmus_notify "$*" &

Then, you must make the file executable by using the following command (assuming your script's name is ``cmus_notify.sh``):

.. code-block:: sh

    chmod +x cmus_notify.sh

Finally, once you are in ``cmus``, you can add the hook by using the following command:

.. code-block:: vim

    :set status_display_program=<path-to-the-shell-script>

Customization
=============

If you want you can specify the formatting of the notification by specifying format strings. For example:

.. code-block:: sh

    #! /bin/sh

    cmus_notify --title "Now playing: {title} by {artist}" --body "$(printf "<b>Album:</b> {album}\n<b>Duration:</b> {duration}")" "$*"

You can also specify a configuration to read these values from. By default, the program will search for a configuration file named ``~/.cmus-notify``. It has the following format:

.. code-block:: ini

    [notifications]
        application_name = Cmus
        custom_notification = /home/user/.cmus/custom_notification.py

    [format]
        title = Now playing: {title} by {artist}
        body = <b>Album:</b> {album}
               <b>Duration:</b> {duration}

The options accepts the same values as their command-line options equivalent.

Options
=======

To view the full options, you can run the following command:

.. code-block:: sh

    cmus_notify --help

which will display the following prompt:

.. code-block:: text

    usage: cmus_notify [-h] [-a APPLICATION_NAME] [-b BODY_FORMAT_STRING]
                       [-t TITLE_FORMAT_STRING] [-f CONFIGURATION_FILE]
                       [-c CUSTOM_NOTIFICATION]
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
      -c CUSTOM_NOTIFICATION, --custom_notification CUSTOM_NOTIFICATION
                            The path to a custom implementation of the
                            notification class. If it is not specified, the
                            standard implementation will be used (the one using
                            notify2).

    Format String Parameters
    ========================

    The available arguments to the format strings are the following:

      - album: The song's album
      - albumartist: The song's album's artist
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
