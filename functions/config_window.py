#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import os
import time

from os import path

from tkinter import filedialog
from tkinter import *

from . import glob
from . import language_functions as lf
from . import config_items as ci

global _


def get_database_dir():
    """ Ask user for directory to store databases.

    Args:
        None.

    Returns:
        Path to database storage location.
    """
    answer = filedialog.askdirectory(parent=glob.edit_edit_frame, initialdir=glob.scriptpath,
                                     title=_("Select databases folder:"))
    if answer != "":
        glob.loc_database.delete(0, 'end')
        glob.loc_database.insert(10, answer)


def get_scans_dir():
    """ Ask user for directory to store pictures/scans.

    Args:
        None.

    Returns:
        Path to pictures/scans storage location.
    """
    answer = filedialog.askdirectory(parent=glob.edit_edit_frame, initialdir=glob.scriptpath,
                                     title=_("Select scans folder:"))
    if answer != "":
        glob.loc_scans.delete(0, 'end')
        glob.loc_scans.insert(10, answer)


def get_orders_dir():
    """ Ask user for directory to store pdf orders.

    Args:
        None.

    Returns:
        Path to pdf storage location.
    """
    answer = filedialog.askdirectory(parent=glob.edit_edit_frame, initialdir=glob.scriptpath,
                                     title=_("Select orders folder:"))
    if answer != "":
        glob.loc_orders.delete(0, 'end')
        glob.loc_orders.insert(10, answer)


def get_logs_dir():
    """ Ask user for directory to store log files.

    Args:
        None.

    Returns:
        Path to logs storage location.
    """
    answer = filedialog.askdirectory(parent=glob.edit_edit_frame, initialdir=glob.scriptpath,
                                     title=_("Select logs folder:"))
    if answer != "":
        glob.loc_logs.delete(0, 'end')
        glob.loc_logs.insert(10, answer)


def get_backups_dir():
    """ Ask user for directory to store backup files.

    Args:
        None.

    Returns:
        Path to backup storage location.
    """
    answer = filedialog.askdirectory(parent=glob.edit_edit_frame, initialdir=glob.scriptpath,
                                     title=_("Select backups folder:"))
    if answer != "":
        glob.loc_backups.delete(0, 'end')
        glob.loc_backups.insert(10, answer)


def get_current_settings():
    """ Get all the settings for the system configuration screen.

    Args:
        None.

    Returns:
        Returns nothing but put all the settings directly on screen.
    """
    config_file = glob.mainpath + "\\coinsv2.config"
    if not path.exists(config_file):
        glob.slide_horizontal.set(70)
        glob.slide_vertical.set(70)
        glob.loc_database.insert(10, glob.scriptpath + "\\database")
        glob.loc_scans.insert(10, glob.scriptpath + "\\images")
        glob.loc_orders.insert(10, glob.scriptpath + "\\orders")
        glob.loc_logs.insert(10, glob.scriptpath + "\\logs")
        glob.loc_backups.insert(10, glob.scriptpath + "\\backup")
    else:
        glob.slide_horizontal.set(ci.get_config_item("slide_horizontal"))
        glob.slide_vertical.set(ci.get_config_item("slide_vertical"))

        glob.loc_database.insert(10, ci.get_config_item("loc_database"))
        glob.loc_scans.insert(10, ci.get_config_item("loc_scans"))
        glob.loc_orders.insert(10, ci.get_config_item("loc_orders"))
        glob.loc_logs.insert(10, ci.get_config_item("loc_logs"))
        glob.loc_backups.insert(10, ci.get_config_item("loc_backups"))
        # langsel = cwd.get_config_item("language_selected")
        if ci.get_config_item("language_selected") == "GB":
            glob.language.set(1)
        else:
            glob.language.set(2)


def build_edit_settings():
    glob.top = Toplevel()
    glob.top.title(_("Edit settings"))
    glob.top.geometry('%sx%s' % (800, 550))
    glob.top.option_add("*Font", "Segoe 8")
    glob.top.grab_set()                      # Disable input on main window.

    # Create frames
    glob.edit_edit_frame = Frame(master=glob.top, padx=5, pady=5)                            # main edit part
    glob.edit_button_frame = Frame(master=glob.top, height=70, bg="gray85", padx=5, pady=5)  # bottom buttons

    glob.edit_edit_frame.pack(fill=BOTH, expand=1)
    glob.edit_button_frame.pack(fill=BOTH, expand=0)

    # Create buttons
    glob.button_edit_cancel = Button(glob.edit_button_frame, text=_("Cancel"),
                                     command=lambda: glob.top.destroy(), padx=20)
    glob.button_edit_cancel.pack(side=LEFT, pady=10, padx=10)

    glob.button_edit_save = Button(glob.edit_button_frame, text=_("Save"), command=lambda: save_settings(), padx=20)
    glob.button_edit_save.pack(side=RIGHT, pady=10, padx=10)

    # screen sliders
    label_mainwindow = Label(glob.edit_edit_frame, text=_("Screensize:"),
                             font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_mainwindow.grid(row=1, column=1, columnspan=2)
    label_horizontal = Label(glob.edit_edit_frame, text=_("Horizontal:"), anchor="e", width=20)
    label_horizontal.grid(row=2, column=1)
    label_vertical = Label(glob.edit_edit_frame, text=_("Vertical:"), anchor="e", width=20)
    label_vertical.grid(row=3, column=1)

    glob.slide_horizontal = Scale(glob.edit_edit_frame, from_=0, to=100, length=150, tickinterval=25, orient=HORIZONTAL)
    glob.slide_horizontal.grid(row=2, column=2, columnspan=2)
    glob.slide_vertical = Scale(glob.edit_edit_frame, from_=0, to=100, length=150, tickinterval=25, orient=HORIZONTAL)
    glob.slide_vertical.grid(row=3, column=2, columnspan=2)

    label_emptyline = Label(glob.edit_edit_frame, text="")
    label_emptyline.grid(row=4, column=1)
    label_emptyline = Label(glob.edit_edit_frame, text="", width=20)
    label_emptyline.grid(row=1, column=4)

    # directories
    label_directories = Label(glob.edit_edit_frame, text=_("File locations:"),
                              font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_directories.grid(row=5, column=1, columnspan=2)
    label_database = Label(glob.edit_edit_frame, text=_("Databases:"), anchor="e", width=20)
    label_database.grid(row=6, column=1)
    glob.loc_database = Entry(glob.edit_edit_frame)
    glob.loc_database.grid(row=6, column=2, columnspan=3, sticky=NSEW)
    button_database = Button(glob.edit_edit_frame, text="▽", command=lambda: get_database_dir())
    button_database.grid(row=6, column=5, sticky='w')

    label_scans = Label(glob.edit_edit_frame, text=_("Scans:"), anchor="e", width=20)
    label_scans.grid(row=7, column=1)
    glob.loc_scans = Entry(glob.edit_edit_frame)
    glob.loc_scans.grid(row=7, column=2, columnspan=3, sticky=NSEW)
    button_scans = Button(glob.edit_edit_frame, text="▽", command=lambda: get_scans_dir())
    button_scans.grid(row=7, column=5, sticky='w')

    label_orders = Label(glob.edit_edit_frame, text=_("Orders:"), anchor="e", width=20)
    label_orders.grid(row=8, column=1)
    glob.loc_orders = Entry(glob.edit_edit_frame)
    glob.loc_orders.grid(row=8, column=2, columnspan=3, sticky=NSEW)
    button_orders = Button(glob.edit_edit_frame, text="▽", command=lambda: get_orders_dir())
    button_orders.grid(row=8, column=5, sticky='w')

    label_logs = Label(glob.edit_edit_frame, text=_("Logs:"), anchor="e", width=20)
    label_logs.grid(row=9, column=1)
    glob.loc_logs = Entry(glob.edit_edit_frame)
    glob.loc_logs.grid(row=9, column=2, columnspan=3, sticky=NSEW)
    button_logs = Button(glob.edit_edit_frame, text="▽", command=lambda: get_logs_dir())
    button_logs.grid(row=9, column=5, sticky='w')

    label_backups = Label(glob.edit_edit_frame, text=_("Backup's:"), anchor="e", width=20)
    label_backups.grid(row=10, column=1)
    glob.loc_backups = Entry(glob.edit_edit_frame)
    glob.loc_backups.grid(row=10, column=2, columnspan=3, sticky=NSEW)
    button_backups = Button(glob.edit_edit_frame, text="▽", command=lambda: get_backups_dir())
    button_backups.grid(row=10, column=5, sticky='w')

    label_emptyline = Label(glob.edit_edit_frame, text="")
    label_emptyline.grid(row=11, column=1)

    # language
    label_language = Label(glob.edit_edit_frame, text=_("Language:"), font=("Segoe", 10, 'bold underline'),
                           anchor="w", width=20)
    label_language.grid(row=12, column=1, columnspan=2)
    label_langsel = Label(glob.edit_edit_frame, text=_("Language:"), anchor="e", width=20)
    label_langsel.grid(row=13, column=1)
    glob.language = IntVar()
    glob.radio1_language = Radiobutton(glob.edit_edit_frame, text=_("English"), variable=glob.language,
                                       value=1, anchor="w", width=20)
    glob.radio2_language = Radiobutton(glob.edit_edit_frame, text=_("Dutch"), variable=glob.language,
                                       value=2, anchor="w", width=20)

    glob.radio1_language.grid(row=13, column=2)
    glob.radio2_language.grid(row=14, column=2)


def save_settings():
    # Rename config file to backup config file
    config_file = glob.mainpath + "\\coinsv2.config"
    new_config_file = glob.mainpath + "\\coinsv2.config.new"

    # Open existing config file for input
    file1 = open(config_file, 'r')

    # Open new config file for output
    file2 = open(new_config_file, 'w')

    for line in file1:
        if line.startswith('slide_horizontal'):
            file2.write("slide_horizontal = " + str(glob.slide_horizontal.get()) + '\n')
        elif line.startswith('slide_vertical'):
            file2.write("slide_vertical = " + str(glob.slide_vertical.get()) + '\n')
        elif line.startswith('loc_database'):
            file2.write("loc_database = " + str(glob.loc_database.get()) + '\n')
        elif line.startswith('loc_scans'):
            file2.write("loc_scans = " + str(glob.loc_scans.get()) + '\n')
        elif line.startswith('loc_orders'):
            file2.write("loc_orders = " + str(glob.loc_orders.get()) + '\n')
        elif line.startswith('loc_logs'):
            file2.write("loc_logs = " + str(glob.loc_logs.get()) + '\n')
        elif line.startswith('loc_backups'):
            file2.write("loc_backups = " + str(glob.loc_backups.get()) + '\n')
        elif line.startswith('language_selected'):
            if glob.language.get() == 1:
                file2.write("language_selected = GB\n")
            else:
                file2.write("language_selected = NL\n")
        else:
            file2.write(line)

    # Closing files
    file1.close()
    file2.close()

    # Rename current file
    os.rename(config_file, config_file + "." + time.strftime("%Y%m%d-%H%M%S"))

    # Rename new config file
    os.rename(new_config_file, config_file)

    lf.send_message(_("New settings saved to configuration file."))

    # Close edit window
    glob.top.destroy()


def edit_settings():
    build_edit_settings()
    get_current_settings()

    # open last database on startup?
    # Include jpg in backup?
    # Include orders in backup?
    # log SQL data?
    # max days to keep logs, 0 = keep all?

    # get a directory
    # answer = filedialog.askdirectory(parent=edit_frame,
    #                                  initialdir=os.getcwd(),
    #                                  title="Please select a folder:")
    # print(answer)
