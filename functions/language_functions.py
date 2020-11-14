#!/usr/bin/env python
# -*- coding: utf-8 -*-

# some related commands:
# C:\>py -3.4 C:\Python34\Tools\i18n\pygettext.py -d guess guess.py
# python C:\Python\Python39\Tools\i18n\pygettext.py --extract-all --default-domain=main --output-dir=locales
#        main_window.py
# python C:\Python\Python39\Tools\i18n\pygettext.py -v -d base -o locales/base.pot main_window.py

# System libs
# import os
# import sys
# import gettext
# import os.path
import gettext
# from . import config_window as cwd
# from . import config_items as ci
from . import glob

global _

def send_message(message_text):
    glob.message_frame.delete("1.0", "end")
    glob.message_frame.insert("1.0", message_text)


def language_nl():
    nl = gettext.translation('base', localedir='locales', languages=['nl'])
    nl.install()
    _ = nl.gettext


def language_en():
    en150 = gettext.translation('base', localedir='locales', languages=['en_150'])
    en150.install()
    _ = en150.gettext
