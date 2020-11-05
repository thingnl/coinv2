#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import os
import gettext

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from win32api import GetSystemMetrics                       # win32api is part of pywin32

# Set up message catalog access
gettext.bindtextdomain('Pecuniae_Collectio', '/locales')
gettext.textdomain('Pecuniae_Collectio')
_ = gettext.gettext

# https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/
# https://simpleit.rocks/python/how-to-translate-a-python-project-with-gettext-the-easy-way/

# C:\>py -3.4 C:\Python34\Tools\i18n\pygettext.py -d guess guess.py
# python C:\Python\Python39\Tools\i18n\pygettext.py --extract-all --default-domain=main --output-dir=locales main_window.py


class glob:
    # system vars
    scriptpath = os.path.dirname(os.path.realpath(__file__))
    screen_width = 0
    screen_height = 0
    screen_width_calc = 0
    screen_height_calc = 0
    screen_top = 0
    screen_left = 0

    # SQL connection
    connection = 0

    # frames
    filterframe = 0
    buttonframe = 0
    sqlframe = 0
    photoframe = 0
    messageframe = 0


def get_screen_size():
    glob.screen_width = GetSystemMetrics(0)
    glob.screen_height = GetSystemMetrics(1)
    # resize to 70%
    glob.screen_width_calc = int(glob.screen_width * .7)
    glob.screen_height_calc = int(glob.screen_height * .7)
    glob.screen_left = int((glob.screen_width - glob.screen_width_calc) / 2)
    glob.screen_top = int((glob.screen_height - glob.screen_height_calc) / 2)


def newfile():
    pass


def about():
    pass


def opendb():
    pass


def main_window():
    get_screen_size()
    root = Tk()
    root.title('Pecuniae Collectio')
    root.geometry('%sx%s+%s+%s' % (glob.screen_width_calc, glob.screen_height_calc,
                                   glob.screen_left, glob.screen_top))
    root.option_add("*Font", "Segoe 8")

    # Add menubar to main window
    menu = Menu(root)
    root.config(menu=menu)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)

    # Menu's
    filemenu = Menu(root, tearoff=0)
    menu.add_cascade(label=_("File"), menu=filemenu)
    filemenu.add_command(label=_("New"), command=newfile)
    filemenu.add_command(label=_("Open"), command=opendb())
    filemenu.add_command(label=_("Close"), command=newfile)
    filemenu.add_command(label=_("Save"), command=newfile)
    filemenu.add_separator()
    filemenu.add_command(label=_("Exit"), command=root.quit)

    tablemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label=_("Tables"), menu=tablemenu)
    tablemenu.add_command(label=_("Countries"), command=about)
    tablemenu.add_command(label=_("Suppliers"), command=about)
    tablemenu.add_command(label=_("Orders"), command=about)
    tablemenu.add_command(label=_("Rarity"), command=about)

    datamenu = Menu(menu, tearoff=0)
    menu.add_cascade(label=_("Data"), menu=datamenu)
    datamenu.add_command(label=_("Export"), command=about)
    datamenu.add_command(label=_("Import"), command=about)

    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label=_("Help"), menu=helpmenu)
    helpmenu.add_command(label=_("About"), command=about)
    helpmenu.add_command(label=_("Manual"), command=about)
    helpmenu.add_command(label=_("Support"), command=about)

    # Frames
    glob.filterframe = Frame(root, bg="red", height=700, width=185, padx=5, pady=5)  # left
    glob.buttonframe = Frame(root, bg="yellow", width=900)  # buttons
    glob.sqlframe = Frame(root, bg="green", width=900)  # center
    glob.photoframe = Frame(root, bg="red", height=700, width=185, padx=5, pady=5)  # right
    glob.messageframe = Frame(root, bg="blue", width=1100)  # message

    glob.filterframe.grid(row=0, column=0, rowspan=2, columnspan=1, sticky=E + W + N + S)  # left
    glob.buttonframe.grid(row=0, column=1, sticky=E + W + N + S)  # buttons
    glob.sqlframe.grid(row=1, column=1, sticky=E + W + N + S)  # center
    glob.photoframe.grid(row=0, column=2, rowspan=2, columnspan=1, sticky=E + W + N + S)  # right
    glob.messageframe.grid(row=2, column=0, rowspan=1, columnspan=3, sticky=E + W + N + S)  # message

    glob.filter_frame = LabelFrame(glob.filterframe, text=_("Filters"), height=650, width=175,
                                   relief=RIDGE, bd=2, bg="gray85")  # bg="gray85"
    glob.filter_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
    glob.filter_frame.place(anchor=NW)

    glob.button_filter_apply = Button(glob.filterframe, text=_("Apply filters"), command=root.quit)
    glob.button_filter_apply.place(relx=0.5, rely=0.96, anchor=CENTER)

    glob.filter_label_country = Label(glob.filter_frame, text=_("Country"), bg="gray85")
    glob.filter_label_country.place(anchor=W, bordermode=INSIDE)
    glob.filter_label_country.place(relx=0.02, rely=0.03)

    glob.combo_country = ttk.Combobox(glob.filter_frame)
    glob.combo_country.place(relx=0.10, rely=0.05)

    glob.filter_label_denomination = Label(glob.filter_frame, text=_("Denomination"), bg="gray85")
    glob.filter_label_denomination.place(anchor=W, bordermode=INSIDE)
    glob.filter_label_denomination.place(relx=0.02, rely=0.12)

    glob.combo_denomination = ttk.Combobox(glob.filter_frame)
    glob.combo_denomination.place(relx=0.10, rely=0.14)

    glob.button_add = Button(glob.buttonframe, text=_("Add"), command=about, padx=20)
    glob.button_add.pack(side=LEFT, pady=10, padx=10)

    glob.button_copy = Button(glob.buttonframe, text=_("Copy"), command=about, padx=20)
    glob.button_copy.pack(side=LEFT, pady=10, padx=10)

    glob.button_del = Button(glob.buttonframe, text=_("Delete"), command=about, padx=20)
    glob.button_del.pack(side=LEFT, pady=10, padx=10)

    glob.photo_frame = LabelFrame(glob.photoframe, text=_("Scans"), height=650, width=175,
                                  relief=FLAT, bg="gray85")
    glob.photo_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
    glob.photo_frame.place(anchor=NW)

    glob.right_front_frame = LabelFrame(glob.photo_frame, text=_("Front"), height=170, width=170,
                                        relief=RIDGE, bd=2, bg="gray85")
    glob.right_front_frame.pack(fill=BOTH, expand=1, padx=5, pady=1)
    glob.right_front_frame.place(anchor=NW, relx=0.00)
    glob.right_front_canvas = Canvas(glob.right_front_frame, width=165, height=165, bd=0, highlightthickness=0,
                                    relief='ridge', bg="gray85")
    #glob.right_front_canvas.bind("<Double-1>", doubleclick_front)
    glob.right_front_canvas.pack()

    glob.right_rear_frame = LabelFrame(glob.photo_frame, text=_("Rear"), height=170, width=170,
                                       relief=RIDGE, bd=2, bg="gray85")
    glob.right_rear_frame.pack(fill=BOTH, expand=1, padx=5, pady=1)
    glob.right_rear_frame.place(anchor=NW, relx=0.00, rely=0.29)
    glob.right_rear_canvas = Canvas(glob.right_rear_frame, width=165, height=165, bd=0, highlightthickness=0,
                                    relief='ridge', bg="gray85")
    #glob.right_rear_canvas.bind("<Double-1>", doubleclick_rear)
    glob.right_rear_canvas.pack()

    glob.right_value_frame = LabelFrame(glob.photo_frame, text=_("Value"), height=170, width=170,
                                        relief=RIDGE, bd=2, bg="gray85")
    glob.right_value_frame.pack()
    glob.right_value_frame.place(anchor=NW, relx=0.00, rely=0.58)
    glob.right_value_canvas = Canvas(glob.right_value_frame, width=165, height=165, bd=0, highlightthickness=0,
                                     relief='ridge', bg="gray85")
    glob.right_value_canvas.pack()

    root.mainloop()
