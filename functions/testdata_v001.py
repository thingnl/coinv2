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


def insert_table_mint(conn):
    """
        Insert test data into mint table

        Args: conn - sql connection object

        Returns: Nothing
        """
    sql_command = """INSERT INTO mint (id, name, adres, zipcode, city, weblink, started, finished, country)
                     VALUES(?,?,?,?,?,?,?,?,?);"""
    sql_tuples = [('1', 'Koninklijke Nederlandse Munt', 'Linker Hoon 2', '3991 CX', 'Houten',
                   'https://www.knm.nl/', '1567', '', 'Nederland'),
                  ('2', 'Koninklijke Munt van België', '', '', '',
                   'https://finance.belgium.be/en/royal-mint-of-belgium', '', '', 'Belgie')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 2 records into table mint")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_valuta(conn):
    """
        Insert test data into valuta table

        Args: conn - sql connection object

        Returns: Nothing
        """
    sql_command = """INSERT INTO valuta (id, valuta, country) VALUES(?,?,?);"""
    sql_tuples = [('1', 'cent', 'Nederland'),
                  ('2', 'gulden', 'Nederland'),
                  ('3', 'eurocent', 'Nederland'),
                  ('4', 'euro', 'Nederland'),
                  ('5', 'dukaat', 'Nederland'),
                  ('6', 'dubbele dukaat', 'Nederland'),
                  ('7', 'rijder', 'Nederland'),
                  ('8', 'daalder', 'Nederland'),
                  ('9', 'mark', 'Duitsland'),
                  ('10', 'groschen', 'Duitsland'),
                  ('11', 'pfennig', 'Duitsland'),
                  ('12', 'franc', 'Frankrijk'),
                  ('13', 'centimes', 'Frankrijk'),
                  ('14', 'sous', 'Frankrijk')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 14 records into table valuta")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


def insert_table_replace(conn):
    """
        Insert test data into replace table

        Args: conn - sql connection object

        Returns: Nothing
        """
    sql_command = """INSERT INTO replace (id, searchfor, replacewith)
                     VALUES(?,?,?);"""
    sql_tuples = [('1', '1/2', '½'),
                  ('2', '.5', '½'),
                  ('3', '1/4', '¼'),
                  ('4', '"a', 'ä'),
                  ('5', '"e', 'ë'),
                  ('6', '/o', 'ø')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 6 records into table replace")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)


# Table for edge?
# muntmeesterteken (mmt)

def insert_table_coin(conn):
    """
        Insert test data into coin table

        Args: conn - sql connection object

        Returns: Nothing
    """
    sql_command = """INSERT INTO coin (id, privateindex, indexid, krauseid, denomination, valuta, country, year, mmt,
                                       quality, remark, coinage, diameter, edge, edgetext, striketype, weight, designer,
                                       frontside, rearside, material, rarity, frontjpglink, rearjpglink, serie, storage, 
                                       ynhave, ynwant, ynordered, ynforsale, ynother, supplier, orderno, purchaseprice, 
                                       mint, mintmaster, headofstate) 
                      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    sql_tuples = [('1', '3500', '', 'KM# 213', '1', 'dukaat', 'Nederland', '1989', 'Pijl en boog', 'PROOF', '', '35747',
                   '40 mm', 'Kabelrand', '', 'Medailleslag', '28.25 g', '',
                   'Ridder met zwaard staande op ondergrond met in de linkerhand een lint waaraan het provincie '
                   'wapen van Utrecht',
                   'Gekroond Nederlands wapen tussen jaartal', 'zilver 873/1000', 'N', '', '', '', 'map 3', 'Y', 'N',
                   'N', 'N', 'N', 'Theo Peters', '', '', 'KNM', '', 'Koningin Beatrix'),
                  ('2', '3505', '', 'KM# 213', '1', 'dukaat', 'Nederland', '1992', 'Pijl en boog', 'PROOF', '', '10900',
                   '40 mm', 'Kabelrand', '', 'Medailleslag', '28.25 g', '',
                   'Ridder met zwaard staande op ondergrond met in de linkerhand een lint waaraan het provincie '
                   'wapen van Utrecht',
                   'Gekroond Nederlands wapen tussen jaartal', 'zilver 873/1000', 'N', '', '', '', 'map 3', 'Y', 'N',
                   'N', 'N', 'N', 'Theo Peters', '', '', 'KNM', '', 'Koningin Beatrix'),
                  ('3', '3510', '', 'KM# 213', '1', 'dukaat', 'Nederland', '1993', 'Pijl en boog', 'PROOF', '', '12500',
                   '40 mm', 'Kabelrand', '', 'Medailleslag', '28.25 g', '',
                   'Ridder met zwaard staande op ondergrond met in de linkerhand een lint waaraan het provincie wapen'
                   ' van Utrecht',
                   'Gekroond Nederlands wapen tussen jaartal', 'zilver 873/1000', 'N', '', '', '', 'map 3', 'Y', 'Y',
                   'N', 'N', 'N', 'Theo Peters', '', '', 'KNM', '', 'Koningin Beatrix'),
                  ('4', '3515', '', 'KM# 218', '1', 'dukaat', 'Nederland', '1994', 'Pijl en boog', 'PROOF', 'Groningen',
                   '11000', '40 mm', 'Kabelrand', '', 'Medailleslag', '28.25 g', '',
                   'Ridder met zwaard staande op ondergrond met in de linkerhand een lint waaraan een '
                   'provinciewapen; aan einde van het omschrift de afgekorte naam van een provincie',
                   'Gekroond Nederlands wapen tussen jaartal', 'zilver 873/1000', 'N', '', '', 'Zeven provinciën',
                   'map 3', 'N', 'Y', 'N', 'N', 'N', 'Theo Peters', '', '', 'KNM', '', 'Koningin Beatrix'),
                  ('5', '3965', '', 'KM# 190.2', '1', 'dukaat', 'Nederland', '1986', 'Aambeeld', 'PROOF', '', '950091',
                   '21 mm', 'Kabelrand', '', 'Medailleslag', '3.494 g', '',
                   'Staande ridder naar rechts met zwaard en pijlenbundel',
                   'Versierd vierkant met daarin: MO.AUR.REG.BELGII AD LEGEM IMPERII.', 'goud 983/1000', 'N', '', '',
                   '', 'map 4', 'Y', 'N', 'N', 'N', 'N', 'KNM', '', '', 'KNM', '', 'Koningin Beatrix')]
    c = conn.cursor()
    try:
        glob.logger_sql.debug("Inserting 5 records into table coin")
        c.executemany(sql_command, sql_tuples)
        conn.commit()
    except Exception as e:
        glob.logger_sql.debug(e)
