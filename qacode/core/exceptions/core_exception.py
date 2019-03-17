# -*- coding: utf-8 -*-
"""Main Exceptions for qacode library"""


from qacode.core.loggers.logger_manager import LoggerManager
from selenium.common.exceptions import WebDriverException


MESSAGE_ERROR_DEFAULT = 'Exception without message'


class CoreException(Exception):
    """Base Exception class for inherit new exceptions on library"""

    log = None
    message = None

    def __init__(self, msg=MESSAGE_ERROR_DEFAULT, err=None, log=None):
        """Raise an exception from any part of qacode package"""
        super(CoreException, self).__init__(err, msg)
        self.msg = "FAILED {}: msg={}".format(
            type(self),
            msg)
        if log is None:
            self.log = LoggerManager().logger
        else:
            self.log = log
        if err is None:
            self.log.error(self.msg)
            return
        if isinstance(err, WebDriverException):
            self.args = err.args
        self.log.error(self.args)
