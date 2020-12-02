#!/usr/bin/env python
# -*- coding: utf-8 -*-


# System libs
import os
import os.path

from . import glob
# from . import journal_functions as jf

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
                        if glob.logger_main != 0:
                            glob.logger_main.debug('Retrieved %s = %s.' % (itemtoget, str(line[-1])))
                        return line[-1]
                    else:
                        if glob.logger_main != 0:
                            glob.logger_main.debug('Retrieved %s = %s.' % (itemtoget, line[-1]))
                        return line[-1]
