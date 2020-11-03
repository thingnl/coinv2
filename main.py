__author__ = 'M. Lebbink'
__copyright__ = 'Copyright 2020, Pecuniae Collectio'
__credits__ = ['Treeview sorting:'
               'https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u='
               'https%3A%2F%2Fwww.pianshen.com%2Farticle%2F60037664%2F',
               ]
__license__ = 'GNU GENERAL PUBLIC LICENSE v3'
__version__ = '2.0.1'
__maintainer__ = 'M. Lebbink'
__email__ = 'mlebbink@yahoo.com'
__status__ = 'Development'


# System libs
import os
import subprocess

# Own modules
import functions.main_window as mwd

# External apps
import applications.app_zoom as zoom


def main():
    mwd.main_window()


if __name__ == "__main__":
    main()
