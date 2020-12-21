#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs

# Own modules
from . import glob

# i18n
global _


def bdown(event):
    global col_from, dx, col_from_id
    tv = event.widget
    if tv.identify_region(event.x, event.y) != 'separator':
        col = tv.identify_column(event.x)
        col_from_id = tv.column(col, 'id')
        col_from = int(col[1:]) - 1  # subtract 1 because display columns array 0 = tree column 1
        # get column x coordinate and width
        bbox = tv.bbox(tv.get_children("")[0], col_from_id)
        dx = bbox[0] - event.x  # distance between cursor and column left border
        tv.heading(col_from_id, text='')
        visual_drag.configure(displaycolumns=[col_from_id])
        visual_drag.place(in_=tv, x=bbox[0], y=0, anchor='nw', width=bbox[2], relheight=1)
    else:
        col_from = None


def bup(event):
    tv = event.widget
    col_to = int(tv.identify_column(event.x)[1:]) - 1  # subtract 1 because display columns array 0 = tree column 1
    visual_drag.place_forget()
    if col_from is not None:
        tv.heading(col_from_id, text=visual_drag.heading('#1', 'text'))
        if col_from != col_to:
            dcols = list(tv["displaycolumns"])
            if dcols[0] == "#all":
                dcols = list(tv["columns"])

            if col_from > col_to:
                dcols.insert(col_to, dcols[col_from])
                dcols.pop(col_from + 1)
            else:
                dcols.insert(col_to + 1, dcols[col_from])
                dcols.pop(col_from)
            tv.config(displaycolumns=dcols)


def bmotion(event):
    # drag around label if visible
    if visual_drag.winfo_ismapped():
        visual_drag.place_configure(x=dx + event.x)


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
