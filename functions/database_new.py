#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
import tkinter
import tkinter.filedialog
import sqlite3
from sqlite3 import Error
from . import config_items as ci
from . import tables_v001 as tables
from . import language_functions as lf

from . import glob


def create_newdb():
    """ Ask user for name and location for a new database.

    Args:

    Returns:
    """
    glob.logger_main.info("Starting New database function.")
    glob.logger_sql.info("Starting New database function.")
    file_list = [("Databases", ".db"), ("All files", ".*")]
    new_dbfile = tkinter.filedialog.asksaveasfilename(title="Create new database...", filetypes=file_list,
                                                      defaultextension=".db",
                                                      initialdir=ci.get_config_item("loc_database"))
    if new_dbfile != "":
        glob.logger_sql.info("Creating new database: " + new_dbfile)

        conn = None
        try:
            conn = sqlite3.connect(new_dbfile)
            glob.logger_sql.debug("sqlite version: " + sqlite3.version)
        except Error as e:
            glob.logger_sql.exception("Error creating " + new_dbfile + " database")

        tables.create_table_schema(conn)
        tables.create_table_country(conn)
        tables.create_table_headofstate(conn)
        tables.create_table_quality(conn)
        tables.create_table_valuations(conn)
        tables.create_table_suppliers(conn)
        tables.create_table_orders(conn)
        tables.create_table_mintmaster(conn)
        tables.create_table_mint(conn)
        tables.create_table_valuta(conn)
        tables.create_table_strike(conn)
        tables.create_table_coin(conn)
        tables.create_table_replace(conn)
        tables.create_table_rarity(conn)













    else:
        glob.logger_main.info("New database function closed.")
        glob.logger_sql.info("New database function closed.")







    conn.close()

    lf.send_message(_("Database " + new_dbfile + " created."))