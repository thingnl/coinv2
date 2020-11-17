#!/usr/bin/env python
# -*- coding: utf-8 -*-

# System libs
# import os
import logging
# import time
from . import glob


def setup_logger(logger_name, log_file, logging_level):
    """ Starts a logger in mode 'append'

    Args:
        logger_name: string: logger name
        log_file: string: filename including path
        logging_level: string: INFO, DEBUG or NOTSET

    Returns:
        Returns nothing, put's message directly on screen.
    """
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
                                  datefmt='%Y/%m/%d %I:%M:%S')
    filehandler = logging.FileHandler(log_file, mode='a')
    filehandler.setFormatter(formatter)
    # Enable streamHandlers for logging to console
    # streamHandler = logging.StreamHandler()
    # streamHandler.setFormatter(formatter)
    logger.setLevel(logging_level)
    logger.addHandler(filehandler)
    # l.addHandler(streamHandler)


def log_new_start():
    """ Send messages to the logs to inducate a new run. Includes version information.

    Args:

    Returns:
    """
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
