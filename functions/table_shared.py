#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs

# Own modules
from . import glob

# i18n
global _


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
