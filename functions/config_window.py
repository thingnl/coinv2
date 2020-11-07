#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import os
import gettext
import os.path
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from PIL import Image, ImageTk
from win32api import GetSystemMetrics                       # win32api is part of pywin32


global _

def edit_settings():

    # todo: check if config exists, if so load into globs (that still need to be defined!)

    top = Toplevel()
    top.title(_("Edit settings"))
    top.geometry('%sx%s' % (800, 550))
    top.option_add("*Font", "Segoe 8")

    # Create frames
    edit_frame = Frame(master=top, padx=5, pady=5)  # main edit part
    # edit_frame = Frame(master=top, bg="yellow", padx=5, pady=5)  # main edit part
    button_frame = Frame(master=top, height=70, bg="gray85", padx=5, pady=5)  # bottom buttons
    # button_frame = Frame(master=top, height=70, bg="red", padx=5, pady=5, )  # bottom buttons

    edit_frame.pack(fill=BOTH, expand=1)  # main edit part
    button_frame.pack(fill=BOTH, expand=0)  # bottom buttons

    # screen sliders
    label_mainwindow = Label(edit_frame, text=_("Screensize:"),
                             font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_mainwindow.grid(row=1, column=1, columnspan=2)
    label_horizontal = Label(edit_frame, text=_("Horizontal:"), anchor="e", width=20)
    label_horizontal.grid(row=2, column=1)
    label_vertical = Label(edit_frame, text=_("Vertical:"), anchor="e", width=20)
    label_vertical.grid(row=3, column=1)
    # for now use horizontal 90%, vertical 70%
    glob.slide_horizontal = Scale(edit_frame, from_=0, to=100, length=150, tickinterval=25, orient=HORIZONTAL)
    glob.slide_horizontal.set(90)        # todo: get from config sile
    glob.slide_horizontal.grid(row=2, column=2, columnspan=2)
    glob.slide_vertical = Scale(edit_frame, from_=0, to=100, length=150, tickinterval=25, orient=HORIZONTAL)
    glob.slide_vertical.set(70)          # todo: get from config sile
    glob.slide_vertical.grid(row=3, column=2, columnspan=2)

    label_emptyline = Label(edit_frame, text="")
    label_emptyline.grid(row=4, column=1)
    label_emptyline = Label(edit_frame, text="", width=20)
    label_emptyline.grid(row=1, column=4)

    # directories
    label_directories = Label(edit_frame, text=_("File locations:"),
                              font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_directories.grid(row=5, column=1, columnspan=2)
    label_database = Label(edit_frame, text=_("Databases:"), anchor="e", width=20)
    label_database.grid(row=6, column=1)
    glob.loc_database = Entry(edit_frame)
    glob.loc_database.insert(10, "F:/py-dev/coinv2/database")
    glob.loc_database.grid(row=6, column=2, columnspan=3, sticky=NSEW)
    button_database = Button(edit_frame, text="▽", command=lambda: about)
    button_database.grid(row=6, column=5, sticky='w')

    label_scans = Label(edit_frame, text=_("Scans:"), anchor="e", width=20)
    label_scans.grid(row=7, column=1)
    glob.loc_scans = Entry(edit_frame)
    glob.loc_scans.insert(10, "F:/py-dev/coinv2/images")
    glob.loc_scans.grid(row=7, column=2, columnspan=3, sticky=NSEW)
    button_scans = Button(edit_frame, text="▽", command=lambda: about)
    button_scans.grid(row=7, column=5, sticky='w')

    label_orders = Label(edit_frame, text=_("Orders:"), anchor="e", width=20)
    label_orders.grid(row=8, column=1)
    glob.loc_orders = Entry(edit_frame)
    glob.loc_orders.insert(10, "F:/py-dev/coinv2/orders")
    glob.loc_orders.grid(row=8, column=2, columnspan=3, sticky=NSEW)
    button_orders = Button(edit_frame, text="▽", command=lambda: about)
    button_orders.grid(row=8, column=5, sticky='w')

    label_logs = Label(edit_frame, text=_("Logs:"), anchor="e", width=20)
    label_logs.grid(row=9, column=1)
    glob.loc_logs = Entry(edit_frame)
    glob.loc_logs.insert(10, "F:/py-dev/coinv2/logs")
    glob.loc_logs.grid(row=9, column=2, columnspan=3, sticky=NSEW)
    button_logs = Button(edit_frame, text="▽", command=lambda: about)
    button_logs.grid(row=9, column=5, sticky='w')

    label_backups = Label(edit_frame, text=_("Backup's:"), anchor="e", width=20)
    label_backups.grid(row=10, column=1)
    glob.loc_backups = Entry(edit_frame)
    glob.loc_backups.insert(10, "F:/py-dev/coinv2/backup")
    glob.loc_backups.grid(row=10, column=2, columnspan=3, sticky=NSEW)
    button_backups = Button(edit_frame, text="▽", command=lambda: about)
    button_backups.grid(row=10, column=5, sticky='w')

    label_emptyline = Label(edit_frame, text="")
    label_emptyline.grid(row=11, column=1)

    # language
    label_language = Label(edit_frame, text=_("Language:"), font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_language.grid(row=12, column=1, columnspan=2)
    label_langsel = Label(edit_frame, text=_("Language:"), anchor="e", width=20)
    label_langsel.grid(row=13, column=1)

    radioValue = tk.IntVar()
    # add , indicatoron = 0 to tk.radiobutton for button type selector
    glob.radio1_language = tk.Radiobutton(edit_frame, text=_("English"), variable=radioValue, value=1, anchor="w", width=20)
    glob.radio2_language = tk.Radiobutton(edit_frame, text=_("Dutch"), variable=radioValue, value=2, anchor="w", width=20)
    glob.radio1_language.grid(row=13, column=2)
    glob.radio2_language.grid(row=14, column=2)
    glob.radio2_language.select()






    # open last database on startup
    # Include jpg in backup
    # Include orders in backup


    # answer = filedialog.askdirectory(parent=edit_frame,
    #                                  initialdir=os.getcwd(),
    #                                  title="Please select a folder:")
    # print(answer)
