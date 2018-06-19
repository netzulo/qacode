# -*- coding: utf-8 -*-
"""Module related with all logging tasks"""


import logging
from qautils.files import path_format


class LoggerManager(object):
    """Manager to instance configurated logger

    @usage: instance.get_log()
    """

    log_path = None
    log_name = None
    log_path_join = None
    log_level = None
    logger = None

    def __init__(self, log_path="logs/", log_name="qacode", log_level=None,
                 is_output_console=True, is_output_file=True):
        """Create new logger_manager instance with default 'logs/qacode.log'
            path, log_level DEBUG console_handler enable file_handler enable
        """
        if log_path is None or len(log_path) <= 0:
            raise Exception("bad format at logger log_path={}"
                            .format(log_path))
        self.log_path = log_path

        if log_name is None or len(log_name) <= 0:
            raise Exception("Log name not provided: log_name={}"
                            .format(log_name))
        self.log_name = log_name

        if log_level is None:
            self.log_level = logging.DEBUG
        else:
            self.log_level = log_level
        if not is_output_console and not is_output_file:
            raise Exception(
                "Can't start LoggerManager without any handler, "
                "is_output_console={} , is_output_file={}"
                .format(is_output_console, is_output_file)
            )
        self.is_output_console = is_output_console
        self.is_output_file = is_output_file
        self.log_path_join = path_format(
            file_path=self.log_path,
            file_name="{}.log".format(self.log_name),
            ignore_raises=True)
        self.logger = self.create_logger()

    def create_logger(self):
        """Generates handlers from logging package"""
        logger = logging.getLogger(self.log_name)
        logger.setLevel(self.log_level)
        self.log_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        for old_handler in logger.handlers:
            logger.removeHandler(old_handler)
        if self.is_output_console:
            logger.addHandler(self.create_console_handler(
                self.log_level, self.log_formatter
            ))
        if self.is_output_file:
            logger.addHandler(self.create_file_handler(
                self.log_level, self.log_formatter, self.log_path_join
            ))
        return logger

    def create_console_handler(self, log_level, log_formatter):
        """Create console handler and set logfile level"""
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(log_formatter)
        return console_handler

    def create_file_handler(self, log_level, log_formatter, log_path_join):
        """Create console handler and set logfile level"""
        file_handler = logging.FileHandler(log_path_join)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(log_formatter)
        return file_handler
