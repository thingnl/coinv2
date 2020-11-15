#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
import time
from . import glob

def write_main_journal_entry(journal_text):
    """ Show message to user at bottom main window.

    Args:
        message_text: string.

    Returns:
        Returns nothing, put's message directly on screen.
    """

    # F:/py-dev/coinv2/logs/system_journal.20201115
    # Open journal, maybe need to change to always open, from start to finish
    if glob.main_journal != "":                       # Skip if journal is not set
        log1 = open(glob.main_journal, "a")
        log1.write(time.strftime("%Y%m%d-%H%M%S - ") + r'%s' % journal_text + '\n')
        log1.close()


def write_sql_journal_entry(sql_text):
    """ Show message to user at bottom main window.

    Args:
        sql_text: string.

    Returns:
        Returns nothing, put's message directly on screen.
    """

    # F:/py-dev/coinv2/logs/sql_journal.20201115
    # Open journal, maybe need to change to always open, from start to finish
    log2 = open(glob.sql_journal, "a")
    log2.write(time.strftime("%Y%m%d-%H%M%S - ") + sql_text + '\n')
    log2.close()
