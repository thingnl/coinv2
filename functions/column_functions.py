#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import os
import time
from os import path
from tkinter import *

# Own modules
from . import glob
from . import language_functions as lf
from . import config_items as ci

# i18n
global _


def set_column_width():
    print("kak, old function still hanging around...")


def save_columns():
    # Rename config file to backup config file
    config_file = glob.mainpath + "\\coinsv2.config"
    new_config_file = glob.mainpath + "\\coinsv2.config.new"

    # Open existing config file for input
    file1 = open(config_file, 'r')

    # Open new config file for output
    file2 = open(new_config_file, 'w')

    glob.logger_main.info("Saving columns:")
    for line in file1:
        if line.startswith('radio_private_index'):
            file2.write("radio_private_index = " + str(glob.radio_private_index.get()) + '\n')
            glob.logger_main.debug("Wrote private_index = " + str(glob.radio_private_index.get()))
        elif line.startswith('radio_index'):
            file2.write("radio_index = " + str(glob.radio_index.get()) + '\n')
            glob.logger_main.debug("Wrote radio_index = " + str(glob.radio_index.get()))
        elif line.startswith('radio_krause_index'):
            file2.write("radio_krause_index = " + str(glob.radio_krause_index.get()) + '\n')
            glob.logger_main.debug("Wrote radio_krause_index = " + str(glob.radio_krause_index.get()))
        elif line.startswith('radio_denomination'):
            file2.write("radio_denomination = " + str(glob.radio_denomination.get()) + '\n')
            glob.logger_main.debug("Wrote radio_denomination = " + str(glob.radio_denomination.get()))
        elif line.startswith('radio_valuta'):
            file2.write("radio_valuta = " + str(glob.radio_valuta.get()) + '\n')
            glob.logger_main.debug("Wrote radio_valuta = " + str(glob.radio_valuta.get()))
        elif line.startswith('radio_country'):
            file2.write("radio_country = " + str(glob.radio_country.get()) + '\n')
            glob.logger_main.debug("Wrote radio_country = " + str(glob.radio_country.get()))
        elif line.startswith('radio_year'):
            file2.write("radio_year = " + str(glob.radio_year.get()) + '\n')
            glob.logger_main.debug("Wrote radio_year = " + str(glob.radio_year.get()))
        elif line.startswith('radio_mmt'):
            file2.write("radio_mmt = " + str(glob.radio_mmt.get()) + '\n')
            glob.logger_main.debug("Wrote radio_mmt = " + str(glob.radio_mmt.get()))
        elif line.startswith('radio_quality'):
            file2.write("radio_quality = " + str(glob.radio_quality.get()) + '\n')
            glob.logger_main.debug("Wrote radio_quality = " + str(glob.radio_quality.get()))
        elif line.startswith('radio_remark'):
            file2.write("radio_remark = " + str(glob.radio_remark.get()) + '\n')
            glob.logger_main.debug("Wrote radio_remark = " + str(glob.radio_remark.get()))
        elif line.startswith('radio_coinage'):
            file2.write("radio_coinage = " + str(glob.radio_coinage.get()) + '\n')
            glob.logger_main.debug("Wrote radio_coinage = " + str(glob.radio_coinage.get()))
        elif line.startswith('radio_diameter'):
            file2.write("radio_diameter = " + str(glob.radio_diameter.get()) + '\n')
            glob.logger_main.debug("Wrote radio_diameter = " + str(glob.radio_diameter.get()))
        elif line.startswith('radio_edge '):
            file2.write("radio_edge = " + str(glob.radio_edge.get()) + '\n')
            glob.logger_main.debug("Wrote radio_edge = " + str(glob.radio_edge.get()))
        elif line.startswith('radio_edgetext'):
            file2.write("radio_edgetext = " + str(glob.radio_edgetext.get()) + '\n')
            glob.logger_main.debug("Wrote radio_edgetext = " + str(glob.radio_edgetext.get()))
        elif line.startswith('radio_stiketype'):
            file2.write("radio_stiketype = " + str(glob.radio_stiketype.get()) + '\n')
            glob.logger_main.debug("Wrote radio_stiketype = " + str(glob.radio_stiketype.get()))
        elif line.startswith('radio_weight'):
            file2.write("radio_weight = " + str(glob.radio_weight.get()) + '\n')
            glob.logger_main.debug("Wrote radio_weight = " + str(glob.radio_weight.get()))
        elif line.startswith('radio_designer'):
            file2.write("radio_designer = " + str(glob.radio_designer.get()) + '\n')
            glob.logger_main.debug("Wrote radio_designer = " + str(glob.radio_designer.get()))
        elif line.startswith('radio_frontside'):
            file2.write("radio_frontside = " + str(glob.radio_frontside.get()) + '\n')
            glob.logger_main.debug("Wrote radio_frontside = " + str(glob.radio_frontside.get()))
        elif line.startswith('radio_rearside'):
            file2.write("radio_rearside = " + str(glob.radio_rearside.get()) + '\n')
            glob.logger_main.debug("Wrote radio_rearside = " + str(glob.radio_rearside.get()))
        elif line.startswith('radio_material'):
            file2.write("radio_material = " + str(glob.radio_material.get()) + '\n')
            glob.logger_main.debug("Wrote radio_material = " + str(glob.radio_material.get()))
        elif line.startswith('radio_rarity'):
            file2.write("radio_rarity = " + str(glob.radio_rarity.get()) + '\n')
            glob.logger_main.debug("Wrote radio_rarity = " + str(glob.radio_rarity.get()))
        elif line.startswith('radio_frontjpg'):
            file2.write("radio_frontjpg = " + str(glob.radio_frontjpg.get()) + '\n')
            glob.logger_main.debug("Wrote radio_frontjpg = " + str(glob.radio_frontjpg.get()))
        elif line.startswith('radio_rearjpg'):
            file2.write("radio_rearjpg = " + str(glob.radio_rearjpg.get()) + '\n')
            glob.logger_main.debug("Wrote radio_rearjpg = " + str(glob.radio_rearjpg.get()))
        elif line.startswith('radio_serie'):
            file2.write("radio_serie = " + str(glob.radio_serie.get()) + '\n')
            glob.logger_main.debug("Wrote radio_serie = " + str(glob.radio_serie.get()))
        elif line.startswith('radio_storage'):
            file2.write("radio_storage = " + str(glob.radio_storage.get()) + '\n')
            glob.logger_main.debug("Wrote radio_storage = " + str(glob.radio_storage.get()))
        elif line.startswith('radio_have'):
            file2.write("radio_have = " + str(glob.radio_have.get()) + '\n')
            glob.logger_main.debug("Wrote radio_have = " + str(glob.radio_have.get()))
        elif line.startswith('radio_want'):
            file2.write("radio_want = " + str(glob.radio_want.get()) + '\n')
            glob.logger_main.debug("Wrote radio_want = " + str(glob.radio_want.get()))
        elif line.startswith('radio_ordered'):
            file2.write("radio_ordered = " + str(glob.radio_ordered.get()) + '\n')
            glob.logger_main.debug("Wrote radio_ordered = " + str(glob.radio_ordered.get()))
        elif line.startswith('radio_sale'):
            file2.write("radio_sale = " + str(glob.radio_sale.get()) + '\n')
            glob.logger_main.debug("Wrote radio_sale = " + str(glob.radio_sale.get()))
        elif line.startswith('radio_other'):
            file2.write("radio_other = " + str(glob.radio_other.get()) + '\n')
            glob.logger_main.debug("Wrote radio_other = " + str(glob.radio_other.get()))
        elif line.startswith('radio_supplier'):
            file2.write("radio_supplier = " + str(glob.radio_supplier.get()) + '\n')
            glob.logger_main.debug("Wrote radio_supplier = " + str(glob.radio_supplier.get()))
        elif line.startswith('radio_order '):           # INCLUDE SPACE
            file2.write("radio_order = " + str(glob.radio_order.get()) + '\n')
            glob.logger_main.debug("Wrote radio_order = " + str(glob.radio_order.get()))
        elif line.startswith('radio_price'):
            file2.write("radio_price = " + str(glob.radio_price.get()) + '\n')
            glob.logger_main.debug("Wrote radio_price = " + str(glob.radio_price.get()))
        elif line.startswith('radio_mint '):
            file2.write("radio_mint = " + str(glob.radio_mint.get()) + '\n')
            glob.logger_main.debug("Wrote radio_mint = " + str(glob.radio_mint.get()))
        elif line.startswith('radio_mintmaster'):
            file2.write("radio_mintmaster = " + str(glob.radio_mintmaster.get()) + '\n')
            glob.logger_main.debug("Wrote radio_mintmaster = " + str(glob.radio_mintmaster.get()))
        elif line.startswith('radio_ruler'):
            file2.write("radio_ruler = " + str(glob.radio_ruler.get()) + '\n')
            glob.logger_main.debug("Wrote radio_ruler = " + str(glob.radio_ruler.get()))
        else:
            file2.write(line)

    # Closing files
    file1.close()
    file2.close()

    # Rename current file
    os.rename(config_file, config_file + "." + time.strftime("%Y%m%d-%H%M%S"))
    glob.logger_main.debug("Old config moved to " + config_file + "." + time.strftime("%Y%m%d-%H%M%S"))

    # Rename new config file
    os.rename(new_config_file, config_file)

    lf.send_message(_("New settings saved to configuration file."))
    glob.logger_main.info("New settings saved to " + config_file + ".")

    # Try apply'ing. May need to check for active database
    apply_column_hide()

    # Close edit window
    glob.top.destroy()


def get_column_settings():
    """ Get all the settings for the column configuration screen.

    Args:
        None.

    Returns:
        Returns nothing but put all the settings directly on screen.
    """
    config_file = glob.mainpath + "\\coinsv2.config"
    if not path.exists(config_file):
        glob.radio_private_index.set("Show")
        glob.radio_index.set("Show")
        glob.radio_krause_index.set("Show")
        glob.radio_denomination.set("Show")
        glob.radio_valuta.set("Show")
        glob.radio_country.set("Show")
        glob.radio_year.set("Show")
        glob.radio_mmt.set("Show")
        glob.radio_quality.set("Show")
        glob.radio_remark.set("Show")
        glob.radio_coinage.set("Show")
        glob.radio_diameter.set("Show")
        glob.radio_edge.set("Show")
        glob.radio_edgetext.set("Show")
        glob.radio_stiketype.set("Show")
        glob.radio_weight.set("Show")
        glob.radio_designer.set("Show")
        glob.radio_frontside.set("Show")
        glob.radio_rearside.set("Show")
        glob.radio_material.set("Show")
        glob.radio_rarity.set("Show")
        glob.radio_frontjpg.set("Show")
        glob.radio_rearjpg.set("Show")
        glob.radio_serie.set("Show")
        glob.radio_storage.set("Show")
        glob.radio_have.set("Show")
        glob.radio_want.set("Show")
        glob.radio_ordered.set("Show")
        glob.radio_sale.set("Show")
        glob.radio_other.set("Show")
        glob.radio_supplier.set("Show")
        glob.radio_order.set("Show")
        glob.radio_price.set("Show")
        glob.radio_mint.set("Show")
        glob.radio_mintmaster.set("Show")
        glob.radio_ruler.set("Show")
    else:
        glob.radio_private_index.set(ci.get_config_item("radio_private_index"))
        glob.radio_index.set(ci.get_config_item("radio_index"))
        glob.radio_krause_index.set(ci.get_config_item("radio_krause_index"))
        glob.radio_denomination.set(ci.get_config_item("radio_denomination"))
        glob.radio_valuta.set(ci.get_config_item("radio_valuta"))
        glob.radio_country.set(ci.get_config_item("radio_country"))
        glob.radio_year.set(ci.get_config_item("radio_year"))
        glob.radio_mmt.set(ci.get_config_item("radio_mmt"))
        glob.radio_quality.set(ci.get_config_item("radio_quality"))
        glob.radio_remark.set(ci.get_config_item("radio_remark"))
        glob.radio_coinage.set(ci.get_config_item("radio_coinage"))
        glob.radio_diameter.set(ci.get_config_item("radio_diameter"))
        glob.radio_edge.set(ci.get_config_item("radio_edge "))
        glob.radio_edgetext.set(ci.get_config_item("radio_edgetext"))
        glob.radio_stiketype.set(ci.get_config_item("radio_stiketype"))
        glob.radio_weight.set(ci.get_config_item("radio_weight"))
        glob.radio_designer.set(ci.get_config_item("radio_designer"))
        glob.radio_frontside.set(ci.get_config_item("radio_frontside"))
        glob.radio_rearside.set(ci.get_config_item("radio_rearside"))
        glob.radio_material.set(ci.get_config_item("radio_material"))
        glob.radio_rarity.set(ci.get_config_item("radio_rarity"))
        glob.radio_frontjpg.set(ci.get_config_item("radio_frontjpg"))
        glob.radio_rearjpg.set(ci.get_config_item("radio_rearjpg"))
        glob.radio_serie.set(ci.get_config_item("radio_serie"))
        glob.radio_storage.set(ci.get_config_item("radio_storage"))
        glob.radio_have.set(ci.get_config_item("radio_have"))
        glob.radio_want.set(ci.get_config_item("radio_want"))
        glob.radio_ordered.set(ci.get_config_item("radio_ordered"))
        glob.radio_sale.set(ci.get_config_item("radio_sale"))
        glob.radio_other.set(ci.get_config_item("radio_other"))
        glob.radio_supplier.set(ci.get_config_item("radio_supplier"))
        glob.radio_order.set(ci.get_config_item("radio_order "))            # INCLUDE SPACE or it matches radio_ordered
        glob.radio_price.set(ci.get_config_item("radio_price"))
        glob.radio_mint.set(ci.get_config_item("radio_mint"))
        glob.radio_mintmaster.set(ci.get_config_item("radio_mintmaster"))
        glob.radio_ruler.set(ci.get_config_item("radio_ruler"))


def apply_column_hide():
    if len(glob.coin_data) != 0:

        # Combine all tuple columns into lines
        elements = list(zip(*glob.coin_data))
        # next, get longest value like len(max(elements[1], key=len)
        # Take longest value from field or header length like max(len(max(elements[2], key=len)) * 9, len("Index") * 8)

        if ci.get_config_item("radio_private_index") == "Hide":
            glob.sql_frame.column("#2", width=0, minwidth=0)    # minwidth=0 is needed or it will default to 20!
        else:
            glob.sql_frame.column("#2", width=max(len(max(elements[1], key=len)) * 9, len("Private index") * 6),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_index") == "Hide":
            glob.sql_frame.column("#3", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#3", width=max(len(max(elements[2], key=len)) * 9, len("Index") * 8), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_krause_index") == "Hide":
            glob.sql_frame.column("#4", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#4", width=max(len(max(elements[3], key=len)) * 9, len("Krause") * 6), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_denomination") == "Hide":
            glob.sql_frame.column("#5", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#5", width=max(len(max(elements[4], key=len)) * 9, len("Denomination") * 7),
                                  minwidth=0, stretch=NO, anchor=E)

        if ci.get_config_item("radio_valuta") == "Hide":
            glob.sql_frame.column("#6", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#6", width=max(len(max(elements[5], key=len)) * 9, len("Valuta") * 6), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_country") == "Hide":
            glob.sql_frame.column("#7", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#7", width=max(len(max(elements[6], key=len)) * 9, len("Country") * 6), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_year") == "Hide":
            glob.sql_frame.column("#8", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#8", width=max(len(max(elements[7], key=len)) * 9, len("Year") * 6), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_mmt") == "Hide":
            glob.sql_frame.column("#9", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#9", width=max(len(max(elements[8], key=len)) * 9, len("Mmt") * 6), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_quality") == "Hide":
            glob.sql_frame.column("#10", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#10", width=max(len(max(elements[9], key=len)) * 9, len("Quality") * 7), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_remark") == "Hide":
            glob.sql_frame.column("#11", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#11", width=max(len(max(elements[10], key=len)) * 9, len("Remark") * 6), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_coinage") == "Hide":
            glob.sql_frame.column("#12", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#12", width=max(len(max(elements[11], key=len)) * 9, len("Coinage") * 6),
                                  minwidth=0, stretch=NO, anchor=E)

        if ci.get_config_item("radio_diameter") == "Hide":
            glob.sql_frame.column("#13", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#13", width=max(len(max(elements[12], key=len)) * 9, len("Diameter") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_edge") == "Hide":
            glob.sql_frame.column("#14", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#14", width=max(len(max(elements[13], key=len)) * 8, len("Edge") * 6), minwidth=0,
                                  stretch=NO)

        if ci.get_config_item("radio_edgetext") == "Hide":
            glob.sql_frame.column("#15", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#15", width=max(len(max(elements[14], key=len)) * 8, len("Edge text") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_stiketype") == "Hide":
            glob.sql_frame.column("#16", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#16", width=max(len(max(elements[15], key=len)) * 9, len("Strike type") * 6),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_weight") == "Hide":
            glob.sql_frame.column("#17", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#17", width=max(len(max(elements[16], key=len)) * 9, len("Weight") * 6),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_designer") == "Hide":
            glob.sql_frame.column("#18", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#18", width=max(len(max(elements[17], key=len)) * 9, len("Designer") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_frontside") == "Hide":
            glob.sql_frame.column("#19", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#19", width=max(len(max(elements[18], key=len)) * 7, len("Front side") * 6),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_rearside") == "Hide":
            glob.sql_frame.column("#20", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#20", width=max(len(max(elements[19], key=len)) * 7, len("Rear side") * 6),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_material") == "Hide":
            glob.sql_frame.column("#21", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#21", width=max(len(max(elements[20], key=len)) * 7, len("Material") * 6),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_rarity") == "Hide":
            glob.sql_frame.column("#22", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#22", width=max(len(max(elements[21], key=len)) * 9, len("Rarity") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_frontjpg") == "Hide":
            glob.sql_frame.column("#23", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#23", width=max(len(max(elements[22], key=len)) * 7, len("Front jpg") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_rearjpg") == "Hide":
            glob.sql_frame.column("#24", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#24", width=max(len(max(elements[23], key=len)) * 7, len("Rear jpg") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_serie") == "Hide":
            glob.sql_frame.column("#25", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#25", width=max(len(max(elements[24], key=len)) * 9, len("Serie") * 6),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_storage") == "Hide":
            glob.sql_frame.column("#26", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#26", width=max(len(max(elements[25], key=len)) * 9, len("Storage") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_have") == "Hide":
            glob.sql_frame.column("#27", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#27", width=max(len(max(elements[26], key=len)) * 9, len("Have") * 9),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_want") == "Hide":
            glob.sql_frame.column("#28", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#28", width=max(len(max(elements[27], key=len)) * 9, len("Want") * 9),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_ordered") == "Hide":
            glob.sql_frame.column("#29", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#29", width=max(len(max(elements[28], key=len)) * 9, len("Ordered") * 8),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_sale") == "Hide":
            glob.sql_frame.column("#30", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#30", width=max(len(max(elements[29], key=len)) * 9, len("For sale") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_other") == "Hide":
            glob.sql_frame.column("#31", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#31", width=max(len(max(elements[30], key=len)) * 9, len("Other") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_supplier") == "Hide":
            glob.sql_frame.column("#32", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#32", width=max(len(max(elements[31], key=len)) * 9, len("Supplier") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_order ") == "Hide":                # INCLUDE SPACE or it matches radio_ordered
            glob.sql_frame.column("#33", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#33", width=max(len(max(elements[32], key=len)) * 9, len("Order no") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_price") == "Hide":
            glob.sql_frame.column("#34", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#34", width=max(len(max(elements[33], key=len)) * 9, len("Price") * 9),
                                  minwidth=0, stretch=NO, anchor=E)

        if ci.get_config_item("radio_mint") == "Hide":
            glob.sql_frame.column("#35", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#35", width=max(len(max(elements[34], key=len)) * 9, len("Mint") * 9),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_mintmaster") == "Hide":
            glob.sql_frame.column("#36", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#36", width=max(len(max(elements[35], key=len)) * 9, len("Mintmaster") * 7),
                                  minwidth=0, stretch=NO)

        if ci.get_config_item("radio_ruler") == "Hide":
            glob.sql_frame.column("#37", width=0, minwidth=0)
        else:
            glob.sql_frame.column("#37", width=max(len(max(elements[36], key=len)) * 9, len("Ruler") * 7),
                                  minwidth=0, stretch=NO)

    # glob.sql_frame.update()   seems to do fuck-all


def build_hide_show():
    glob.top = Toplevel()
    glob.top.title(_("Hide/Show Columns"))
    glob.top.geometry('%sx%s' % (800, 600))
    glob.top.option_add("*Font", "Segoe 8")
    glob.top.grab_set()                      # Disable input on main window.

    # Create frames
    glob.edit_edit_frame = Frame(master=glob.top, padx=5, pady=5)
    glob.edit_button_frame = Frame(master=glob.top, height=70, bg="gray85", padx=5, pady=5)

    glob.edit_edit_frame.pack(fill=BOTH, expand=1)
    glob.edit_button_frame.pack(fill=BOTH, expand=0)

    # Create buttons
    glob.button_edit_cancel = Button(glob.edit_button_frame, text=_("Cancel"),
                                     command=lambda: glob.top.destroy(), padx=20)
    glob.button_edit_cancel.pack(side=LEFT, pady=10, padx=10)

    glob.button_edit_save = Button(glob.edit_button_frame, text=_("Save"), command=lambda: save_columns(), padx=20)
    glob.button_edit_save.pack(side=RIGHT, pady=10, padx=10)

    label_mainwindow = Label(glob.edit_edit_frame, text=_("Hide or Show columns:"),
                             font=("Segoe", 10, 'bold underline'), anchor="w", width=20)
    label_mainwindow.grid(row=1, column=1, columnspan=2)

    label_empty_line = Label(glob.edit_edit_frame, text=" ", anchor="w", width=20)
    label_empty_line.grid(row=2, column=1)

    label_fill1_line = Label(glob.edit_edit_frame, text=" ", anchor="w", width=20)
    label_fill1_line.grid(row=2, column=7)
    label_fill2_line = Label(glob.edit_edit_frame, text="Hide")
    label_fill2_line.grid(row=3, column=3)
    label_fill3_line = Label(glob.edit_edit_frame, text="Show")
    label_fill3_line.grid(row=3, column=4)
    label_fill4_line = Label(glob.edit_edit_frame, text="Hide")
    label_fill4_line.grid(row=3, column=9)
    label_fill5_line = Label(glob.edit_edit_frame, text="Show")
    label_fill5_line.grid(row=3, column=10)

    # --------
    label_private_index = Label(glob.edit_edit_frame, text=_("Private Index:"), anchor="w", width=20)
    label_private_index.grid(row=4, column=2)
    glob.radio_private_index = StringVar()
    radio1_private_index = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_private_index, value="Hide")
    radio2_private_index = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_private_index, value="Show")
    radio1_private_index.grid(row=4, column=3)
    radio2_private_index.grid(row=4, column=4)
    # --------
    label_index = Label(glob.edit_edit_frame, text=_("Index:"), anchor="w", width=20)
    label_index.grid(row=5, column=2)
    glob.radio_index = StringVar()
    radio1_index = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_index, value="Hide")
    radio2_index = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_index, value="Show")
    radio1_index.grid(row=5, column=3)
    radio2_index.grid(row=5, column=4)
    # --------
    label_krause_index = Label(glob.edit_edit_frame, text=_("Krause Index:"), anchor="w", width=20)
    label_krause_index.grid(row=6, column=2)
    glob.radio_krause_index = StringVar()
    radio1_krause_index = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_krause_index, value="Hide")
    radio2_krause_index = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_krause_index, value="Show")
    radio1_krause_index.grid(row=6, column=3)
    radio2_krause_index.grid(row=6, column=4)
    # --------
    label_denomination = Label(glob.edit_edit_frame, text=_("Denomination:"), anchor="w", width=20)
    label_denomination.grid(row=7, column=2)
    glob.radio_denomination = StringVar()
    radio1_denomination = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_denomination, value="Hide")
    radio2_denomination = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_denomination, value="Show")
    radio1_denomination.grid(row=7, column=3)
    radio2_denomination.grid(row=7, column=4)
    # --------
    label_valuta = Label(glob.edit_edit_frame, text=_("Valuta:"), anchor="w", width=20)
    label_valuta.grid(row=8, column=2)
    glob.radio_valuta = StringVar()
    radio1_valuta = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_valuta, value="Hide")
    radio2_valuta = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_valuta, value="Show")
    radio1_valuta.grid(row=8, column=3)
    radio2_valuta.grid(row=8, column=4)
    # --------
    label_country = Label(glob.edit_edit_frame, text=_("Country:"), anchor="w", width=20)
    label_country.grid(row=9, column=2)
    glob.radio_country = StringVar()
    radio1_country = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_country, value="Hide")
    radio2_country = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_country, value="Show")
    radio1_country.grid(row=9, column=3)
    radio2_country.grid(row=9, column=4)
    # --------
    label_year = Label(glob.edit_edit_frame, text=_("Year:"), anchor="w", width=20)
    label_year.grid(row=10, column=2)
    glob.radio_year = StringVar()
    radio1_year = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_year, value="Hide")
    radio2_year = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_year, value="Show")
    radio1_year.grid(row=10, column=3)
    radio2_year.grid(row=10, column=4)
    # --------
    label_mmt = Label(glob.edit_edit_frame, text=_("Mintmaster sign:"), anchor="w", width=20)
    label_mmt.grid(row=11, column=2)
    glob.radio_mmt = StringVar()
    radio1_mmt = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_mmt, value="Hide")
    radio2_mmt = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_mmt, value="Show")
    radio1_mmt.grid(row=11, column=3)
    radio2_mmt.grid(row=11, column=4)
    # --------
    label_quality = Label(glob.edit_edit_frame, text=_("Quality:"), anchor="w", width=20)
    label_quality.grid(row=12, column=2)
    glob.radio_quality = StringVar()
    radio1_quality = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_quality, value="Hide")
    radio2_quality = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_quality, value="Show")
    radio1_quality.grid(row=12, column=3)
    radio2_quality.grid(row=12, column=4)
    # --------
    label_remark = Label(glob.edit_edit_frame, text=_("Remark:"), anchor="w", width=20)
    label_remark.grid(row=13, column=2)
    glob.radio_remark = StringVar()
    radio1_remark = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_remark, value="Hide")
    radio2_remark = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_remark, value="Show")
    radio1_remark.grid(row=13, column=3)
    radio2_remark.grid(row=13, column=4)
    # --------
    label_coinage = Label(glob.edit_edit_frame, text=_("Coinage:"), anchor="w", width=20)
    label_coinage.grid(row=14, column=2)
    glob.radio_coinage = StringVar()
    radio1_coinage = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_coinage, value="Hide")
    radio2_coinage = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_coinage, value="Show")
    radio1_coinage.grid(row=14, column=3)
    radio2_coinage.grid(row=14, column=4)
    # --------
    label_diameter = Label(glob.edit_edit_frame, text=_("Diameter:"), anchor="w", width=20)
    label_diameter.grid(row=15, column=2)
    glob.radio_diameter = StringVar()
    radio1_diameter = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_diameter, value="Hide")
    radio2_diameter = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_diameter, value="Show")
    radio1_diameter.grid(row=15, column=3)
    radio2_diameter.grid(row=15, column=4)
    # --------
    label_edge = Label(glob.edit_edit_frame, text=_("Edge:"), anchor="w", width=20)
    label_edge.grid(row=16, column=2)
    glob.radio_edge = StringVar()
    radio1_edge = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_edge, value="Hide")
    radio2_edge = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_edge, value="Show")
    radio1_edge.grid(row=16, column=3)
    radio2_edge.grid(row=16, column=4)
    # --------
    label_edgetext = Label(glob.edit_edit_frame, text=_("Edge text:"), anchor="w", width=20)
    label_edgetext.grid(row=17, column=2)
    glob.radio_edgetext = StringVar()
    radio1_edgetext = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_edgetext, value="Hide")
    radio2_edgetext = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_edgetext, value="Show")
    radio1_edgetext.grid(row=17, column=3)
    radio2_edgetext.grid(row=17, column=4)
    # --------
    label_stiketype = Label(glob.edit_edit_frame, text=_("Strike type:"), anchor="w", width=20)
    label_stiketype.grid(row=18, column=2)
    glob.radio_stiketype = StringVar()
    radio1_stiketype = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_stiketype, value="Hide")
    radio2_stiketype = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_stiketype, value="Show")
    radio1_stiketype.grid(row=18, column=3)
    radio2_stiketype.grid(row=18, column=4)
    # --------
    label_weight = Label(glob.edit_edit_frame, text=_("Weight:"), anchor="w", width=20)
    label_weight.grid(row=19, column=2)
    glob.radio_weight = StringVar()
    radio1_weight = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_weight, value="Hide")
    radio2_weight = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_weight, value="Show")
    radio1_weight.grid(row=19, column=3)
    radio2_weight.grid(row=19, column=4)
    # --------
    label_designer = Label(glob.edit_edit_frame, text=_("Designer:"), anchor="w", width=20)
    label_designer.grid(row=20, column=2)
    glob.radio_designer = StringVar()
    radio1_designer = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_designer, value="Hide")
    radio2_designer = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_designer, value="Show")
    radio1_designer.grid(row=20, column=3)
    radio2_designer.grid(row=20, column=4)
    # --------
    label_frontside = Label(glob.edit_edit_frame, text=_("Front side description:"), anchor="w", width=20)
    label_frontside.grid(row=21, column=2)
    glob.radio_frontside = StringVar()
    radio1_frontside = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_frontside, value="Hide")
    radio2_frontside = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_frontside, value="Show")
    radio1_frontside.grid(row=21, column=3)
    radio2_frontside.grid(row=21, column=4)
    # --------
    label_rearside = Label(glob.edit_edit_frame, text=_("Rear side description:"), anchor="w", width=20)
    label_rearside.grid(row=22, column=2)
    glob.radio_rearside = StringVar()
    radio1_rearside = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_rearside, value="Hide")
    radio2_rearside = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_rearside, value="Show")
    radio1_rearside.grid(row=22, column=3)
    radio2_rearside.grid(row=22, column=4)
    # --------
    label_material = Label(glob.edit_edit_frame, text=_("Material:"), anchor="w", width=20)
    label_material.grid(row=4, column=8)
    glob.radio_material = StringVar()
    radio1_material = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_material, value="Hide")
    radio2_material = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_material, value="Show")
    radio1_material.grid(row=4, column=9)
    radio2_material.grid(row=4, column=10)
    # --------
    label_rarity = Label(glob.edit_edit_frame, text=_("Rarity:"), anchor="w", width=20)
    label_rarity.grid(row=5, column=8)
    glob.radio_rarity = StringVar()
    radio1_rarity = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_rarity, value="Hide")
    radio2_rarity = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_rarity, value="Show")
    radio1_rarity.grid(row=5, column=9)
    radio2_rarity.grid(row=5, column=10)
    # --------
    label_frontjpg = Label(glob.edit_edit_frame, text=_("Front side image:"), anchor="w", width=20)
    label_frontjpg.grid(row=6, column=8)
    glob.radio_frontjpg = StringVar()
    radio1_frontjpg = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_frontjpg, value="Hide")
    radio2_frontjpg = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_frontjpg, value="Show")
    radio1_frontjpg.grid(row=6, column=9)
    radio2_frontjpg.grid(row=6, column=10)
    # --------
    label_rearjpg = Label(glob.edit_edit_frame, text=_("Rear side image:"), anchor="w", width=20)
    label_rearjpg.grid(row=7, column=8)
    glob.radio_rearjpg = StringVar()
    radio1_rearjpg = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_rearjpg, value="Hide")
    radio2_rearjpg = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_rearjpg, value="Show")
    radio1_rearjpg.grid(row=7, column=9)
    radio2_rearjpg.grid(row=7, column=10)
    # --------
    label_serie = Label(glob.edit_edit_frame, text=_("Serie:"), anchor="w", width=20)
    label_serie.grid(row=8, column=8)
    glob.radio_serie = StringVar()
    radio1_serie = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_serie, value="Hide")
    radio2_serie = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_serie, value="Show")
    radio1_serie.grid(row=8, column=9)
    radio2_serie.grid(row=8, column=10)
    # --------
    label_storage = Label(glob.edit_edit_frame, text=_("Storage:"), anchor="w", width=20)
    label_storage.grid(row=9, column=8)
    glob.radio_storage = StringVar()
    radio1_storage = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_storage, value="Hide")
    radio2_storage = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_storage, value="Show")
    radio1_storage.grid(row=9, column=9)
    radio2_storage.grid(row=9, column=10)
    # --------
    label_have = Label(glob.edit_edit_frame, text=_("In collection:"), anchor="w", width=20)
    label_have.grid(row=10, column=8)
    glob.radio_have = StringVar()
    radio1_have = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_have, value="Hide")
    radio2_have = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_have, value="Show")
    radio1_have.grid(row=10, column=9)
    radio2_have.grid(row=10, column=10)
    # --------
    label_want = Label(glob.edit_edit_frame, text=_("Missing from collection:"), anchor="w", width=20)
    label_want.grid(row=11, column=8)
    glob.radio_want = StringVar()
    radio1_want = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_want, value="Hide")
    radio2_want = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_want, value="Show")
    radio1_want.grid(row=11, column=9)
    radio2_want.grid(row=11, column=10)
    # --------
    label_ordered = Label(glob.edit_edit_frame, text=_("On order:"), anchor="w", width=20)
    label_ordered.grid(row=12, column=8)
    glob.radio_ordered = StringVar()
    radio1_ordered = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_ordered, value="Hide")
    radio2_ordered = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_ordered, value="Show")
    radio1_ordered.grid(row=12, column=9)
    radio2_ordered.grid(row=12, column=10)
    # --------
    label_sale = Label(glob.edit_edit_frame, text=_("Is for sale:"), anchor="w", width=20)
    label_sale.grid(row=13, column=8)
    glob.radio_sale = StringVar()
    radio1_sale = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_sale, value="Hide")
    radio2_sale = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_sale, value="Show")
    radio1_sale.grid(row=13, column=9)
    radio2_sale.grid(row=13, column=10)
    # --------
    label_other = Label(glob.edit_edit_frame, text=_("Free to use y/n:"), anchor="w", width=20)
    label_other.grid(row=14, column=8)
    glob.radio_other = StringVar()
    radio1_other = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_other, value="Hide")
    radio2_other = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_other, value="Show")
    radio1_other.grid(row=14, column=9)
    radio2_other.grid(row=14, column=10)
    # --------
    label_supplier = Label(glob.edit_edit_frame, text=_("Supplier:"), anchor="w", width=20)
    label_supplier.grid(row=15, column=8)
    glob.radio_supplier = StringVar()
    radio1_supplier = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_supplier, value="Hide")
    radio2_supplier = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_supplier, value="Show")
    radio1_supplier.grid(row=15, column=9)
    radio2_supplier.grid(row=15, column=10)
    # --------
    label_order = Label(glob.edit_edit_frame, text=_("Order number:"), anchor="w", width=20)
    label_order.grid(row=16, column=8)
    glob.radio_order = StringVar()
    radio1_order = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_order, value="Hide")
    radio2_order = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_order, value="Show")
    radio1_order.grid(row=16, column=9)
    radio2_order.grid(row=16, column=10)
    # --------
    label_price = Label(glob.edit_edit_frame, text=_("Purchase price:"), anchor="w", width=20)
    label_price.grid(row=17, column=8)
    glob.radio_price = StringVar()
    radio1_price = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_price, value="Hide")
    radio2_price = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_price, value="Show")
    radio1_price.grid(row=17, column=9)
    radio2_price.grid(row=17, column=10)
    # --------
    label_mint = Label(glob.edit_edit_frame, text=_("Mint:"), anchor="w", width=20)
    label_mint.grid(row=18, column=8)
    glob.radio_mint = StringVar()
    radio1_mint = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_mint, value="Hide")
    radio2_mint = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_mint, value="Show")
    radio1_mint.grid(row=18, column=9)
    radio2_mint.grid(row=18, column=10)
    # --------
    label_mintmaster = Label(glob.edit_edit_frame, text=_("Mintmaster:"), anchor="w", width=20)
    label_mintmaster.grid(row=19, column=8)
    glob.radio_mintmaster = StringVar()
    radio1_mintmaster = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_mintmaster, value="Hide")
    radio2_mintmaster = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_mintmaster, value="Show")
    radio1_mintmaster.grid(row=19, column=9)
    radio2_mintmaster.grid(row=19, column=10)
    # --------
    label_ruler = Label(glob.edit_edit_frame, text=_("State ruler:"), anchor="w", width=20)
    label_ruler.grid(row=20, column=8)
    glob.radio_ruler = StringVar()
    radio1_ruler = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_ruler, value="Hide")
    radio2_ruler = Radiobutton(glob.edit_edit_frame, text="", variable=glob.radio_ruler, value="Show")
    radio1_ruler.grid(row=20, column=9)
    radio2_ruler.grid(row=20, column=10)


def hide_show_columns():
    glob.logger_main.info("Hide/Show Columns starting.")
    build_hide_show()
    get_column_settings()

    glob.logger_main.info("Hide/Show Columns window closed.")
