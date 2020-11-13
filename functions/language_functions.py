#!/usr/bin/env python
# -*- coding: utf-8 -*-

# some related commands:
# C:\>py -3.4 C:\Python34\Tools\i18n\pygettext.py -d guess guess.py
# python C:\Python\Python39\Tools\i18n\pygettext.py --extract-all --default-domain=main --output-dir=locales
#        main_window.py
# python C:\Python\Python39\Tools\i18n\pygettext.py -v -d base -o locales/base.pot main_window.py

# System libs
import os
import sys
import gettext
import os.path
import gettext
from . import config_window as cwd
from . import config_items as ci
from . import glob

global _

# def init_language(configdir):
# def init_language():
#     # print("in init_language():-" + glob.mainpath + "-")
#     gettext.textdomain('main')
#     #localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locales')
#     localedir = os.path.join(glob.mainpath, 'locales')
#     translate = gettext.translation('main', localedir, fallback=True)
#     nl = gettext.translation('base', localedir='locales', languages=['nl'])
#     nl.install()
#     en = gettext.translation('base', localedir='locales', languages=['en'])
#     en.install()
#
#     langsel = ci.get_config_item("language_selected")
#     #if ci.get_config_item("language_selected") == "GB":
#     if langsel == "GB":
#         _ = en.gettext
#     else:
#         _ = nl.gettext


# def set_language():
#     print("in set_language():-" + glob.mainpath + "-")
#
#     #langsel = ci.get_config_item("language_selected")
#     if ci.get_config_item("language_selected") == "GB":
#         # _ = translate.gettext
#         _ = en.gettext
#     else:
#         _ = nl.gettext


def language_nl():
    nl = gettext.translation('base', localedir=os.path.join(glob.mainpath, 'locales'), languages=['nl'])
    nl.install()
    _ = nl.gettext
    rebuild_buttons()


def language_en():
    nl = gettext.translation('base', localedir=os.path.join(glob.mainpath, 'locales'), languages=['nl'])
    nl.install()
    _ = gettext.gettext
    rebuild_buttons()