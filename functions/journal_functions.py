#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
import logging
# import time
from . import glob


def setup_logger(logger_name, log_file, logging_level):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
                                  datefmt='%Y/%m/%d %I:%M:%S')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    # Enable streamHandlers for logging to console
    # streamHandler = logging.StreamHandler()
    # streamHandler.setFormatter(formatter)
    l.setLevel(logging_level)
    l.addHandler(fileHandler)
    # l.addHandler(streamHandler)


def log_new_start():
    glob.logger_main.info('-----------------------')
    glob.logger_main.info('New PC session started.')
    glob.logger_main.debug('System_version = ' + glob.system_version)
    glob.logger_main.debug('System_build = ' + glob.system_build)
    glob.logger_main.debug('System_sql = ' + glob.system_sql)

    glob.logger_sql.info('-----------------------')
    glob.logger_sql.info('New PC session started.')
    glob.logger_sql.debug('System_version = ' + glob.system_version)
    glob.logger_sql.debug('System_build = ' + glob.system_build)
    glob.logger_sql.debug('System_sql = ' + glob.system_sql)
