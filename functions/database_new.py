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
    print(conn)
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
    # Is there already a open database?
    if glob.current_open_db != "":
        messagebox.showerror(title=_("Database loaded"), message=_("A database is currently loaded. Please close the "
                                                                   "current database first before opening a new "
                                                                   "database."))
        glob.logger_main.info("A database is already open, exiting.")
        return

    glob.logger_main.info("Starting Open database function.")
    file_list = [("Databases", ".db"), ("All files", ".*")]
    # No open database... What file would you like me to open?
    glob.current_open_db = tkinter.filedialog.askopenfilename(title=_("Select database to open..."),
                                                              filetypes=file_list,
                                                              defaultextension=".db",
                                                              initialdir=ci.get_config_item("loc_database"))
    if glob.current_open_db == "":
        glob.logger_main.info("Nothing selected, exiting.")
        return

    # try to create a connection
    conn = None
    try:
        conn = sqlite3.connect(glob.current_open_db)
    except Exception as e:
        messagebox.showerror(title=_("Database error"), message=_("A connection to the selected database could not be"
                                                                  " made. Please make sure the selected file is a "
                                                                  "valid database."))
        glob.logger_main.info("Database could not be connected, exiting.")
        print(e)

    # try getting the db version
    sql_command = """SELECT * FROM schema"""
    cur = conn.cursor()
    try:
        cur.execute(sql_command)
        row = cur.fetchone()
    except Exception as e:
        messagebox.showerror(title=_("Database error"), message=_("An error happened while trying to read the "
                                                                  "database. Please make sure the selected file "
                                                                  "is a database and is undamaged."))
        glob.logger_main.info("Database could not be read, exiting.")
        glob.logger_sql.info("Database could not be read, exiting.")
        glob.logger_sql.debug(e)
        print(e)
        return

    # So by now we have a working database and got the version of the schema. Let's check it...
    glob.logger_sql.debug("Schema version found: " + row[1] + ", system is on " + glob.system_sql)
    if row[1] != glob.system_sql:
        messagebox.showerror(title=_("Database error"), message=_("This database version (" + row[1] + ") is for a "
                                                                  "different version of Pecuniae Collectio and can "
                                                                  "not be used."))
        glob.logger_main.info("Wrong schema version found, exiting")

    # And we have a correct version of the database schema. What's next.... ah, load the data....
    sql_command = """SELECT * FROM coin"""
    try:
        cur.execute(sql_command)
        glob.coin_data = cur.fetchall()
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    for row in glob.coin_data:
        print(row)

    sql_command = """SELECT description FROM country ORDER by description"""
    try:
        cur.execute(sql_command)
        glob.country_data = ['*']
        for row in cur.fetchall():
            glob.country_data.append(row[0])
    except Exception as e:
        glob.logger_sql.debug(e)
        print(e)

    # Try sening the countries to the correct filter
    # while adding a * for all
    for line in glob.country_data:
        print(line)

    lf.send_message(_("Loading of database " + glob.current_open_db + " finished. " + str(len(glob.coin_data)) + " coins loaded."))

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
