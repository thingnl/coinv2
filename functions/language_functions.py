#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import gettext

# Own modules
from . import glob

# i18n
global _


def send_message(message_text):
    """ Show message to user at bottom main window.

    Args: message_text

    Returns: Returns nothing, put's message directly on screen.
    """
    glob.message_frame.delete("1.0", "end")
    glob.message_frame.insert("1.0", message_text)
    glob.message_frame.update()                         # force update on frame


def language_nl():
    """ Switch GUI language to Dutch.  For a permanent switch, update setting in the system configuration.

    Args: None

    Returns: Nothing
    """
    nl = gettext.translation('base', localedir='locales', languages=['nl'])
    nl.install()
    _ = nl.gettext
    glob.logger_main.info("Language switched to NL.")


def language_en():
    """ Switch GUI language to English. For a permanent switch, update setting in the system configuration.

    Args: None

    Returns: Nothing
    """
    en150 = gettext.translation('base', localedir='locales', languages=['en_150'])
    en150.install()
    _ = en150.gettext
    glob.logger_main.info("Language switched to GB.")
