# System libs
import os

from tkinter import *
from tkinter import ttk
from tkinter import Tk

# win32api is part of pywin32
from win32api import GetSystemMetrics


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

    # ------------------------------------------------------------------------------------------------------------------------------------
    # Add menubar to main window
    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(root, tearoff=0)
    menu.add_cascade(label="file", menu=filemenu)
    filemenu.add_command(label="new", command=newfile)
    filemenu.add_command(label="open", command=lambda: opendb())
    filemenu.add_command(label="close", command=newfile)
    filemenu.add_command(label="save", command=newfile)
    filemenu.add_separator()
    filemenu.add_command(label="exit", command=root.quit)

    tablemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="var_menu_tables", menu=tablemenu)
    tablemenu.add_command(label="var_menu_countries", command=about)
    tablemenu.add_command(label="var_menu_suppliers", command=about)
    tablemenu.add_command(label="var_menu_orders", command=about)
    tablemenu.add_command(label="var_menu_rarity", command=about)

    datamenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="var_menu_data", menu=datamenu)
    datamenu.add_command(label="var_menu_export", command=about)
    datamenu.add_command(label="var_menu_import", command=about)

    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="var_menu_help", menu=helpmenu)
    helpmenu.add_command(label="var_menu_manual", command=about)
    helpmenu.add_command(label="var_menu_about", command=about)
    helpmenu.add_command(label="var_menu_support", command=about)

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

    glob.filter_frame = LabelFrame(glob.filterframe, text="var_label_filters", height=650, width=175,
                                   relief=RIDGE, bd=2, bg="gray85")  # bg="gray85"
    glob.filter_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)
    glob.filter_frame.place(anchor=NW)

    glob.button_filter_apply = Button(glob.filterframe, text="var_label_apply", command=root.quit)
    glob.button_filter_apply.place(relx=0.5, rely=0.96, anchor=CENTER)

    glob.filter_label_country = Label(glob.filter_frame, text="var_label_country", bg="gray85")
    glob.filter_label_country.place(anchor=W, bordermode=INSIDE)
    glob.filter_label_country.place(relx=0.02, rely=0.03)

    glob.combo_country = ttk.Combobox(glob.filter_frame)
    glob.combo_country.place(relx=0.10, rely=0.05)

    glob.filter_label_denomination = Label(glob.filter_frame, text="var_label_denomination", bg="gray85")
    glob.filter_label_denomination.place(anchor=W, bordermode=INSIDE)
    glob.filter_label_denomination.place(relx=0.02, rely=0.12)

    glob.combo_denomination = ttk.Combobox(glob.filter_frame)
    glob.combo_denomination.place(relx=0.10, rely=0.14)

    root.mainloop()
