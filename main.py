#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'M. Lebbink'
__copyright__ = 'Copyright 2020, Pecuniae Collectio'
__credits__ = ['Billal Begueradj: https://stackoverflow.com/questions/36240787/'
               'python-3-4-tkinter-not-able-to-give-a-size-to-frames-in-panedwindow',

               'ReflexTechR: https://stackoverflow.com/questions/60740268/populate-treeview-with-info-from-sql',

               'GinTonic: https://stackoverflow.com/questions/56331001/'
               'python-tkinter-treeview-colors-are-not-updating/60949800#60949800',

               'Martin Thoma: https://martin-thoma.com/configuration-files-in-python/',

               'Treeview sorting:'
               'https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u='
               'https%3A%2F%2Fwww.pianshen.com%2Farticle%2F60037664%2F',

               'Muhammad Junaid Khalid:https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/'
               ]
__license__ = 'CC BY-NC-ND 4.0 Attribution-NonCommercial-NoDerivatives 4.0 International'
__version__ = '0.0.3'
__maintainer__ = 'M. Lebbink'
__email__ = 'mlebbink@yahoo.com'
__status__ = 'Development'

# todo   1  Investigate decent multi language solution like https://docs.python.org/3/library/gettext.html
# todo   1  Create configuration import/management functions
# todo   1  Create logging functionality
# todo   1  Create database
# todo   1  Import test data

# todo      Check glob valiable for all frames

# idea      Make sql fieldlist configurable
# idea      Replace top button bar with icons

# fix       Currently nothing needs fixing


# System libs
import os
import gettext

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from win32api import GetSystemMetrics                       # win32api is part of pywin32

# Own modules
import functions.main_window as mwd

# External apps
import applications.app_zoom as zoom


def main():
    mwd.main_window()


if __name__ == "__main__":
    main()
