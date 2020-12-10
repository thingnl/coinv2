#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
# import time

# from os import path

# from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

from . import glob
# from . import language_functions as lf
# from . import config_items as ci

global _


def build_edit_country():
    glob.top = Toplevel()
    glob.top.title(_("Country table"))
    glob.top.geometry('%sx%s' % (800, 550))
    glob.top.option_add("*Font", "Segoe 8")
    glob.top.grab_set()                      # Disable input on main window.

    # Create frames
    glob.edit_edit_frame = Frame(master=glob.top, padx=5, pady=5)
    glob.edit_button_frame = Frame(master=glob.top, height=70, bg="gray85", padx=5, pady=5)

    glob.edit_edit_frame.pack(fill=BOTH, expand=1)
    glob.edit_button_frame.pack(fill=BOTH, expand=0)

    # Create buttons
    glob.button_edit_cancel = Button(glob.edit_button_frame, text=_("Cancel"),
                                     command=lambda: glob.top.destroy(), padx=20)
    glob.button_edit_cancel.pack(side=LEFT, pady=10, padx=10)

    glob.button_edit_save = Button(glob.edit_button_frame, text=_("Save"), command=lambda: save_settings(), padx=20)
    glob.button_edit_save.pack(side=RIGHT, pady=10, padx=10)

    pass


def edit_country():

    # log function starting
    # make shure a database is loaded
    # if not, inform and stop
    # if it is:
    #  build screen
    #  get data
    #  save data
    # log closing
    # close screen while leaving database as is.

    glob.logger_main.info("Country table maintenance starting.")

    # Is a database currently loaded?
    if glob.current_open_db == "":
        messagebox.showerror(title=_("Database to use"), message=_("No database is loaded. "
                                                                   "Please open a database first."))
        return

    build_edit_country()
    #build_edit_settings()
    # get_current_settings()

    glob.logger_main.info("Country table maintenance closed.")


    pass
