#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
import tkinter
import tkinter.filedialog
from . import config_items as ci

from . import glob


def func1():
    """ Placeholder

    Args:

    Returns:
    """
    pass


def savebox():
    glob.logger_main.info("Stating New database function.")
    glob.logger_sql.info("Stating New database function.")
    file_list = [("Databases", ".db"), ("All files", ".*")]
    new_dbfile = tkinter.filedialog.asksaveasfilename(title="Create new database...", filetypes=file_list,
                                                      defaultextension=".db",
                                                      initialdir=ci.get_config_item("loc_database"))
    if new_dbfile != "":
        glob.logger_sql.info("Creating new database: " + new_dbfile)
