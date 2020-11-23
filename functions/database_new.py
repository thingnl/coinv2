#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
import tkinter
import tkinter.filedialog
import sqlite3
from . import config_items as ci
from . import tables_v001 as tables
from . import language_functions as lf
from . import testdata_v001 as td

import time

from . import glob

global _


def check_database_empty(conn):
    """ Ask user for name and location for a new database.

        Args:

        Returns:
        """

    pass


def insert_testdate():
    """ Ask user for name and location for a new database.

    Args:

    Returns:
    """

    pass






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
        lf.send_message(_(" " + new_dbfile + "."))
        glob.logger_sql.info("Creating new database: " + new_dbfile)

        conn = None
        try:
            conn = sqlite3.connect(new_dbfile)
            glob.logger_sql.debug("sqlite version: " + sqlite3.version)
        except Exception as e:
            glob.logger_sql.exception("Error creating " + new_dbfile + " database")
            glob.logger_sql.exception(e)

        tables.create_table_schema(conn)

        tables.create_table_country(conn)
        td.insert_table_country(conn)

        tables.create_table_headofstate(conn)
        td.insert_table_headofstate(conn)

        tables.create_table_quality(conn)
        td.insert_table_quality(conn)

        tables.create_table_valuations(conn)

        tables.create_table_suppliers(conn)
        td.insert_table_suppliers(conn)

        tables.create_table_orders(conn)
        td.insert_table_orders(conn)

        tables.create_table_mintmaster(conn)
        td.insert_table_mintmaster(conn)

        tables.create_table_mint(conn)
        td.insert_table_mint(conn)

        tables.create_table_valuta(conn)
        td.insert_table_valuta(conn)

        tables.create_table_strike(conn)
        td.insert_table_strike(conn)

        tables.create_table_coin(conn)
        td.insert_table_coin(conn)

        tables.create_table_replace(conn)
        td.insert_table_replace(conn)

        tables.create_table_rarity(conn)
        td.insert_table_rarity(conn)

        conn.close()
        lf.send_message(_("Database " + new_dbfile + " created."))
    else:
        glob.logger_main.info("New database function closed.")
        glob.logger_sql.info("New database function closed.")
