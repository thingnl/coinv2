#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
from tkinter import ttk
from tkinter import *
from . import glob
from . import column_functions as cl
from . import table_shared as ts
# from . import config_window as cw


def load_filter_country():
    sql_command = """SELECT description FROM country ORDER by description"""
    try:
        glob.cur.execute(sql_command)
        glob.country_data = ['*']
        for row in glob.cur.fetchall():
            glob.country_data.append(row[0])
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    # Sending the countries to the correct filter
    glob.combo_country['values'] = glob.country_data
    glob.combo_country.current(0)


def load_coin_tree():
    sql_command = """SELECT * FROM coin"""
    try:
        glob.cur.execute(sql_command)
        glob.coin_data = glob.cur.fetchall()
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    # format price data with 2 decimals by replaceing tuple value
    if len(glob.coin_data) != 0:
        for i in range(0, len(glob.coin_data)):
            if glob.coin_data[i][33] != "":                 # We do need a price there.... not an empty field
                templist = list(glob.coin_data[i])
                templist[33] = f'{glob.coin_data[i][33]:.2f}'
                glob.coin_data[i] = templist

    glob.style = ttk.Style()
    glob.style.map("Custom.Treeview", foreground=ts.fixed_map('foreground'), background=ts.fixed_map('background'))
    glob.style.element_create("Custom.Treeheading.border", "from", "default")
    glob.style.layout("Custom.Treeview.Heading", [
        ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
        ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                ("Custom.Treeheading.text", {'sticky': 'we'})
            ]})
        ]}),
    ])
    glob.style.configure("Custom.Treeview.Heading", background="blue", foreground="white", relief="flat")
    glob.style.map("Custom.Treeview.Heading", relief=[('active', 'groove'), ('pressed', 'sunken')])

    glob.sql_frame = ttk.Treeview(glob.sqlframe, style="Custom.Treeview")
    glob.sql_frame['columns'] = ("SQL RecNo", "Private index", "Index", "Krause", "denomination", "valuta",
                                 "country", "year", "mmt", "quality", "remark", "coinage", "diameter",
                                 "edge", "edgetext", "striketype", "weight", "designer", "frontside",
                                 "rearside", "material", "rarity", "frontjpglink", "rearjpglink", "serie",
                                 "storage", "ynhave", "ynwant", "ynordered", "ynforsale", "ynother",
                                 "supplier", "orderno", "purchaseprice", "mint", "mintmaster",
                                 "headofstate")

    # Set colors for odd and even rows
    glob.sql_frame.tag_configure('odd', background='#FFFFFF')  # light blue #FFFFFF
    glob.sql_frame.tag_configure('even', background='#E2FFFF')  # white #E2FFFF

    # Set width for all columns so data fits and/or header shows, while hiding the first 2 index fields.
    glob.sql_frame.column("#0", width=0, minwidth=0, stretch=NO)
    glob.sql_frame.column("#1", width=0, minwidth=0, stretch=NO)

    # Set headings and register sort command
    glob.sql_frame.heading("#0", text="Id", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#0", False))
    glob.sql_frame.heading("#1", text="SQL RecNo", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#1", False))
    glob.sql_frame.heading("#2", text="Private index", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#2", False))
    glob.sql_frame.heading("#3", text="Index", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#3", False))
    glob.sql_frame.heading("#4", text="Krause", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#4", False))
    glob.sql_frame.heading("#5", text="Denomination", anchor=E,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#5", False))
    glob.sql_frame.heading("#6", text="Valuta", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#6", False))
    glob.sql_frame.heading("#7", text="Country", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#7", False))
    glob.sql_frame.heading("#8", text="Year", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#8", False))
    glob.sql_frame.heading("#9", text="Mmt", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#9", False))
    glob.sql_frame.heading("#10", text="Quality", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#10", False))
    glob.sql_frame.heading("#11", text="Remark", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#11", False))
    glob.sql_frame.heading("#12", text="Coinage", anchor=E,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#12", False))
    glob.sql_frame.heading("#13", text="Diameter", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#13", False))
    glob.sql_frame.heading("#14", text="Edge", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#14", False))
    glob.sql_frame.heading("#15", text="Edge text", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#15", False))
    glob.sql_frame.heading("#16", text="Strike type", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#16", False))
    glob.sql_frame.heading("#17", text="Weight", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#17", False))
    glob.sql_frame.heading("#18", text="Designer", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#18", False))
    glob.sql_frame.heading("#19", text="Front side", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#19", False))
    glob.sql_frame.heading("#20", text="Rear side", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#20", False))
    glob.sql_frame.heading("#21", text="Material", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#21", False))
    glob.sql_frame.heading("#22", text="Rarity", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#22", False))
    glob.sql_frame.heading("#23", text="Front jpg link", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#23", False))
    glob.sql_frame.heading("#24", text="Rear jpg link", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#24", False))
    glob.sql_frame.heading("#25", text="Serie", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#25", False))
    glob.sql_frame.heading("#26", text="Storage", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#26", False))
    glob.sql_frame.heading("#27", text="Have", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#27", False))
    glob.sql_frame.heading("#28", text="Want", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#28", False))
    glob.sql_frame.heading("#29", text="Ordered", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#29", False))
    glob.sql_frame.heading("#30", text="For sale", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#30", False))
    glob.sql_frame.heading("#31", text="Other", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#31", False))
    glob.sql_frame.heading("#32", text="Supplier", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#32", False))
    glob.sql_frame.heading("#33", text="Order no", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#33", False))
    glob.sql_frame.heading("#34", text="Price", anchor=E,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#34", False))
    glob.sql_frame.heading("#35", text="Mint", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#35", False))
    glob.sql_frame.heading("#36", text="Mintmaster", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#36", False))
    glob.sql_frame.heading("#37", text="Ruler", anchor=W,
                           command=lambda: ts.treeview_sort_column(glob.sql_frame, "#37", False))

    # Inster data into tree
    for teller in range(0, len(glob.coin_data)):
        glob.sql_frame.insert(parent='', index='end', iid=teller, text="text", values=glob.coin_data[teller])

    # Set color indicators for all lines when we have data
    if len(glob.coin_data) != 0:
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
    glob.scrollh = ttk.Scrollbar(glob.sqlframe, orient="horizontal", command=glob.sql_frame.xview)
    glob.scrollh.pack(side=BOTTOM, fill='x')
    glob.sql_frame.configure(xscrollcommand=glob.scrollh.set)

    # Inserting vertical scrollbar
    glob.scrollv = ttk.Scrollbar(glob.sqlframe, orient="vertical", command=glob.sql_frame.yview)
    glob.scrollv.pack(side=RIGHT, fill='y')
    glob.sql_frame.configure(yscrollcommand=glob.scrollv.set)

    # Hide column we don't want to see and send with of those we do want to see
    cl.apply_column_hide()

    glob.sql_frame.pack(fill=BOTH, expand=1)

    # glob.sql_frame.update()
