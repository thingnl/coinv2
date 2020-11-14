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

# todo   0  studie: https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
# todo   1  Create configuration import/management functions
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
# import gettext
# Own modules
from functions import glob
from functions import main_window as mwd

global _

glob.mainpath = os.path.abspath(os.path.dirname(__file__))
glob.localespath = glob.mainpath + '\\locales'


def main():
    mwd.main_window()


if __name__ == "__main__":
    main()
