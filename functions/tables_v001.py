#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
from . import glob


def create_table_schema(conn):
    """
    Create schema table and insert version number into schema table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS schema (id integer PRIMARY KEY,	version text NOT NULL);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table schema")
    except Exception as e:
        glob.logger_sql.debug(e)

    sql_command = """INSERT INTO schema (id, version) VALUES(?,?);"""
    sql_data = [1, "v001"]
    c = conn.cursor()
    try:
        c.execute(sql_command, sql_data,)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_country(conn):
    """
    Create country table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS country (id	         INTEGER PRIMARY KEY AUTOINCREMENT,
                                                         description TEXT);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table country")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_headofstate(conn):
    """
    Create head of state table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS headofstate (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                             name            TEXT,
                                                             headjpg         TEXT,
                                                             started         TEXT,
                                                             finished        TEXT,
                                                             country         TEXT);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table headofstate")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_quality(conn):
    """
    Create quality table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS quality (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                         quality         TEXT,
                                                         description     TEXT);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table quality")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_valuations(conn):
    """
    Create valuations table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS valuations (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            coin_id         INTEGER,
                                                            year            INTEGER NOT NULL,
                                                            value           REAL NOT NULL);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table valuations")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_suppliers(conn):
    """
    Create suppliers table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS suppliers (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           company         TEXT CHECK(COALESCE("company", "contact") 
                                                                           IS NOT NULL),
                                                           contact         TEXT,
                                                           street          TEXT,
                                                           number          TEXT,
                                                           zipcode         TEXT,
                                                           city            TEXT,
                                                           phone           TEXT,
                                                           mobile          TEXT,
                                                           email           TEXT,
                                                           web             TEXT,
                                                           customerid      TEXT,
                                                           country_id      REFERENCES country(id));"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table suppliers")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_config(conn):
    pass


def create_table_orders(conn):
    """
    Create orders table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS orders (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        orderno         TEXT,
                                                        date            TEXT,
                                                        pdflink         TEXT,
                                                        status          TEXT,
                                                        suppliers_id    REFERENCES suppliers(id));"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table orders")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_mintmaster(conn):
    """
    Create mintmaster table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS mintmaster (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            naam            TEXT NOT NULL,
                                                            signtxt         TEXT,
                                                            started         TEXT,
                                                            finished        TEXT,
                                                            remark          TEXT,
                                                            country_id      REFERENCES country(id));"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table mintmaster")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_mint(conn):
    """
    Create mint table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS mint (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                      name            TEXT,
                                                      adres	          TEXT,
                                                      zipcode         TEXT,
                                                      city            TEXT,
                                                      weblink         TEXT,
                                                      started         TEXT,
                                                      finished        TEXT,
                                                      country_id      REFERENCES country(id));"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table mint")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_valuta(conn):
    """
    Create valuta table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS valuta (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        valuta          TEXT NOT NULL,
                                                        country_id      REFERENCES country(id));"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table valuta")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_strike(conn):
    """
    Create strike table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS strike (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        striketype      TEXT);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table strike")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_coin(conn):
    """
    Create coin table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS coin (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                      privateindex    TEXT,
                                                      indexid         TEXT,
                                                      krauseid        TEXT,
                                                      denomination    TEXT NOT NULL,
                                                      valuta          TEXT NOT NULL,
                                                      country         TEXT NOT NULL,
                                                      year            TEXT,
                                                      quality         TEXT,
                                                      remark          TEXT,
                                                      coinage         TEXT,
                                                      diameter        TEXT,
                                                      edge            TEXT,
                                                      edgetext        TEXT,
                                                      weight          TEXT,
                                                      designer        TEXT,
                                                      frontside       TEXT,
                                                      rearside        TEXT,
                                                      material        TEXT,
                                                      rarity          TEXT,
                                                      frontjpglink    TEXT,
                                                      rearjpglink     TEXT,
                                                      serie           TEXT,
                                                      storage         TEXT,
                                                      ynhave          INTEGER,
                                                      ynwant          INTEGER,
                                                      ynordered       INTEGER,
                                                      ynforsale       INTEGER,
                                                      ynother         INTEGER,
                                                      supplier        TEXT,
                                                      order           TEXT,
                                                      purchaseprice   REAL,
                                                      mint            TEXT,
                                                      mintmaster      TEXT,
                                                      headofstate     TEXT);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table coin")
    except Exception as e:
        glob.logger_sql.debug(e)


def create_table_replace(conn):
    """
    Create replace table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS replace (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                         searchfor       TEXT,
                                                         replacewith     TEXT);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table replace")
    except Exception as e:
        glob.logger_sql.debug(e)
    pass


def create_table_rarity(conn):
    """
    Create rarity table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """CREATE TABLE IF NOT EXISTS rarity (id              INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        rarity	        TEXT, 
                                                        description 	TEXT);"""
    c = conn.cursor()
    try:
        c.execute(sql_command)
        glob.logger_sql.debug("Created table rarity")
    except Exception as e:
        glob.logger_sql.debug(e)
    pass
