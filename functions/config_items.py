#!/usr/bin/env python
# -*- coding: utf-8 -*-

# some related commands:
# C:\>py -3.4 C:\Python34\Tools\i18n\pygettext.py -d guess guess.py
# python C:\Python\Python39\Tools\i18n\pygettext.py --extract-all --default-domain=main --output-dir=locales
#        main_window.py
# python C:\Python\Python39\Tools\i18n\pygettext.py -v -d base -o locales/base.pot main_window.py

# System libs
import os
import os.path

from . import glob

global _


def get_config_item(itemtoget):
    """ Retrieves requested configuration setting from coinv2.config file.

    Args:
        itemtoget: sting.

    Returns:
        Returns value found for requested configuration item.
    """
    with open(os.path.join(glob.mainpath, 'coinsv2.config'), "r") as fp:
        for line in fp:
            if not line.startswith('#'):
                if itemtoget in line:
                    line = line.split("=", 1)
                    if isinstance(line[-1], str):
                        line[-1] = line[-1].strip()
                        return line[-1]
                    else:
                        return line[-1]
