#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import os
import os.path

# Own modules
from . import glob

# i18n
global _


def dump_vars():
    print("Script info:")
    print(f'    {str(type(glob.mainpath        )):28}  glob.mainpath       = {glob.mainpath}')
    print(f'    {str(type(glob.localespath     )):28}  glob.localespath    = {glob.localespath}')

    print("Version info:")
    print(f'    {str(type(glob.language        )):28}  glob.language        = {str(glob.language)}')
    print(f'    {str(type(glob.system_version  )):28}  glob.system_version  = {glob.mainpath}')
    print(f'    {str(type(glob.system_build    )):28}  glob.system_build    = {glob.system_build}')
    print(f'    {str(type(glob.system_sql      )):28}  glob.system_sql      = {glob.system_sql}')

    print("Log info:")
    print(f'    {str(type(glob.logger_main     )):28}  glob.logger_main     = {glob.logger_main}')
    print(f'    {str(type(glob.logger_sql      )):28}  glob.logger_sql      = {glob.logger_sql}')

    print("SQL info:")
    print(f'    {str(type(glob.open_filename   )):28}  glob.open_filename   = {glob.open_filename}')
    print(f'    {str(type(glob.current_open_db )):28}  glob.current_open_db = {glob.current_open_db}')
    print(f'    {str(type(glob.conn            )):28}  glob.conn            = {str(glob.conn)}')
    print(f'    {str(type(glob.cur             )):28}  glob.cur             = {str(glob.cur)}')
    print(f'    {str(type(glob.conn_new        )):28}  glob.conn_new        = {str(glob.conn_new)}')

    print("Config Tk variables:")
    print(f'    {str(type(glob.loc_database    )):28}  glob.loc_database    = {glob.loc_database}')
    print(f'    {str(type(glob.loc_scans       )):28}  glob.loc_scans       = {glob.loc_scans}')
    print(f'    {str(type(glob.loc_orders      )):28}  glob.loc_orders      = {glob.loc_orders}')
    print(f'    {str(type(glob.loc_logs        )):28}  glob.loc_logs        = {glob.loc_logs}')
    print(f'    {str(type(glob.loc_backups     )):28}  glob.loc_backups     = {glob.loc_backups}')

    print("-"*100)


def get_config_item(itemtoget):
    """ Retrieves requested configuration setting from coinv2.config file.

    Args:
        itemtoget: sting.

    Returns:
        Returns value found for requested configuration item.
    """
    with open(os.path.join(glob.mainpath, 'coinsv2.config'), "r") as fp:
        for line in fp:
            if not line.startswith('#'):
                if itemtoget in line:
                    line = line.split("=", 1)
                    if isinstance(line[-1], str):
                        line[-1] = line[-1].strip()
                        if glob.logger_main != 0:
                            glob.logger_main.debug('Retrieved %s = %s.' % (itemtoget, str(line[-1])))
                        return line[-1]
                    else:
                        if glob.logger_main != 0:
                            glob.logger_main.debug('Retrieved %s = %s.' % (itemtoget, line[-1]))
                        return line[-1]
