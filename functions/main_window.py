#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import os
import os.path
# import gettext
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
from win32api import GetSystemMetrics                       # win32api is part of pywin32

# Own modules
from . import glob
from . import config_items as ci
from . import config_window as cwd
from . import language_functions as lf
from . import database_new as dbn
# from . import journal_functions as jf

global _


def get_screen_size():
    glob.screen_width = GetSystemMetrics(0)
    glob.screen_height = GetSystemMetrics(1)
    glob.screen_width_setup = int(ci.get_config_item("slide_horizontal"))/100
    glob.screen_height_setup = int(ci.get_config_item("slide_vertical"))/100
    glob.screen_width_calc = int(glob.screen_width * glob.screen_width_setup)
    glob.screen_height_calc = int(glob.screen_height * glob.screen_height_setup)
    glob.screen_left = int((glob.screen_width - glob.screen_width_calc) / 2)
    glob.screen_top = int((glob.screen_height - glob.screen_height_calc) / 2)


def resize(img, max_px_size):
    width_0, height_0 = img.size
    if width_0 >= height_0:
        wpercent = max_px_size / float(width_0)
        hsize = int(float(height_0) * float(wpercent))
        img = img.resize((max_px_size, hsize), Image.ANTIALIAS)
    if width_0 < height_0:
        hpercent = max_px_size / float(height_0)
        wsize = int(float(width_0) * float(hpercent))
        img = img.resize((max_px_size, wsize), Image.ANTIALIAS)
    return img


def newfile():
    pass


def about():
    pass


def opendb():
    pass


def build_menu():
    # Menu
    glob.menu = Menu(glob.root)
    glob.root.config(menu=glob.menu)
    glob.root.columnconfigure(1, weight=1)
    glob.root.rowconfigure(1, weight=1)

    # Menu options
    glob.filemenu = Menu(glob.root, tearoff=0)
    glob.menu.add_cascade(label=_("File"), menu=glob.filemenu)
    glob.filemenu.add_command(label=_("New"), command=lambda: dbn.saveBox())
    glob.filemenu.add_command(label=_("Open"), command=opendb())
    glob.filemenu.add_command(label=_("Close"), command=newfile)
    glob.filemenu.add_command(label=_("Save"), command=newfile)
    glob.filemenu.add_separator()
    glob.filemenu.add_command(label=_("Exit"), command=glob.root.quit)

    glob.tablemenu = Menu(glob.menu, tearoff=0)
    glob.menu.add_cascade(label=_("Tables"), menu=glob.tablemenu)
    glob.tablemenu.add_command(label=_("Countries"), command=about)
    glob.tablemenu.add_command(label=_("Suppliers"), command=about)
    glob.tablemenu.add_command(label=_("Orders"), command=about)
    glob.tablemenu.add_command(label=_("Rarity"), command=about)

    glob.datamenu = Menu(glob.menu, tearoff=0)
    glob.menu.add_cascade(label=_("Data"), menu=glob.datamenu)
    glob.datamenu.add_command(label=_("Export"), command=about)
    glob.datamenu.add_command(label=_("Import"), command=about)
    glob.datamenu.add_command(label=_("Backup"), command=about)
    glob.datamenu.add_command(label=_("Restore"), command=about)

    glob.sysmenu = Menu(glob.menu, tearoff=0)
    glob.menu.add_cascade(label=_("System"), menu=glob.sysmenu)
    glob.sysmenu.add_command(label=_("Settings"), command=lambda: cwd.edit_settings())

    glob.helpmenu = Menu(glob.menu, tearoff=0)
    glob.menu.add_cascade(label=_("Help"), menu=glob.helpmenu)
    glob.helpmenu.add_command(label=_("About"), command=about)
    glob.helpmenu.add_command(label=_("Manual"), command=about)
    glob.helpmenu.add_command(label=_("Support"), command=about)


def build_frames():
    # Frames
    glob.filterframe = Frame(glob.root, bg="red", height=700, width=185, padx=5, pady=5)  # left
    glob.buttonframe = Frame(glob.root, bg="gray85", width=900)  # buttons
    glob.sqlframe = Frame(glob.root, bg="green", width=900)  # center
    glob.photoframe = Frame(glob.root, bg="red", height=700, width=185, padx=5, pady=5)  # right
    glob.messageframe = Frame(glob.root, bg="blue", height=50, width=1100)  # message

    glob.filterframe.grid(row=0, column=0, rowspan=2, columnspan=1, sticky=E + W + N + S)  # left
    glob.buttonframe.grid(row=0, column=1, sticky=E + W + N + S)  # buttons
    glob.sqlframe.grid(row=1, column=1, sticky=E + W + N + S)  # center
    glob.photoframe.grid(row=0, column=2, rowspan=2, columnspan=1, sticky=E + W + N + S)  # right
    glob.messageframe.grid(row=2, column=0, rowspan=1, columnspan=3, sticky=E + W + N + S)  # message

    glob.message_frame = Text(glob.messageframe, height=1)
    glob.message_frame.pack(fill=X, expand=1, padx=5, pady=5)
    lf.send_message(_("Welcome to Pecuniae Collectio"))

    glob.filter_frame = LabelFrame(glob.filterframe, text=_("Filters"), height=650, width=175,
                                   relief=RIDGE, bd=2, bg="gray85")  # bg="gray85"
    glob.filter_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
    glob.filter_frame.place(anchor=NW)

    glob.button_filter_apply = Button(glob.filterframe, text=_("Apply filters"), command=glob.root.quit)
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
    # glob.right_front_canvas.bind("<Double-1>", doubleclick_front)
    glob.right_front_canvas.pack()

    glob.right_rear_frame = LabelFrame(glob.photo_frame, text=_("Rear"), height=170, width=170,
                                       relief=RIDGE, bd=2, bg="gray85")
    glob.right_rear_frame.pack(fill=BOTH, expand=1, padx=5, pady=1)
    glob.right_rear_frame.place(anchor=NW, relx=0.00, rely=0.29)
    glob.right_rear_canvas = Canvas(glob.right_rear_frame, width=165, height=165, bd=0, highlightthickness=0,
                                    relief='ridge', bg="gray85")
    # glob.right_rear_canvas.bind("<Double-1>", doubleclick_rear)
    glob.right_rear_canvas.pack()

    glob.right_value_frame = LabelFrame(glob.photo_frame, text=_("Value"), height=170, width=170,
                                        relief=RIDGE, bd=2, bg="gray85")
    glob.right_value_frame.pack()
    glob.right_value_frame.place(anchor=NW, relx=0.00, rely=0.58)
    glob.right_value_canvas = Canvas(glob.right_value_frame, width=165, height=165, bd=0, highlightthickness=0,
                                     relief='ridge', bg="gray85")
    glob.right_value_canvas.pack()


def build_buttons():
    glob.button_add = Button(glob.buttonframe, text=_("Add"), command=about, padx=20)
    glob.button_add.pack(side=LEFT, pady=10, padx=10)

    glob.button_copy = Button(glob.buttonframe, text=_("Copy"), command=about, padx=20)
    glob.button_copy.pack(side=LEFT, pady=10, padx=10)

    glob.button_del = Button(glob.buttonframe, text=_("Delete"), command=about, padx=20)
    glob.button_del.pack(side=LEFT, pady=10, padx=10)

    # text or icon for language
    if os.path.isfile("icon-nl.png"):
        imagenl = Image.open("icon-nl.png")
        imagenl = resize(imagenl, 20)
        photonl = ImageTk.PhotoImage(imagenl)
        glob.button_nl = Button(glob.buttonframe, image=photonl, command=lambda: (lf.language_nl(),
                                                                                  rebuild_buttons()), padx=5)
        glob.button_nl.image = photonl
        glob.button_nl.pack(side=RIGHT, pady=10, padx=5)
    else:
        glob.button_nl = Button(glob.buttonframe, text="NL", command=lambda: (lf.language_nl(),
                                                                              rebuild_buttons()), padx=20)
        glob.button_nl.pack(side=RIGHT, pady=10, padx=10)

    if os.path.isfile("icon-en.png"):
        imageen = Image.open("icon-en.png")
        imageen = resize(imageen, 20)
        photoen = ImageTk.PhotoImage(imageen)
        glob.button_en = Button(glob.buttonframe, image=photoen, command=lambda: (lf.language_en(),
                                                                                  rebuild_buttons()), padx=55)
        glob.button_en.image = photoen
        glob.button_en.pack(side=RIGHT, pady=10, padx=5)
    else:
        glob.button_en = Button(glob.buttonframe, text=_("GB"), command=lambda: (lf.language_en(),
                                                                                 rebuild_buttons()), padx=20)
        glob.button_en.pack(side=RIGHT, pady=10, padx=10)


def build_message():
    glob.message_frame = Text(glob.messageframe, height=1)
    glob.message_frame.pack(fill=X, expand=1, padx=5, pady=5)
    glob.message_frame.insert(END, "msg_welcome")


def rebuild_buttons():
    # delete old frames
    glob.filterframe.destroy()
    glob.buttonframe.destroy()
    glob.sqlframe.destroy()
    glob.photoframe.destroy()
    glob.messageframe.destroy()
    # Build new menu, frames and buttons
    build_menu()
    build_frames()
    build_buttons()


def main_window():
    # setup language based on config file
    langsel = ci.get_config_item("language_selected")
    if langsel == "GB":
        lf.language_en()
    else:
        lf.language_nl()

    get_screen_size()
    glob.root = Tk()
    glob.root.title('Pecuniae Collectio')
    glob.root.geometry('%sx%s+%s+%s' % (glob.screen_width_calc, glob.screen_height_calc,
                                        glob.screen_left, glob.screen_top))
    glob.logger_main.debug("Screem metrics  %sx%s" % (GetSystemMetrics(0), GetSystemMetrics(1)))
    glob.logger_main.debug("Window geometry %sx%s+%s+%s." % (glob.screen_width_calc, glob.screen_height_calc,
                                                             glob.screen_left, glob.screen_top))
    glob.root.option_add("*Font", "Segoe 8")

    build_menu()
    build_frames()
    build_buttons()

    glob.root.mainloop()
