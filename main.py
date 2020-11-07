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

# todo   1  Create configuration import/management functions
# todo   1  Create logging functionality https://realpython.com/python-logging/
# todo   1  Create database function
# todo   1  Import test data function

# idea      Make sql fieldlist configurable
# idea      Replace top button bar with icons

# fix       Currently nothing needs fixing


# System libs
import os
import gettext
import logging

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from win32api import GetSystemMetrics                       # win32api is part of pywin32

# Own modules
import functions.main_window as mwd

logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')



def main():
    mwd.main_window()


if __name__ == "__main__":
    main()
