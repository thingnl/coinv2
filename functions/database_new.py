#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
import tkinter
import tkinter.filedialog
import sqlite3
from tkinter import messagebox
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


def insert_testdata():
    """ Ask user for name and location for a new database.

    Args:

    Returns:
    """
    # Is a database currently loaded?
    if glob.current_open_db == "":
        messagebox.showerror(title=_("No database"), message=_("No database is loaded. Please open a database first."))
        return

    # td.insert_table_country(conn)
    # td.insert_table_headofstate(conn)
    # td.insert_table_quality(conn)
    # td.insert_table_suppliers(conn)
    # td.insert_table_orders(conn)
    # td.insert_table_mintmaster(conn)
    # td.insert_table_mint(conn)
    # td.insert_table_valuta(conn)
    # td.insert_table_strike(conn)
    # td.insert_table_coin(conn)
    # td.insert_table_replace(conn)
    # td.insert_table_rarity(conn)
    pass


def open_db():
    """ Ask user to selct a database and load it's contents.

    Args:

    Returns:
    """
    if glob.current_open_db != "":
        messagebox.showerror(title=_("Database loaded"), message=_("A database is currently loaded. Please close the "
                                                                   "current database first before opening a new "
                                                                   "database."))
        glob.logger_main.info("A database is already open, exiting.")
        return

    glob.logger_main.info("Starting Open database function.")
    file_list = [("Databases", ".db"), ("All files", ".*")]
    glob.current_open_db = tkinter.filedialog.askopenfilename(title="Select database to open...", filetypes=file_list,
                                                      defaultextension=".db",
                                                      initialdir=ci.get_config_item("loc_database"))
    if glob.current_open_db == "":
        return

    # Create connection
    conn = None
    try:
        conn = sqlite3.connect(glob.current_open_db)
    except Error as e:
        print(e)

    # try getting the db version
    sql_command = """SELECT * FROM schema"""
    cur = conn.cursor()
    cur.execute(sql_command)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    print(glob.current_open_db)
    print(conn)

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
        lf.send_message(_("Creating new database: " + new_dbfile + "."))
        glob.logger_sql.info("Creating new database: " + new_dbfile)

        conn = None
        try:
            conn = sqlite3.connect(new_dbfile)
            glob.logger_sql.debug("sqlite version: " + sqlite3.version)
        except Exception as e:
            glob.logger_sql.exception("Error creating " + new_dbfile + " database")
            glob.logger_sql.exception(e)
            lf.send_message(_("Error creating " + new_dbfile + " database"))
            return

        lf.send_message(_("Creating new database: " + new_dbfile + " (5%)"))
        tables.create_table_schema(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (11%)"))
        tables.create_table_country(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (18%)"))
        tables.create_table_headofstate(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (26%)"))
        tables.create_table_quality(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (37%)"))
        tables.create_table_valuations(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (51%)"))
        tables.create_table_suppliers(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (63%)"))
        tables.create_table_orders(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (69%)"))
        tables.create_table_mintmaster(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (76%)"))
        tables.create_table_mint(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (82%)"))
        tables.create_table_valuta(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (87%)"))
        tables.create_table_strike(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (92%)"))
        tables.create_table_coin(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (95%)"))
        tables.create_table_replace(conn)
        time.sleep(1)

        lf.send_message(_("Creating new database: " + new_dbfile + " (98%)"))
        tables.create_table_rarity(conn)
        time.sleep(1)

        conn.close()
        time.sleep(1)
        lf.send_message(_("Database " + new_dbfile + " created."))
    else:
        glob.logger_main.info("New database function closed.")
        glob.logger_sql.info("New database function closed.")
