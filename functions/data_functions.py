#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import os
import logging
from tkinter import ttk
from tkinter import *
from . import glob
from . import config_items as ci


def load_filter_country(cur):
    sql_command = """SELECT description FROM country ORDER by description"""
    try:
        cur.execute(sql_command)
        glob.country_data = ['*']
        for row in cur.fetchall():
            glob.country_data.append(row[0])
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    # Sending the countries to the correct filter
    glob.combo_country['values'] = glob.country_data
    glob.combo_country.current(0)


def load_coin_tree(cur):

    # Need this next to column move, sort and coloring:
    # hide:    https://stackoverflow.com/questions/33290969/hiding-treeview-columns-in-tkinter
    # drag:    https://stackoverflow.com/questions/51378611/python-tkinter-table-order-table-columns-with-drag-and-drop
    #

    sql_command = """SELECT * FROM coin"""
    try:
        cur.execute(sql_command)
        glob.coin_data = cur.fetchall()
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    # glob.sqlframe
    glob.sql_frame = ttk.Treeview(glob.sqlframe)
    glob.sql_frame['columns'] = ("SQL RecNo", "Private index", "Index", "Krause", "denomination", "valuta",
                                 "country", "year", "mmt", "quality", "remark", "coinage", "diameter",
                                 "edge", "edgetext", "striketype", "weight", "designer", "frontside",
                                 "rearside", "material", "rarity", "frontjpglink", "rearjpglink", "serie",
                                 "storage", "ynhave", "ynwant", "ynordered", "ynforsale", "ynother",
                                 "supplier", "orderno", "purchaseprice", "mint", "mintmaster",
                                 "headofstate")

    # glob.sql_frame.column("#0", width=0, stretch=NO)  # Hide tree index
    # glob.sql_frame.column("#1", anchor=W)
    # glob.sql_frame.column("#2", anchor=W)
    # glob.sql_frame.column("#3", anchor=W)
    # glob.sql_frame.column("#4", anchor=W)
    # glob.sql_frame.column("#5", anchor=W)
    # glob.sql_frame.column("#6", anchor=W)
    # glob.sql_frame.column("#7", anchor=W)
    # glob.sql_frame.column("#8", anchor=W)
    # glob.sql_frame.column("#9", anchor=W)

    # glob.sql_frame.column("#2", width=len(max(glob.coin_data, key=lambda t: len(t[0]))[3]), stretch=NO)

    elements = list(zip(*glob.coin_data))  # Combine all tuple columns into lines
                                           # next, get longest value and compare to 20
                                           # Take longest value as width
    glob.sql_frame.column("#0", width=0, minwidth=0, stretch=NO)
    glob.sql_frame.column("#1", width=0, minwidth=0, stretch=NO)
    glob.sql_frame.column("#2", width=max(len(max(elements[1], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#3", width=max(len(max(elements[2], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#4", width=max(len(max(elements[3], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#5", width=max(len(max(elements[4], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#6", width=max(len(max(elements[5], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#7", width=max(len(max(elements[6], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#8", width=max(len(max(elements[7], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#9", width=max(len(max(elements[8], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#10", width=max(len(max(elements[9], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#11", width=max(len(max(elements[10], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#12", width=max(len(max(elements[11], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#13", width=max(len(max(elements[12], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#14", width=max(len(max(elements[13], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#15", width=max(len(max(elements[14], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#16", width=max(len(max(elements[15], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#17", width=max(len(max(elements[16], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#18", width=max(len(max(elements[17], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#19", width=max(len(max(elements[18], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#20", width=max(len(max(elements[19], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#21", width=max(len(max(elements[20], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#22", width=max(len(max(elements[21], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#23", width=max(len(max(elements[22], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#24", width=max(len(max(elements[23], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#25", width=max(len(max(elements[24], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#26", width=max(len(max(elements[25], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#27", width=max(len(max(elements[26], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#28", width=max(len(max(elements[27], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#29", width=max(len(max(elements[28], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#30", width=max(len(max(elements[29], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#31", width=max(len(max(elements[30], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#32", width=max(len(max(elements[31], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#33", width=max(len(max(elements[32], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#34", width=max(len(max(elements[33], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#35", width=max(len(max(elements[34], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#36", width=max(len(max(elements[35], key=len)) * 9, 20), stretch=NO)
    glob.sql_frame.column("#37", width=max(len(max(elements[36], key=len)) * 9, 20), stretch=NO)

    glob.sql_frame.heading("#0", text="Id", anchor=W)
    glob.sql_frame.heading("#1", text="SQL RecNo", anchor=W)
    glob.sql_frame.heading("#2", text="Private index", anchor=W)
    glob.sql_frame.heading("#3", text="Index", anchor=W)
    glob.sql_frame.heading("#4", text="Krause", anchor=W)
    glob.sql_frame.heading("#5", text="denomination", anchor=W)
    glob.sql_frame.heading("#6", text="valuta", anchor=W)
    glob.sql_frame.heading("#7", text="country", anchor=W)
    glob.sql_frame.heading("#8", text="year", anchor=W)
    glob.sql_frame.heading("#9", text="mmt", anchor=W)
    glob.sql_frame.heading("#10", text="quality", anchor=W)
    glob.sql_frame.heading("#11", text="remark", anchor=W)
    glob.sql_frame.heading("#12", text="coinage", anchor=W)
    glob.sql_frame.heading("#13", text="diameter", anchor=W)
    glob.sql_frame.heading("#14", text="edge", anchor=W)
    glob.sql_frame.heading("#15", text="edgetext", anchor=W)
    glob.sql_frame.heading("#16", text="striketype", anchor=W)
    glob.sql_frame.heading("#17", text="weight", anchor=W)
    glob.sql_frame.heading("#18", text="designer", anchor=W)
    glob.sql_frame.heading("#19", text="frontside", anchor=W)
    glob.sql_frame.heading("#20", text="rearside", anchor=W)
    glob.sql_frame.heading("#21", text="material", anchor=W)
    glob.sql_frame.heading("#22", text="rarity", anchor=W)
    glob.sql_frame.heading("#23", text="frontjpglink", anchor=W)
    glob.sql_frame.heading("#24", text="rearjpglink", anchor=W)
    glob.sql_frame.heading("#25", text="serie", anchor=W)
    glob.sql_frame.heading("#26", text="storage", anchor=W)
    glob.sql_frame.heading("#27", text="ynhave", anchor=W)
    glob.sql_frame.heading("#28", text="ynwant", anchor=W)
    glob.sql_frame.heading("#29", text="ynordered", anchor=W)
    glob.sql_frame.heading("#30", text="ynforsale", anchor=W)
    glob.sql_frame.heading("#31", text="ynother", anchor=W)
    glob.sql_frame.heading("#32", text="supplier", anchor=W)
    glob.sql_frame.heading("#33", text="orderno", anchor=W)
    glob.sql_frame.heading("#34", text="purchaseprice", anchor=W)
    glob.sql_frame.heading("#35", text="mint", anchor=W)
    glob.sql_frame.heading("#36", text="mintmaster", anchor=W)
    glob.sql_frame.heading("#37", text="headofstate", anchor=W)












    # for teller in range(0,len(glob.treeheaders)):
    #    glob.sql_frame.heading(glob.treeheaders[teller][0], text=glob.treeheaders[teller][1], anchor=W)

    for teller in range(0, len(glob.coin_data)):
        glob.sql_frame.insert(parent='', index='end', iid=teller, text="text", values=glob.coin_data[teller])

    glob.sql_frame.pack(fill=BOTH, expand=1)

    glob.sql_frame.update()

    # # Inserting horizontal scrollbar
    # scrollh = ttk.Scrollbar(glob.sqlframe, orient="horizontal", command=mem.coinlist.xview)
    # scrollh.pack(side=BOTTOM, fill='x')
    # mem.coinlist.configure(xscrollcommand=scrollh.set)
    #
    # # Inserting vertical scrollbar
    # scrollv = ttk.Scrollbar(glob.sqlframe, orient="vertical", command=mem.coinlist.yview)
    # scrollv.pack(side=RIGHT, fill='y')
    # mem.coinlist.configure(yscrollcommand=scrollv.set)