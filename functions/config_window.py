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
# from . import journal_functions as jf

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
        glob.language.set(1)
        glob.sqllog.set("INFO")
        glob.sqllog.set("INFO")
    else:
        glob.slide_horizontal.set(ci.get_config_item("slide_horizontal"))
        glob.slide_vertical.set(ci.get_config_item("slide_vertical"))

        glob.loc_database.insert(10, ci.get_config_item("loc_database"))
        glob.loc_scans.insert(10, ci.get_config_item("loc_scans"))
        glob.loc_orders.insert(10, ci.get_config_item("loc_orders"))
        glob.loc_logs.insert(10, ci.get_config_item("loc_logs"))
        glob.loc_backups.insert(10, ci.get_config_item("loc_backups"))
        if ci.get_config_item("language_selected") == "GB":
            glob.language.set(1)
        else:
            glob.language.set(2)
        glob.mainlog.set(ci.get_config_item("main_log_level"))
        glob.sqllog.set(ci.get_config_item("sql_log_level"))


def build_edit_settings():
    glob.top = Toplevel()
    glob.top.title(_("Edit settings"))
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

    # screen sliders
    label_mainwindow = Label(glob.edit_edit_frame, text=_("Screensize:"),
                             font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_mainwindow.grid(row=1, column=1, columnspan=2)
    label_horizontal = Label(glob.edit_edit_frame, text=_("Horizontal:"), anchor="e", width=20)
    label_horizontal.grid(row=2, column=1)
    label_vertical = Label(glob.edit_edit_frame, text=_("Vertical:"), anchor="e", width=20)
    label_vertical.grid(row=2, column=4)

    glob.slide_horizontal = Scale(glob.edit_edit_frame, from_=0, to=100, length=150, tickinterval=25, orient=HORIZONTAL)
    glob.slide_horizontal.grid(row=2, column=2, columnspan=2)
    glob.slide_vertical = Scale(glob.edit_edit_frame, from_=0, to=100, length=150, tickinterval=25, orient=HORIZONTAL)
    glob.slide_vertical.grid(row=2, column=5, columnspan=2)

    label_emptyline = Label(glob.edit_edit_frame, text="")
    label_emptyline.grid(row=4, column=1)
    label_emptyline = Label(glob.edit_edit_frame, text="", width=20)
    label_emptyline.grid(row=1, column=4)

    # Main log setting
    label_mainlog = Label(glob.edit_edit_frame, text=_("Log levels:"),
                          font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_mainlog.grid(row=5, column=4, columnspan=2)
    label_mainsel = Label(glob.edit_edit_frame, text=_("Level main log:"), anchor="e", width=20)
    label_mainsel.grid(row=6, column=4)
    glob.mainlog = StringVar()
    glob.radio1_mainlog = Radiobutton(glob.edit_edit_frame, text=_("No logging"), variable=glob.mainlog,
                                      value="NOTSET", anchor="w", width=20)
    glob.radio2_mainlog = Radiobutton(glob.edit_edit_frame, text=_("Info"), variable=glob.mainlog,
                                      value="INFO", anchor="w", width=20)
    glob.radio3_mainlog = Radiobutton(glob.edit_edit_frame, text=_("Extended"), variable=glob.mainlog,
                                      value="DEBUG", anchor="w", width=20)

    glob.radio1_mainlog.grid(row=6, column=5)
    glob.radio2_mainlog.grid(row=7, column=5)
    glob.radio3_mainlog.grid(row=8, column=5)

    # SQL log setting
    label_sqllog = Label(glob.edit_edit_frame, text=_("Level sql log:"), anchor="e", width=20)
    label_sqllog.grid(row=6, column=6)
    glob.sqllog = StringVar()
    glob.radio1_sqllog = Radiobutton(glob.edit_edit_frame, text=_("No logging"),
                                     variable=glob.sqllog, value="NOTSET", anchor="w", width=20)
    glob.radio2_sqllog = Radiobutton(glob.edit_edit_frame, text=_("Info"),
                                     variable=glob.sqllog, value="INFO", anchor="w", width=20)
    glob.radio3_sqllog = Radiobutton(glob.edit_edit_frame, text=_("Extended"),
                                     variable=glob.sqllog, value="DEBUG", anchor="w", width=20)

    glob.radio1_sqllog.grid(row=6, column=7)
    glob.radio2_sqllog.grid(row=7, column=7)
    glob.radio3_sqllog.grid(row=8, column=7)

    # directories
    label_emptyline = Label(glob.edit_edit_frame, text="")
    label_emptyline.grid(row=13, column=1)

    label_directories = Label(glob.edit_edit_frame, text=_("File locations:"),
                              font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_directories.grid(row=14, column=1, columnspan=2)
    label_database = Label(glob.edit_edit_frame, text=_("Databases:"), anchor="e", width=20)
    label_database.grid(row=15, column=1)
    glob.loc_database = Entry(glob.edit_edit_frame)
    glob.loc_database.grid(row=15, column=2, columnspan=3, sticky=NSEW)
    button_database = Button(glob.edit_edit_frame, text="▽", command=lambda: get_database_dir())
    button_database.grid(row=15, column=5, sticky='w')

    label_scans = Label(glob.edit_edit_frame, text=_("Scans:"), anchor="e", width=20)
    label_scans.grid(row=16, column=1)
    glob.loc_scans = Entry(glob.edit_edit_frame)
    glob.loc_scans.grid(row=16, column=2, columnspan=3, sticky=NSEW)
    button_scans = Button(glob.edit_edit_frame, text="▽", command=lambda: get_scans_dir())
    button_scans.grid(row=16, column=5, sticky='w')

    label_orders = Label(glob.edit_edit_frame, text=_("Orders:"), anchor="e", width=20)
    label_orders.grid(row=17, column=1)
    glob.loc_orders = Entry(glob.edit_edit_frame)
    glob.loc_orders.grid(row=17, column=2, columnspan=3, sticky=NSEW)
    button_orders = Button(glob.edit_edit_frame, text="▽", command=lambda: get_orders_dir())
    button_orders.grid(row=17, column=5, sticky='w')

    label_logs = Label(glob.edit_edit_frame, text=_("Logs:"), anchor="e", width=20)
    label_logs.grid(row=18, column=1)
    glob.loc_logs = Entry(glob.edit_edit_frame)
    glob.loc_logs.grid(row=18, column=2, columnspan=3, sticky=NSEW)
    button_logs = Button(glob.edit_edit_frame, text="▽", command=lambda: get_logs_dir())
    button_logs.grid(row=18, column=5, sticky='w')

    label_backups = Label(glob.edit_edit_frame, text=_("Backup's:"), anchor="e", width=20)
    label_backups.grid(row=19, column=1)
    glob.loc_backups = Entry(glob.edit_edit_frame)
    glob.loc_backups.grid(row=19, column=2, columnspan=3, sticky=NSEW)
    button_backups = Button(glob.edit_edit_frame, text="▽", command=lambda: get_backups_dir())
    button_backups.grid(row=19, column=5, sticky='w')

    label_emptyline = Label(glob.edit_edit_frame, text="")
    label_emptyline.grid(row=20, column=1)

    # language
    label_language = Label(glob.edit_edit_frame, text=_("Language:"), font=("Segoe", 10, 'bold underline'),
                           anchor="w", width=20)
    label_language.grid(row=5, column=1, columnspan=2)
    label_langsel = Label(glob.edit_edit_frame, text=_("Language:"), anchor="e", width=20)
    label_langsel.grid(row=6, column=1)
    glob.language = IntVar()
    glob.radio1_language = Radiobutton(glob.edit_edit_frame, text=_("English"), variable=glob.language,
                                       value=1, anchor="w", width=20)
    glob.radio2_language = Radiobutton(glob.edit_edit_frame, text=_("Dutch"), variable=glob.language,
                                       value=2, anchor="w", width=20)

    glob.radio1_language.grid(row=6, column=2)
    glob.radio2_language.grid(row=7, column=2)


def save_settings():
    # Rename config file to backup config file
    config_file = glob.mainpath + "\\coinsv2.config"
    new_config_file = glob.mainpath + "\\coinsv2.config.new"

    # Open existing config file for input
    file1 = open(config_file, 'r')

    # Open new config file for output
    file2 = open(new_config_file, 'w')

    glob.logger_main.info("Saving configuration:")
    for line in file1:
        if line.startswith('slide_horizontal'):
            file2.write("slide_horizontal = " + str(glob.slide_horizontal.get()) + '\n')
        elif line.startswith('slide_vertical'):
            file2.write("slide_vertical = " + str(glob.slide_vertical.get()) + '\n')
            glob.logger_main.debug("Wrote slide_vertical = " + str(glob.slide_vertical.get()))
        elif line.startswith('loc_database'):
            file2.write("loc_database = " + str(glob.loc_database.get()) + '\n')
            glob.logger_main.debug("Wrote loc_database = " + str(glob.loc_database.get()))
        elif line.startswith('loc_scans'):
            file2.write("loc_scans = " + str(glob.loc_scans.get()) + '\n')
            glob.logger_main.debug("Wrote loc_scans = " + str(glob.loc_scans.get()))
        elif line.startswith('loc_orders'):
            file2.write("loc_orders = " + str(glob.loc_orders.get()) + '\n')
            glob.logger_main.debug("Wrote loc_orders = " + str(glob.loc_orders.get()))
        elif line.startswith('loc_logs'):
            file2.write("loc_logs = " + str(glob.loc_logs.get()) + '\n')
            glob.logger_main.debug("Wrote loc_logs = " + str(glob.loc_logs.get()))
        elif line.startswith('loc_backups'):
            file2.write("loc_backups = " + str(glob.loc_backups.get()) + '\n')
            glob.logger_main.debug("Wrote loc_backups = " + str(glob.loc_backups.get()))
        elif line.startswith('language_selected'):
            if glob.language.get() == 1:
                file2.write("language_selected = GB\n")
                glob.logger_main.debug("Wrote language_selected = GB")
            else:
                file2.write("language_selected = NL\n")
                glob.logger_main.debug("Wrote language_selected = NL")

        elif line.startswith('main_log_level'):
            file2.write("main_log_level = " + glob.mainlog.get() + '\n')
            glob.logger_main.debug("Wrote main_log_level = " + glob.mainlog.get())

        elif line.startswith('sql_log_level'):
            file2.write("sql_log_level = " + glob.sqllog.get() + '\n')
            glob.logger_main.debug("Wrote sql_log_level = " + glob.sqllog.get())

        else:
            file2.write(line)

    # Closing files
    file1.close()
    file2.close()

    # Rename current file
    os.rename(config_file, config_file + "." + time.strftime("%Y%m%d-%H%M%S"))
    glob.logger_main.debug("Old config moved to " + config_file + "." + time.strftime("%Y%m%d-%H%M%S"))

    # Rename new config file
    os.rename(new_config_file, config_file)

    lf.send_message(_("New settings saved to configuration file."))
    glob.logger_main.info("New settings saved to " + config_file + ".")

    # Close edit window
    glob.top.destroy()


def save_columns():
    # Rename config file to backup config file
    config_file = glob.mainpath + "\\coinsv2.config"
    new_config_file = glob.mainpath + "\\coinsv2.config.new"

    # Open existing config file for input
    file1 = open(config_file, 'r')

    # Open new config file for output
    file2 = open(new_config_file, 'w')

    glob.logger_main.info("Saving columns:")
    for line in file1:
        if line.startswith('radio_private_index'):
            file2.write("radio_private_index = " + str(glob.radio_private_index.get()) + '\n')
            glob.logger_main.debug("Wrote private_index = " + str(glob.radio_private_index.get()))
        elif line.startswith('radio_index'):
            file2.write("radio_index = " + str(glob.radio_index.get()) + '\n')
            glob.logger_main.debug("Wrote radio_index = " + str(glob.radio_index.get()))
        elif line.startswith('radio_krause_index'):
            file2.write("radio_krause_index = " + str(glob.radio_krause_index.get()) + '\n')
            glob.logger_main.debug("Wrote radio_krause_index = " + str(glob.radio_krause_index.get()))
        elif line.startswith('radio_denomination'):
            file2.write("radio_denomination = " + str(glob.radio_denomination.get()) + '\n')
            glob.logger_main.debug("Wrote radio_denomination = " + str(glob.radio_denomination.get()))
        elif line.startswith('radio_valuta'):
            file2.write("radio_valuta = " + str(glob.radio_valuta.get()) + '\n')
            glob.logger_main.debug("Wrote radio_valuta = " + str(glob.radio_valuta.get()))
        elif line.startswith('radio_country'):
            file2.write("radio_country = " + str(glob.radio_country.get()) + '\n')
            glob.logger_main.debug("Wrote radio_country = " + str(glob.radio_country.get()))
        elif line.startswith('radio_year'):
            file2.write("radio_year = " + str(glob.radio_year.get()) + '\n')
            glob.logger_main.debug("Wrote radio_year = " + str(glob.radio_year.get()))
        elif line.startswith('radio_mmt'):
            file2.write("radio_mmt = " + str(glob.radio_mmt.get()) + '\n')
            glob.logger_main.debug("Wrote radio_mmt = " + str(glob.radio_mmt.get()))
        elif line.startswith('radio_quality'):
            file2.write("radio_quality = " + str(glob.radio_quality.get()) + '\n')
            glob.logger_main.debug("Wrote radio_quality = " + str(glob.radio_quality.get()))
        elif line.startswith('radio_remark'):
            file2.write("radio_remark = " + str(glob.radio_remark.get()) + '\n')
            glob.logger_main.debug("Wrote radio_remark = " + str(glob.radio_remark.get()))
        elif line.startswith('radio_coinage'):
            file2.write("radio_coinage = " + str(glob.radio_coinage.get()) + '\n')
            glob.logger_main.debug("Wrote radio_coinage = " + str(glob.radio_coinage.get()))
        elif line.startswith('radio_diameter'):
            file2.write("radio_diameter = " + str(glob.radio_diameter.get()) + '\n')
            glob.logger_main.debug("Wrote radio_diameter = " + str(glob.radio_diameter.get()))
        elif line.startswith('radio_edge '):
            file2.write("radio_edge = " + str(glob.radio_edge.get()) + '\n')
            glob.logger_main.debug("Wrote radio_edge = " + str(glob.radio_edge.get()))
        elif line.startswith('radio_edgetext'):
            file2.write("radio_edgetext = " + str(glob.radio_edgetext.get()) + '\n')
            glob.logger_main.debug("Wrote radio_edgetext = " + str(glob.radio_edgetext.get()))
        elif line.startswith('radio_stiketype'):
            file2.write("radio_stiketype = " + str(glob.radio_stiketype.get()) + '\n')
            glob.logger_main.debug("Wrote radio_stiketype = " + str(glob.radio_stiketype.get()))
        elif line.startswith('radio_weight'):
            file2.write("radio_weight = " + str(glob.radio_weight.get()) + '\n')
            glob.logger_main.debug("Wrote radio_weight = " + str(glob.radio_weight.get()))
        elif line.startswith('radio_designer'):
            file2.write("radio_designer = " + str(glob.radio_designer.get()) + '\n')
            glob.logger_main.debug("Wrote radio_designer = " + str(glob.radio_designer.get()))
        elif line.startswith('radio_frontside'):
            file2.write("radio_frontside = " + str(glob.radio_frontside.get()) + '\n')
            glob.logger_main.debug("Wrote radio_frontside = " + str(glob.radio_frontside.get()))
        elif line.startswith('radio_rearside'):
            file2.write("radio_rearside = " + str(glob.radio_rearside.get()) + '\n')
            glob.logger_main.debug("Wrote radio_rearside = " + str(glob.radio_rearside.get()))
        elif line.startswith('radio_material'):
            file2.write("radio_material = " + str(glob.radio_material.get()) + '\n')
            glob.logger_main.debug("Wrote radio_material = " + str(glob.radio_material.get()))
        elif line.startswith('radio_rarity'):
            file2.write("radio_rarity = " + str(glob.radio_rarity.get()) + '\n')
            glob.logger_main.debug("Wrote radio_rarity = " + str(glob.radio_rarity.get()))
        elif line.startswith('radio_frontjpg'):
            file2.write("radio_frontjpg = " + str(glob.radio_frontjpg.get()) + '\n')
            glob.logger_main.debug("Wrote radio_frontjpg = " + str(glob.radio_frontjpg.get()))
        elif line.startswith('radio_rearjpg'):
            file2.write("radio_rearjpg = " + str(glob.radio_rearjpg.get()) + '\n')
            glob.logger_main.debug("Wrote radio_rearjpg = " + str(glob.radio_rearjpg.get()))
        elif line.startswith('radio_serie'):
            file2.write("radio_serie = " + str(glob.radio_serie.get()) + '\n')
            glob.logger_main.debug("Wrote radio_serie = " + str(glob.radio_serie.get()))
        elif line.startswith('radio_storage'):
            file2.write("radio_storage = " + str(glob.radio_storage.get()) + '\n')
            glob.logger_main.debug("Wrote radio_storage = " + str(glob.radio_storage.get()))
        elif line.startswith('radio_have'):
            file2.write("radio_have = " + str(glob.radio_have.get()) + '\n')
            glob.logger_main.debug("Wrote radio_have = " + str(glob.radio_have.get()))
        elif line.startswith('radio_want'):
            file2.write("radio_want = " + str(glob.radio_want.get()) + '\n')
            glob.logger_main.debug("Wrote radio_want = " + str(glob.radio_want.get()))
        elif line.startswith('radio_ordered'):
            file2.write("radio_ordered = " + str(glob.radio_ordered.get()) + '\n')
            glob.logger_main.debug("Wrote radio_ordered = " + str(glob.radio_ordered.get()))
        elif line.startswith('radio_sale'):
            file2.write("radio_sale = " + str(glob.radio_sale.get()) + '\n')
            glob.logger_main.debug("Wrote radio_sale = " + str(glob.radio_sale.get()))
        elif line.startswith('radio_other'):
            file2.write("radio_other = " + str(glob.radio_other.get()) + '\n')
            glob.logger_main.debug("Wrote radio_other = " + str(glob.radio_other.get()))
        elif line.startswith('radio_supplier'):
            file2.write("radio_supplier = " + str(glob.radio_supplier.get()) + '\n')
            glob.logger_main.debug("Wrote radio_supplier = " + str(glob.radio_supplier.get()))
        elif line.startswith('radio_order'):
            file2.write("radio_order = " + str(glob.radio_order.get()) + '\n')
            glob.logger_main.debug("Wrote radio_order = " + str(glob.radio_order.get()))
        elif line.startswith('radio_price'):
            file2.write("radio_price = " + str(glob.radio_price.get()) + '\n')
            glob.logger_main.debug("Wrote radio_price = " + str(glob.radio_price.get()))
        elif line.startswith('radio_mint '):
            file2.write("radio_mint = " + str(glob.radio_mint.get()) + '\n')
            glob.logger_main.debug("Wrote radio_mint = " + str(glob.radio_mint.get()))
        elif line.startswith('radio_mintmaster'):
            file2.write("radio_mintmaster = " + str(glob.radio_mintmaster.get()) + '\n')
            glob.logger_main.debug("Wrote radio_mintmaster = " + str(glob.radio_mintmaster.get()))
        elif line.startswith('radio_ruler'):
            file2.write("radio_ruler = " + str(glob.radio_ruler.get()) + '\n')
            glob.logger_main.debug("Wrote radio_ruler = " + str(glob.radio_ruler.get()))
        else:
            file2.write(line)

    # Closing files
    file1.close()
    file2.close()

    # Rename current file
    os.rename(config_file, config_file + "." + time.strftime("%Y%m%d-%H%M%S"))
    glob.logger_main.debug("Old config moved to " + config_file + "." + time.strftime("%Y%m%d-%H%M%S"))

    # Rename new config file
    os.rename(new_config_file, config_file)

    lf.send_message(_("New settings saved to configuration file."))
    glob.logger_main.info("New settings saved to " + config_file + ".")

    # Close edit window
    glob.top.destroy()


def build_hide_show():
    glob.top = Toplevel()
    glob.top.title(_("Hide/Show Columns"))
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

    glob.button_edit_save = Button(glob.edit_button_frame, text=_("Save"), command=lambda: save_columns(), padx=20)
    glob.button_edit_save.pack(side=RIGHT, pady=10, padx=10)

    label_mainwindow = Label(glob.edit_edit_frame, text=_("Hide or Show columns:"),
                             font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_mainwindow.grid(row=1, column=1, columnspan=2)

    label_empty_line = Label(glob.edit_edit_frame, text=" ", anchor="w", width=20)
    label_empty_line.grid(row=2, column=1)

    label_fill1_line = Label(glob.edit_edit_frame, text=" ", anchor="w", width=20)
    label_fill1_line.grid(row=2, column=7)
    label_fill2_line = Label(glob.edit_edit_frame, text="Hide")
    label_fill2_line.grid(row=3, column=3)
    label_fill3_line = Label(glob.edit_edit_frame, text="Show")
    label_fill3_line.grid(row=3, column=4)
    label_fill4_line = Label(glob.edit_edit_frame, text="Hide")
    label_fill4_line.grid(row=3, column=9)
    label_fill5_line = Label(glob.edit_edit_frame, text="Show")
    label_fill5_line.grid(row=3, column=10)

    # --------
    label_private_index = Label(glob.edit_edit_frame, text=_("Private Index:"), anchor="w", width=20)
    label_private_index.grid(row=4, column=2)
    glob.radio_private_index = StringVar()
    glob.radio1_private_index = Radiobutton(glob.edit_edit_frame, text="",
                                            variable=glob.radio_private_index, value="Hide")
    glob.radio2_private_index = Radiobutton(glob.edit_edit_frame, text="",
                                            variable=glob.radio_private_index, value="Show")
    glob.radio1_private_index.grid(row=4, column=3)
    glob.radio2_private_index.grid(row=4, column=4)
    # --------
    label_index = Label(glob.edit_edit_frame, text=_("Index:"), anchor="w", width=20)
    label_index.grid(row=5, column=2)
    glob.radio_index = StringVar()
    glob.radio1_index = Radiobutton(glob.edit_edit_frame, text="",
                                    variable=glob.radio_index, value="Hide")
    glob.radio2_index = Radiobutton(glob.edit_edit_frame, text="",
                                    variable=glob.radio_index, value="Show")
    glob.radio1_index.grid(row=5, column=3)
    glob.radio2_index.grid(row=5, column=4)
    # --------
    label_krause_index = Label(glob.edit_edit_frame, text=_("Krause Index:"), anchor="w", width=20)
    label_krause_index.grid(row=6, column=2)
    glob.radio_krause_index = StringVar()
    glob.radio1_krause_index = Radiobutton(glob.edit_edit_frame, text="",
                                           variable=glob.radio_krause_index, value="Hide")
    glob.radio2_krause_index = Radiobutton(glob.edit_edit_frame, text="",
                                           variable=glob.radio_krause_index, value="Show")
    glob.radio1_krause_index.grid(row=6, column=3)
    glob.radio2_krause_index.grid(row=6, column=4)
    # --------
    label_denomination = Label(glob.edit_edit_frame, text=_("Denomination:"), anchor="w", width=20)
    label_denomination.grid(row=7, column=2)
    glob.radio_denomination = StringVar()
    glob.radio1_denomination = Radiobutton(glob.edit_edit_frame, text="",
                                           variable=glob.radio_denomination, value="Hide")
    glob.radio2_denomination = Radiobutton(glob.edit_edit_frame, text="",
                                           variable=glob.radio_denomination, value="Show")
    glob.radio1_denomination.grid(row=7, column=3)
    glob.radio2_denomination.grid(row=7, column=4)
    # --------
    label_valuta = Label(glob.edit_edit_frame, text=_("Valuta:"), anchor="w", width=20)
    label_valuta.grid(row=8, column=2)
    glob.radio_valuta = StringVar()
    glob.radio1_valuta = Radiobutton(glob.edit_edit_frame, text="",
                                     variable=glob.radio_valuta, value="Hide")
    glob.radio2_valuta = Radiobutton(glob.edit_edit_frame, text="",
                                     variable=glob.radio_valuta, value="Show")
    glob.radio1_valuta.grid(row=8, column=3)
    glob.radio2_valuta.grid(row=8, column=4)
    # --------
    label_country = Label(glob.edit_edit_frame, text=_("Country:"), anchor="w", width=20)
    label_country.grid(row=9, column=2)
    glob.radio_country = StringVar()
    glob.radio1_country = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_country, value="Hide")
    glob.radio2_country = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_country, value="Show")
    glob.radio1_country.grid(row=9, column=3)
    glob.radio2_country.grid(row=9, column=4)
    # --------
    label_year = Label(glob.edit_edit_frame, text=_("Year:"), anchor="w", width=20)
    label_year.grid(row=10, column=2)
    glob.radio_year = StringVar()
    glob.radio1_year = Radiobutton(glob.edit_edit_frame, text="",
                                   variable=glob.radio_year, value="Hide")
    glob.radio2_year = Radiobutton(glob.edit_edit_frame, text="",
                                   variable=glob.radio_year, value="Show")
    glob.radio1_year.grid(row=10, column=3)
    glob.radio2_year.grid(row=10, column=4)
    # --------
    label_mmt = Label(glob.edit_edit_frame, text=_("Mintmaster sign:"), anchor="w", width=20)
    label_mmt.grid(row=11, column=2)
    glob.radio_mmt = StringVar()
    glob.radio1_mmt = Radiobutton(glob.edit_edit_frame, text="",
                                         variable=glob.radio_mmt, value="Hide")
    glob.radio2_mmt = Radiobutton(glob.edit_edit_frame, text="",
                                         variable=glob.radio_mmt, value="Show")
    glob.radio1_mmt.grid(row=11, column=3)
    glob.radio2_mmt.grid(row=11, column=4)
    # --------
    label_quality = Label(glob.edit_edit_frame, text=_("Quality:"), anchor="w", width=20)
    label_quality.grid(row=12, column=2)
    glob.radio_quality = StringVar()
    glob.radio1_quality = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_quality, value="Hide")
    glob.radio2_quality = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_quality, value="Show")
    glob.radio1_quality.grid(row=12, column=3)
    glob.radio2_quality.grid(row=12, column=4)
    # --------
    label_remark = Label(glob.edit_edit_frame, text=_("Remark:"), anchor="w", width=20)
    label_remark.grid(row=13, column=2)
    glob.radio_remark = StringVar()
    glob.radio1_remark = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_remark, value="Hide")
    glob.radio2_remark = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_remark, value="Show")
    glob.radio1_remark.grid(row=13, column=3)
    glob.radio2_remark.grid(row=13, column=4)
    # --------
    label_coinage = Label(glob.edit_edit_frame, text=_("Coinage:"), anchor="w", width=20)
    label_coinage.grid(row=14, column=2)
    glob.radio_coinage = StringVar()
    glob.radio1_coinage = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_coinage, value="Hide")
    glob.radio2_coinage = Radiobutton(glob.edit_edit_frame, text="",
                                      variable=glob.radio_coinage, value="Show")
    glob.radio1_coinage.grid(row=14, column=3)
    glob.radio2_coinage.grid(row=14, column=4)
    # --------
    label_diameter = Label(glob.edit_edit_frame, text=_("Diameter:"), anchor="w", width=20)
    label_diameter.grid(row=15, column=2)
    glob.radio_diameter = StringVar()
    glob.radio1_diameter = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_diameter, value="Hide")
    glob.radio2_diameter = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_diameter, value="Show")
    glob.radio1_diameter.grid(row=15, column=3)
    glob.radio2_diameter.grid(row=15, column=4)
    # --------
    label_edge = Label(glob.edit_edit_frame, text=_("Edge:"), anchor="w", width=20)
    label_edge.grid(row=16, column=2)
    glob.radio_edge = StringVar()
    glob.radio1_edge = Radiobutton(glob.edit_edit_frame, text="",
                                   variable=glob.radio_edge, value="Hide")
    glob.radio2_edge = Radiobutton(glob.edit_edit_frame, text="",
                                   variable=glob.radio_edge, value="Show")
    glob.radio1_edge.grid(row=16, column=3)
    glob.radio2_edge.grid(row=16, column=4)
    # --------
    label_edgetext = Label(glob.edit_edit_frame, text=_("Edge text:"), anchor="w", width=20)
    label_edgetext.grid(row=17, column=2)
    glob.radio_edgetext = StringVar()
    glob.radio1_edgetext = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_edgetext, value="Hide")
    glob.radio2_edgetext = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_edgetext, value="Show")
    glob.radio1_edgetext.grid(row=17, column=3)
    glob.radio2_edgetext.grid(row=17, column=4)
    # --------
    label_stiketype = Label(glob.edit_edit_frame, text=_("Strike type:"), anchor="w", width=20)
    label_stiketype.grid(row=18, column=2)
    glob.radio_stiketype = StringVar()
    glob.radio1_stiketype = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_stiketype, value="Hide")
    glob.radio2_stiketype = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_stiketype, value="Show")
    glob.radio1_stiketype.grid(row=18, column=3)
    glob.radio2_stiketype.grid(row=18, column=4)
    # --------
    label_weight = Label(glob.edit_edit_frame, text=_("Weight:"), anchor="w", width=20)
    label_weight.grid(row=19, column=2)
    glob.radio_weight = StringVar()
    glob.radio1_weight = Radiobutton(glob.edit_edit_frame, text="",
                                     variable=glob.radio_weight, value="Hide")
    glob.radio2_weight = Radiobutton(glob.edit_edit_frame, text="",
                                     variable=glob.radio_weight, value="Show")
    glob.radio1_weight.grid(row=19, column=3)
    glob.radio2_weight.grid(row=19, column=4)
    # --------
    label_designer = Label(glob.edit_edit_frame, text=_("Designer:"), anchor="w", width=20)
    label_designer.grid(row=20, column=2)
    glob.radio_designer = StringVar()
    glob.radio1_designer = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_designer, value="Hide")
    glob.radio2_designer = Radiobutton(glob.edit_edit_frame, text="",
                                       variable=glob.radio_designer, value="Show")
    glob.radio1_designer.grid(row=20, column=3)
    glob.radio2_designer.grid(row=20, column=4)
    # --------
    label_frontside = Label(glob.edit_edit_frame, text=_("Front side description:"), anchor="w", width=20)
    label_frontside.grid(row=21, column=2)
    glob.radio_frontside = StringVar()
    glob.radio1_frontside = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_frontside, value="Hide")
    glob.radio2_frontside = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_frontside, value="Show")
    glob.radio1_frontside.grid(row=21, column=3)
    glob.radio2_frontside.grid(row=21, column=4)
    # --------
    label_rearside = Label(glob.edit_edit_frame, text=_("Rear side description:"), anchor="w", width=20)
    label_rearside.grid(row=22, column=2)
    glob.radio_rearside = StringVar()
    glob.radio1_rearside = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_rearside, value="Hide")
    glob.radio2_rearside = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_rearside, value="Show")
    glob.radio1_rearside.grid(row=22, column=3)
    glob.radio2_rearside.grid(row=22, column=4)
    # --------
    label_material = Label(glob.edit_edit_frame, text=_("Material:"), anchor="w", width=20)
    label_material.grid(row=4, column=8)
    glob.radio_material = StringVar()
    glob.radio1_material = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_material, value="Hide")
    glob.radio2_material = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_material, value="Show")
    glob.radio1_material.grid(row=4, column=9)
    glob.radio2_material.grid(row=4, column=10)
    # --------
    label_rarity = Label(glob.edit_edit_frame, text=_("Rarity:"), anchor="w", width=20)
    label_rarity.grid(row=5, column=8)
    glob.radio_rarity = StringVar()
    glob.radio1_rarity = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_rarity, value="Hide")
    glob.radio2_rarity = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_rarity, value="Show")
    glob.radio1_rarity.grid(row=5, column=9)
    glob.radio2_rarity.grid(row=5, column=10)
    # --------
    label_frontjpg = Label(glob.edit_edit_frame, text=_("Front side image:"), anchor="w", width=20)
    label_frontjpg.grid(row=6, column=8)
    glob.radio_frontjpg = StringVar()
    glob.radio1_frontjpg = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_frontjpg, value="Hide")
    glob.radio2_frontjpg = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_frontjpg, value="Show")
    glob.radio1_frontjpg.grid(row=6, column=9)
    glob.radio2_frontjpg.grid(row=6, column=10)
    # --------
    label_rearjpg = Label(glob.edit_edit_frame, text=_("Rear side image:"), anchor="w", width=20)
    label_rearjpg.grid(row=7, column=8)
    glob.radio_rearjpg = StringVar()
    glob.radio1_rearjpg = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_rearjpg, value="Hide")
    glob.radio2_rearjpg = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_rearjpg, value="Show")
    glob.radio1_rearjpg.grid(row=7, column=9)
    glob.radio2_rearjpg.grid(row=7, column=10)
    # --------
    label_serie = Label(glob.edit_edit_frame, text=_("Serie:"), anchor="w", width=20)
    label_serie.grid(row=8, column=8)
    glob.radio_serie = StringVar()
    glob.radio1_serie = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_serie, value="Hide")
    glob.radio2_serie = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_serie, value="Show")
    glob.radio1_serie.grid(row=8, column=9)
    glob.radio2_serie.grid(row=8, column=10)
    # --------
    label_storage = Label(glob.edit_edit_frame, text=_("Storage:"), anchor="w", width=20)
    label_storage.grid(row=9, column=8)
    glob.radio_storage = StringVar()
    glob.radio1_storage = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_storage, value="Hide")
    glob.radio2_storage = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_storage, value="Show")
    glob.radio1_storage.grid(row=9, column=9)
    glob.radio2_storage.grid(row=9, column=10)
    # --------
    label_have = Label(glob.edit_edit_frame, text=_("In collection:"), anchor="w", width=20)
    label_have.grid(row=10, column=8)
    glob.radio_have = StringVar()
    glob.radio1_have = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_have, value="Hide")
    glob.radio2_have = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_have, value="Show")
    glob.radio1_have.grid(row=10, column=9)
    glob.radio2_have.grid(row=10, column=10)
    # --------
    label_want = Label(glob.edit_edit_frame, text=_("Missing from collection:"), anchor="w", width=20)
    label_want.grid(row=11, column=8)
    glob.radio_want = StringVar()
    glob.radio1_want = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_want, value="Hide")
    glob.radio2_want = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_want, value="Show")
    glob.radio1_want.grid(row=11, column=9)
    glob.radio2_want.grid(row=11, column=10)
    # --------
    label_ordered = Label(glob.edit_edit_frame, text=_("On order:"), anchor="w", width=20)
    label_ordered.grid(row=12, column=8)
    glob.radio_ordered = StringVar()
    glob.radio1_ordered = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_ordered, value="Hide")
    glob.radio2_ordered = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_ordered, value="Show")
    glob.radio1_ordered.grid(row=12, column=9)
    glob.radio2_ordered.grid(row=12, column=10)
    # --------
    label_sale = Label(glob.edit_edit_frame, text=_("Is for sale:"), anchor="w", width=20)
    label_sale.grid(row=13, column=8)
    glob.radio_sale = StringVar()
    glob.radio1_sale = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_sale, value="Hide")
    glob.radio2_sale = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_sale, value="Show")
    glob.radio1_sale.grid(row=13, column=9)
    glob.radio2_sale.grid(row=13, column=10)
    # --------
    label_other = Label(glob.edit_edit_frame, text=_("Free to use y/n:"), anchor="w", width=20)
    label_other.grid(row=14, column=8)
    glob.radio_other = StringVar()
    glob.radio1_other = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_other, value="Hide")
    glob.radio2_other = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_other, value="Show")
    glob.radio1_other.grid(row=14, column=9)
    glob.radio2_other.grid(row=14, column=10)
    # --------
    label_supplier = Label(glob.edit_edit_frame, text=_("Supplier:"), anchor="w", width=20)
    label_supplier.grid(row=15, column=8)
    glob.radio_supplier = StringVar()
    glob.radio1_supplier = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_supplier, value="Hide")
    glob.radio2_supplier = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_supplier, value="Show")
    glob.radio1_supplier.grid(row=15, column=9)
    glob.radio2_supplier.grid(row=15, column=10)
    # --------
    label_order = Label(glob.edit_edit_frame, text=_("Order number:"), anchor="w", width=20)
    label_order.grid(row=16, column=8)
    glob.radio_order = StringVar()
    glob.radio1_order = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_order, value="Hide")
    glob.radio2_order = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_order, value="Show")
    glob.radio1_order.grid(row=16, column=9)
    glob.radio2_order.grid(row=16, column=10)
    # --------
    label_price = Label(glob.edit_edit_frame, text=_("Purchase price:"), anchor="w", width=20)
    label_price.grid(row=17, column=8)
    glob.radio_price = StringVar()
    glob.radio1_price = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_price, value="Hide")
    glob.radio2_price = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_price, value="Show")
    glob.radio1_price.grid(row=17, column=9)
    glob.radio2_price.grid(row=17, column=10)
    # --------
    label_mint = Label(glob.edit_edit_frame, text=_("Mint:"), anchor="w", width=20)
    label_mint.grid(row=18, column=8)
    glob.radio_mint = StringVar()
    glob.radio1_mint = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_mint, value="Hide")
    glob.radio2_mint = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_mint, value="Show")
    glob.radio1_mint.grid(row=18, column=9)
    glob.radio2_mint.grid(row=18, column=10)
    # --------
    label_mintmaster = Label(glob.edit_edit_frame, text=_("Mintmaster:"), anchor="w", width=20)
    label_mintmaster.grid(row=19, column=8)
    glob.radio_mintmaster = StringVar()
    glob.radio1_mintmaster = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_mintmaster, value="Hide")
    glob.radio2_mintmaster = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_mintmaster, value="Show")
    glob.radio1_mintmaster.grid(row=19, column=9)
    glob.radio2_mintmaster.grid(row=19, column=10)
    # --------
    label_ruler = Label(glob.edit_edit_frame, text=_("State ruler:"), anchor="w", width=20)
    label_ruler.grid(row=20, column=8)
    glob.radio_ruler = StringVar()
    glob.radio1_ruler = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_ruler, value="Hide")
    glob.radio2_ruler = Radiobutton(glob.edit_edit_frame, text="",
                                        variable=glob.radio_ruler, value="Show")
    glob.radio1_ruler.grid(row=20, column=9)
    glob.radio2_ruler.grid(row=20, column=10)


def edit_settings():
    glob.logger_main.info("Configuration window starting.")
    build_edit_settings()
    get_current_settings()

    glob.logger_main.info("Configuration window closed.")

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


def hide_show_columns():
    glob.logger_main.info("Hide/Show Columns starting.")
    build_hide_show()


    glob.logger_main.info("Hide/Show Columns window closed.")
