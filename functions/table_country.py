#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
# import time

# from os import path

# from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

from . import glob
# from . import language_functions as lf
# from . import config_items as ci

global _


# Needed for the line coloring stuff
def fixed_map(option):
    return [elm for elm in glob.style.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]


def treeview_sort_column(tv, col, reverse):  # Treeview, column name, arrangement
    listindex = [(tv.set(k, col), k) for k in tv.get_children('')]
    listindex.sort(reverse=reverse)  # Sort by
    for index, (val, k) in enumerate(listindex):  # based on sorted index movement
        tv.move(k, '', index)
        tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

    # Reset the child coloring
    acounter = 0
    for child in glob.sql_frame.get_children():
        if acounter % 2 == 0:
            glob.sql_frame.item(child, tags="even")
            acounter += 1
        else:
            glob.sql_frame.item(child, tags="odd")
            acounter += 1


def load_country_sql():
    sql_command = """SELECT description FROM country ORDER by description"""
    try:
        glob.cur.execute(sql_command)
        glob.country_data = []
        for row in glob.cur.fetchall():
            glob.country_data.append(row[0])
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    # check if sql window exists (no name yet....)
    #   if so, delete
    # create new sql window
    style = ttk.Style()
    style.element_create("Custom.Treeheading.border", "from", "default")
    style.layout("Custom.Treeview.Heading", [
        ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
        ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                ("Custom.Treeheading.text", {'sticky': 'we'})
            ]})
        ]}),
    ])

    # glob.sqlframe
    glob.sql_frame = ttk.Treeview(glob.edit_edit_frame, style = "Custom.Treeview")
    glob.sql_frame['columns'] = ("country")

    # Set colors for odd and even rows
    glob.sql_frame.tag_configure('odd', background='#FFFFFF')  # light blue #FFFFFF
    glob.sql_frame.tag_configure('even', background='#E2FFFF')  # white #E2FFFF

    # Set width for all columns so data fits and/or header shows, while hiding the first index field
    glob.sql_frame.column("#0", width=0, minwidth=0, stretch=NO)
    glob.sql_frame.column("#1", width=300, minwidth=50)
    # Set headings and register sort command
    glob.sql_frame.heading("#1", text="Country", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                "#1", False))

    # fill with countries
    for teller in range(0, len(glob.coin_data)):
        glob.sql_frame.insert(parent='', index='end', iid=teller, text=str(teller), values=glob.country_data[teller])

    # Set color indicators for all lines when we have data
    if len(glob.country_data) != 0:
        # Reset the child coloring
        acounter = 0
        for child in glob.sql_frame.get_children():
            if acounter % 2 == 0:
                glob.sql_frame.item(child, tags="even")
                acounter += 1
            else:
                glob.sql_frame.item(child, tags="odd")
                acounter += 1

    # Inserting horizontal scrollbar
    glob.scrollh = ttk.Scrollbar(glob.sql_frame, orient="horizontal", command=glob.sql_frame.xview)
    glob.scrollh.pack(side=BOTTOM, fill='x')
    glob.sql_frame.configure(xscrollcommand=glob.scrollh.set)

    # Inserting vertical scrollbar
    glob.scrollv = ttk.Scrollbar(glob.sql_frame, orient="vertical", command=glob.sql_frame.yview)
    glob.scrollv.pack(side=RIGHT, fill='y')
    glob.sql_frame.configure(yscrollcommand=glob.scrollv.set)

    # Show the actual data
    glob.sql_frame.pack(fill=BOTH, expand=1)


def build_edit_country():
    glob.top = Toplevel()
    glob.top.title(_("Country table"))
    glob.top.geometry('%sx%s' % (400, 350))
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
    # build_edit_settings()

    load_country_sql()
    # get_current_settings()

    glob.logger_main.info("Country table maintenance closed.")

    pass
