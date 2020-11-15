#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'M. Lebbink'
__copyright__ = 'Copyright 2020, Pecuniae Collectio'
__credits__ = ['I18n:'
               'Theo Despoudis'
               'https://phrase.com/blog/posts/translate-python-gnu-gettext/',

               'Treeview sorting:'
               'unknown'
               'https://www.pianshen.com/article/60037664/'
               ]
__license__ = 'CC BY-NC-ND 4.0 Attribution-NonCommercial-NoDerivatives 4.0 International'
__version__ = '0.0.3'
__maintainer__ = 'M. Lebbink'
__email__ = 'mlebbink@yahoo.com'
__status__ = 'Development'

# Done   1  Investigate decent multi language solution like https://docs.python.org/3/library/gettext.html
# Done      Check glob valiable for all frames, menu's and buttons
# Done   0  studie: https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
# Done   0  Create configuration import/management functions

# todo   1  Create logging functionality https://realpython.com/python-logging/

# todo   1  Create database function
# todo   1  Import test data function
# todo   1  Add a check databse option
# todo   1  validate config (directories) on startup and set alarm if it fails

# idea      Make sql fieldlist configurable
# idea      Replace top button bar with icons

# fixed     frame size in reloading with language button, delete frames was not deleting all frames.
# fix       Nothing at the moment :)

# System libs
import os
import time

# Own modules
from functions import glob
from functions import main_window as mwd
from functions import config_items as ci
from functions import journal_functions as jf

global _

# Setup some system variables
glob.mainpath = os.path.abspath(os.path.dirname(__file__))
glob.localespath = glob.mainpath + '\\locales'
glob.main_journal = ci.get_config_item("loc_logs") + "/system_journal" + "." + time.strftime("%Y%m%d")
glob.sql_journal = ci.get_config_item("loc_logs") + "/sql_journal" + "." + time.strftime("%Y%m%d")

# Write some log entries
jf.write_main_journal_entry("[main.py] - -----------------------")
jf.write_main_journal_entry("[main.py] - New PC session started.")
jf.write_main_journal_entry("[main.py] - system_version = " + glob.system_version)
jf.write_main_journal_entry("[main.py] - system_build = " + glob.system_build)
jf.write_main_journal_entry("[main.py] - system_sql = " + glob.system_sql)


def main():
    mwd.main_window()

    jf.write_main_journal_entry("[main.py] - Main closed by Exit.")

if __name__ == "__main__":
    main()
