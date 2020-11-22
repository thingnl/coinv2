#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
from . import glob


def insert_table_country(conn):
    """
    Insert test data into country table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """INSERT INTO country (id, description) VALUES(?,?);"""
    sql_tuples = [(1, 'Nederland'), (2, 'Belgie'), (3, 'Duitsland'), (4, 'Frankrijk'), (5, 'Spanje')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 5 records into table country")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_headofstate(conn):
    """
    Insert test data into head of state table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """INSERT INTO headofstate (id, name, headjpg, started, finished, country) VALUES(?,?,?,?,?,?);"""
    sql_tuples = [('1', 'Koning Willem I', ' ', '1815', '1840', 'Nederland'),
                  ('2', 'Koning Willem II', ' ', '1840', '1849', 'Nederland'),
                  ('3', 'Koning Willem III', ' ', '1849', '1890', 'Nederland'),
                  ('4', 'Koningin Wilhelmina', ' ', '1890', '1948', 'Nederland'),
                  ('5', 'Koningin Juliana', ' ', '1948', '1980', 'Nederland'),
                  ('6', 'Koningin Beatrix', ' ', '1980', '2013', 'Nederland'),
                  ('7', 'Koning Willem-Alexander', ' ', '2013', '', 'Nederland')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 7 records into table head of state")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_rarity(conn):
    """
    Insert test data into rarity table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """INSERT INTO rarity (id, rarity, description) VALUES(?,?,?);"""
    sql_tuples = [('1', 'N', '>1001 exemplaren bekend'),
                  ('2', 'S', '251-1000 exemplaren bekend'),
                  ('3', 'R', '76-250 exemplaren bekend'),
                  ('4', 'RR', '16-75 exemplaren bekend'),
                  ('5', 'RRR', '6-15 exemplaren bekend'),
                  ('6', 'RRRR', '2-5 exemplaren bekend'),
                  ('7', 'U', 'Slechts 1 exemplaar bekend')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 7 records into table rarity")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_quality(conn):
    """
    Insert test data into quality table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """INSERT INTO quality (id, quality, description) VALUES(?,?,?);"""
    sql_tuples = [('1', 'G', 'Goed'),
                  ('2', 'ZG', 'Zeer goed'),
                  ('3', 'F', 'Fraai'),
                  ('4', 'ZFr', 'Zeer fraai'),
                  ('5', 'PR', 'Prachtig'),
                  ('6', 'FDC', 'Fleur de Coin'),
                  ('7', 'PL', 'Prooflike'),
                  ('8', 'PROOF', 'Proof')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 8 records into table quality")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_strike(conn):
    """
    Insert test data into strike table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """INSERT INTO strike (id, striketype) VALUES(?,?);"""
    sql_tuples = [('1', 'Muntslag'),
                  ('2', 'Medailleslag'),
                  ('3', 'Misslag'),
                  ('4', 'Overslag')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 4 records into table strike")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_suppliers(conn):
    """
    Insert test data into suppliers table

    Args: conn - sql connection object

    Returns: Nothing
    """
    sql_command = """INSERT INTO suppliers (id, company, contact, street, number, zipcode, city, phone, mobile, email, 
                     web, customerid, country) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    sql_tuples = [('1', 'Theo Peters', '', 'Westerdoksdijk', '605', '1013 BX', 'Amsterdam', '020 622 25 30', '',
                   'info@theopeters.com', 'https://www.theopeters.com/', 'mymail@google.com', 'Nederland'),
                  ('2', 'VerzamelaarsMarkt', 'Kantoor Klaaswaal', 'Industrieweg', '13', '3286 BW', 'Klaaswaal',
                   '', '', '', 'https://www.verzamelaarsmarkt.nl/', 'mymail@google.com', 'Nederland'),
                  ('3', 'Hansmunt.nl', '', '', '', '', '', '0492-849709', '', '', 'https://www.euromuntenonline.nl/',
                   '', 'Nederland')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 3 records into table suppliers")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_orders(conn):
    """
        Insert test data into orders table

        Args: conn - sql connection object

        Returns: Nothing
        """
    sql_command = """INSERT INTO orders (id, orderno, date, pdflink, status, suppliers_id) 
                     VALUES(?,?,?,?,?,?);"""
    sql_tuples = [('1', 'TP-1254', '2017-05-23',
                   'D:\\Dropbox\\Theo Peters - order 1254 2017-5-23.pdf', 'Gesloten', '1'),
                  ('2', 'TP-1367', '2017-08-04',
                   'D:\\Dropbox\\Theo Peters - order 1367 2017-08-04.pdf', 'Gesloten', '1'),
                  ('3', 'VM735432', '2017-08-22', '', 'Open', '2')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 3 records into table orders")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_mintmaster(conn):
    """
            Insert test data into mintmaster table

            Args: conn - sql connection object

            Returns: Nothing
            """
    sql_command = """INSERT INTO mintmaster (id, naam, signtxt, signjpg, started, finished, remark, country)
                     VALUES(?,?,?,?,?,?,?,?);"""
    sql_tuples = [('1', 'E.J. van Schouwenburg', 'Pijl-en-boog met ster', '', '2000', '2000',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('2', 'R. Bruens ING', 'Vruchtdragende wijnrank', '', '2001', '2001', '', 'Nederland'),
                  ('3', 'Ir. M.T. Brouwer', 'Vruchtdragende wijnrank met ster', '', '2002', '2002',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('4', 'Ir. M.T. Brouwer', 'Koerszettende zeilen', '', '2003', '2015', '', 'Nederland'),
                  ('5', 'Ir. K. Bruinsma', 'Koerszettende zeilen met ster', '', '2015', '2016',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('6', 'T. Peters', 'Koerszettende zeilen met ster', '', '2016', '2017',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('7', 'S. Satijn', 'Sint Servaasbrug', '', '2017', '', '', 'Nederland'),
                  ('8', 'E.J. van Schouwenburg', 'Pijl-en-boog met ster', '', '2000', '2000',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('9', 'R. Bruens ING', 'Vruchtdragende wijnrank', '', '2001', '2001', '', 'Nederland'),
                  ('10', 'Ir. M.T. Brouwer', 'Vruchtdragende wijnrank met ster', '', '2002', '2002',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('11', 'Ir. M.T. Brouwer', 'Koerszettende zeilen', '', '2003', '2015', '', 'Nederland'),
                  ('12', 'Ir. K. Bruinsma', 'Koerszettende zeilen met ster', '', '2015', '2016',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('13', 'T. Peters', 'Koerszettende zeilen met ster', '', '2016', '2017',
                   'Waarnemend muntmeester', 'Nederland'),
                  ('14', 'S. Satijn', 'Sint Servaasbrug', '', '2017', '', '', 'Nederland')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 14 records into table mintmaster")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)
