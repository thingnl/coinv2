#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
from tkinter import ttk
from tkinter import *
from . import glob
from . import column_functions as cl
# from . import config_window as cw


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
    sql_command = """SELECT * FROM coin"""
    try:
        cur.execute(sql_command)
        glob.coin_data = cur.fetchall()
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    glob.style = ttk.Style()
    glob.style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
    glob.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                         font=('Courier New', 8))  # Modify the font of the body

    # glob.sqlframe
    glob.sql_frame = ttk.Treeview(glob.sqlframe, style="mystyle.Treeview")
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

    # Combine all tuple columns into lines
    elements = list(zip(*glob.coin_data))
    # next, get longest value like len(max(elements[1], key=len)
    # Take longest value from field or header length like max(len(max(elements[2], key=len)) * 9, len("Index") * 8)

    # Set width for all columns so data fits and/or header shows, while hiding the first 2 index fields.
    glob.sql_frame.column("#0", width=0, minwidth=0, stretch=NO)
    glob.sql_frame.column("#1", width=0, minwidth=0, stretch=NO)

    if len(glob.coin_data) != 0:
        glob.sql_frame.column("#2", width=max(len(max(elements[1], key=len)) * 9, len("Private index") * 6), stretch=NO)
        glob.sql_frame.column("#3", width=max(len(max(elements[2], key=len)) * 9, len("Index") * 8), stretch=NO)
        glob.sql_frame.column("#4", width=max(len(max(elements[3], key=len)) * 9, len("Krause") * 6), stretch=NO)
        glob.sql_frame.column("#5", width=max(len(max(elements[4], key=len)) * 9, len("Denomination") * 7), stretch=NO,
                              anchor=E)
        glob.sql_frame.column("#6", width=max(len(max(elements[5], key=len)) * 9, len("Valuta") * 6), stretch=NO)
        glob.sql_frame.column("#7", width=max(len(max(elements[6], key=len)) * 9, len("Country") * 6), stretch=NO)
        glob.sql_frame.column("#8", width=max(len(max(elements[7], key=len)) * 9, len("Year") * 6), stretch=NO)
        glob.sql_frame.column("#9", width=max(len(max(elements[8], key=len)) * 9, len("Mmt") * 6), stretch=NO)
        glob.sql_frame.column("#10", width=max(len(max(elements[9], key=len)) * 9, len("Quality") * 7), stretch=NO)
        glob.sql_frame.column("#11", width=max(len(max(elements[10], key=len)) * 9, len("Remark") * 6), stretch=NO)
        glob.sql_frame.column("#12", width=max(len(max(elements[11], key=len)) * 9, len("Coinage") * 6), stretch=NO,
                              anchor=E)
        glob.sql_frame.column("#13", width=max(len(max(elements[12], key=len)) * 9, len("Diameter") * 7), stretch=NO)
        glob.sql_frame.column("#14", width=max(len(max(elements[13], key=len)) * 8, len("Edge") * 6), stretch=NO)
        glob.sql_frame.column("#15", width=max(len(max(elements[14], key=len)) * 8, len("Edge text") * 7), stretch=NO)
        glob.sql_frame.column("#16", width=max(len(max(elements[15], key=len)) * 9, len("Strike type") * 6), stretch=NO)
        glob.sql_frame.column("#17", width=max(len(max(elements[16], key=len)) * 9, len("Weight") * 6), stretch=NO)
        glob.sql_frame.column("#18", width=max(len(max(elements[17], key=len)) * 9, len("Designer") * 7), stretch=NO)
        glob.sql_frame.column("#19", width=max(len(max(elements[18], key=len)) * 7, len("Front side") * 6), stretch=NO)
        glob.sql_frame.column("#20", width=max(len(max(elements[19], key=len)) * 7, len("Rear side") * 6), stretch=NO)
        glob.sql_frame.column("#21", width=max(len(max(elements[20], key=len)) * 7, len("Material") * 6), stretch=NO)
        glob.sql_frame.column("#22", width=max(len(max(elements[21], key=len)) * 9, len("Rarity") * 7), stretch=NO)
        glob.sql_frame.column("#23", width=max(len(max(elements[22], key=len)) * 7, len("Front jpg") * 7), stretch=NO)
        glob.sql_frame.column("#24", width=max(len(max(elements[23], key=len)) * 7, len("Rear jpg") * 7), stretch=NO)
        glob.sql_frame.column("#25", width=max(len(max(elements[24], key=len)) * 9, len("Serie") * 6), stretch=NO)
        glob.sql_frame.column("#26", width=max(len(max(elements[25], key=len)) * 9, len("Storage") * 7), stretch=NO)
        glob.sql_frame.column("#27", width=max(len(max(elements[26], key=len)) * 9, len("Have") * 9), stretch=NO)
        glob.sql_frame.column("#28", width=max(len(max(elements[27], key=len)) * 9, len("Want") * 9), stretch=NO)
        glob.sql_frame.column("#29", width=max(len(max(elements[28], key=len)) * 9, len("Ordered") * 8), stretch=NO)
        glob.sql_frame.column("#30", width=max(len(max(elements[29], key=len)) * 9, len("For sale") * 7), stretch=NO)
        glob.sql_frame.column("#31", width=max(len(max(elements[30], key=len)) * 9, len("Other") * 7), stretch=NO)
        glob.sql_frame.column("#32", width=max(len(max(elements[31], key=len)) * 9, len("Supplier") * 7), stretch=NO)
        glob.sql_frame.column("#33", width=max(len(max(elements[32], key=len)) * 9, len("Order no") * 7), stretch=NO)
        glob.sql_frame.column("#34", width=max(len(max(elements[33], key=len)) * 9, len("Price") * 9), stretch=NO,
                              anchor=E)
        glob.sql_frame.column("#35", width=max(len(max(elements[34], key=len)) * 9, len("Mint") * 9), stretch=NO)
        glob.sql_frame.column("#36", width=max(len(max(elements[35], key=len)) * 9, len("Mintmaster") * 7), stretch=NO)
        glob.sql_frame.column("#37", width=max(len(max(elements[36], key=len)) * 9, len("Ruler") * 7), stretch=NO)

    # Set headings and register sort command
    glob.sql_frame.heading("#0", text="Id", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                           "#0", False))
    glob.sql_frame.heading("#1", text="SQL RecNo", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                  "#1", False))
    glob.sql_frame.heading("#2", text="Private index", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                      "#2", False))
    glob.sql_frame.heading("#3", text="Index", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                              "#3", False))
    glob.sql_frame.heading("#4", text="Krause", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                               "#4", False))
    glob.sql_frame.heading("#5", text="Denomination", anchor=E, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                     "#5", False))
    glob.sql_frame.heading("#6", text="Valuta", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                               "#6", False))
    glob.sql_frame.heading("#7", text="Country", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                "#7", False))
    glob.sql_frame.heading("#8", text="Year", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                             "#8", False))
    glob.sql_frame.heading("#9", text="Mmt", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                            "#9", False))
    glob.sql_frame.heading("#10", text="Quality", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                 "#10", False))
    glob.sql_frame.heading("#11", text="Remark", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                "#11", False))
    glob.sql_frame.heading("#12", text="Coinage", anchor=E, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                 "#12", False))
    glob.sql_frame.heading("#13", text="Diameter", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                  "#13", False))
    glob.sql_frame.heading("#14", text="Edge", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                              "#14", False))
    glob.sql_frame.heading("#15", text="Edge text", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                   "#15", False))
    glob.sql_frame.heading("#16", text="Strike type", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                     "#16", False))
    glob.sql_frame.heading("#17", text="Weight", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                "#17", False))
    glob.sql_frame.heading("#18", text="Designer", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                  "#18", False))
    glob.sql_frame.heading("#19", text="Front side", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                    "#19", False))
    glob.sql_frame.heading("#20", text="Rear side", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                   "#20", False))
    glob.sql_frame.heading("#21", text="Material", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                  "#21", False))
    glob.sql_frame.heading("#22", text="Rarity", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                "#22", False))
    glob.sql_frame.heading("#23", text="Front jpg link", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                        "#23", False))
    glob.sql_frame.heading("#24", text="Rear jpg link", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                       "#24", False))
    glob.sql_frame.heading("#25", text="Serie", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                               "#25", False))
    glob.sql_frame.heading("#26", text="Storage", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                 "#26", False))
    glob.sql_frame.heading("#27", text="Have", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                              "#27", False))
    glob.sql_frame.heading("#28", text="Want", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                              "#28", False))
    glob.sql_frame.heading("#29", text="Ordered", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                 "#29", False))
    glob.sql_frame.heading("#30", text="For sale", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                  "#30", False))
    glob.sql_frame.heading("#31", text="Other", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                               "#31", False))
    glob.sql_frame.heading("#32", text="Supplier", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                  "#32", False))
    glob.sql_frame.heading("#33", text="Order no", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                  "#33", False))
    glob.sql_frame.heading("#34", text="Price", anchor=E, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                               "#34", False))
    glob.sql_frame.heading("#35", text="Mint", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                              "#35", False))
    glob.sql_frame.heading("#36", text="Mintmaster", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                                    "#36", False))
    glob.sql_frame.heading("#37", text="Ruler", anchor=W, command=lambda: treeview_sort_column(glob.sql_frame,
                                                                                               "#37", False))

    for teller in range(0, len(glob.coin_data)):
        glob.sql_frame.insert(parent='', index='end', iid=teller, text="text", values=glob.coin_data[teller])

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

    glob.sql_frame.pack(fill=BOTH, expand=1)

    # Hide column we don't want to see
    cl.apply_column_hide()

    glob.sql_frame.update()
