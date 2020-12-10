#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'M. Lebbink'
__copyright__ = 'Copyright 2020, Pecuniae Collectio'
__credits__ = ['I18n:'
               'Theo Despoudis'
               'https://phrase.com/blog/posts/translate-python-gnu-gettext/',

               'Logging:'
               'Gank'
               'https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings',

               'Treeview sorting:'
               'unknown'
               'https://www.pianshen.com/article/60037664/',

               'Treeview hiding columns:'
               'R4PH43L'
               'https://stackoverflow.com/questions/33290969/hiding-treeview-columns-in-tkinter'
               ]
__license__ = 'CC BY-NC-ND 4.0 Attribution-NonCommercial-NoDerivatives 4.0 International'
__version__ = '0.0.3'
__maintainer__ = 'M. Lebbink'
__email__ = 'mlebbink@yahoo.com'
__status__ = 'Development'

# todone 1  Investigate decent multi language solution like https://docs.python.org/3/library/gettext.html
# todone 1  Check glob valiable for all frames, menu's and buttons
# todone 0  studie: https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
# todone 0  Create configuration import/management functions
# todone 1  Create logging functionality
# todone 1  Add main loglevel setting to config file (INFO-20/DEBUG-10/NOTSET-0)
# todone 1  Add sql loglevel setting to config file (INFO-20/DEBUG-10/NOTSET-0)
# todone 1  Add show main log option to system menu
# todone 1  Add show sql log option to main menu
# todone 1  Create create database function
# todone 1  Before loading testdata, verify db is open and empty: SELECT exists(SELECT 1 FROM MyTable LIMIT 1);
# todone 1  Import/create test data function
# todo   1  Create housekeeping function to clear out old logs and config files
# todo   1  Add a check database option to system menu
# todo   1  validate config (directories) on startup and set alarm if it fails
# todo   2  Update language select on config screen to use stringvar() iso intvar(), like logging
# todo   2  SQL housekeeping function Vacuum (https://sqlite.org/lang_vacuum.html)
# todo   2  SQL housekeeping function integrity check
# todo   2  SQL housekeeping function foreign key check
# todo   2  SQL housekeeping function optimize
# todo   2  SQL housekeeping function compact
# todo   3  Create reports (or some query engine app)
# todo   2  Strike type missing from coin, need to check
# todo   2  Obverse in stead of front
# todo   2  Reverse in stead of rear
# todo   2  Ruler in stead of Head of state
# todo   2  Subject for Serie
# todo   2  Date for year
# todo   2  Mintage/Minted as struck
# todo   2  Edge lettering voor randschrift
# todo   2  Add to config screen: open last database on startup?
# todo   2  Add to config screen: Include jpg in backup?
# todo   2  Add to config screen: Include orders in backup?
# todo   2  Add to config screen: log SQL data?
# todo   2  Add to config screen: max days to keep logs, 0 = keep all?
# todo   2  Movable columns: https://stackoverflow.com/questions/51378611
#                                                     /python-tkinter-table-order-table-columns-with-drag-and-drop
# todo   2  Make row editable: https://stackoverflow.com/questions/18562123/how-to-make-ttk-treeviews-rows-editable
# todo   2  Check this: https://github.com/ragardner/tksheet iso sql window

# idone     Add Schema Version table to SQL database
# idone     Make sql fieldlist configurable
# idea      Replace top button bar with icons
# idea      Some library function to link PDF catalogs like a library
# idea      Krause books: https://world-coins.weebly.com/krause-catalogs--other-books.html

# fixed     frame size in reloading with language button, delete frames was not deleting all frames.
# fixed     Menu exit does not, takes 3 times to actually exit. Switched to logger, solved write delay (4 now)
# fixed     Creating and opening new database does not create sql frame. Forgot a glob.
# fixed     On loading empty database, treeview crashes with out of range error. Fixed by checking length != 0
# fixed     On loading defective database, reset loaded file indicators. Fixed with glob.current_open_db = ""
# fixed     Auto reload after adding testdata working. Needed new glob.conn & glob.cur after closing
# fix       Cleanup opening logfiles and add log entries on opening, depending on settings in config


# System libs
import os
import time
import logging

# Own modules
from functions import glob
from functions import main_window as mwd
from functions import config_items as ci
from functions import journal_functions as jf

global _

# Setup some system variables
glob.mainpath = os.path.abspath(os.path.dirname(__file__))
glob.localespath = glob.mainpath + '\\locales'
glob.main_journal = ci.get_config_item("loc_logs") + "/system_journal" + "." + time.strftime("%Y%m%d") + ".log"
glob.sql_journal = ci.get_config_item("loc_logs") + "/sql_journal" + "." + time.strftime("%Y%m%d") + ".log"

# Setup logging
jf.setup_logger('Main_log', glob.main_journal, ci.get_config_item("main_log_level"))
jf.setup_logger('SQL_log', glob.sql_journal, ci.get_config_item("sql_log_level"))
glob.logger_main = logging.getLogger('Main_log')
glob.logger_sql = logging.getLogger('SQL_log')

jf.log_new_start()


def main():
    mwd.main_window()

    glob.logger_main.info("Main closed by Exit.")


if __name__ == "__main__":
    main()
