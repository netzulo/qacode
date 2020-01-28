# -*- coding: utf-8 -*-
"""Main Exceptions for qacode library"""


from qacode.core.loggers.logger_manager import Log
from selenium.common.exceptions import WebDriverException


NOT_MSG = 'Exception without message'


class CoreException(Exception):
    """Base Exception class for inherit new exceptions on library"""

    def __init__(self, msg=NOT_MSG, log=None, info_bot=None):
        """Allow to handle Qacode and/or Selenium exceptions

        Keyword Arguments:
            msg {str} -- Exception message (default: {NOT_MSG})
            log {Log} -- Logging class (default: {None})
            info_bot {dict} -- Qacode+Selenium information (default: {None})
        """
        self.is_just_msg = False
        self.msg = msg
        if info_bot is None:
            info_bot = {}
            self.is_just_msg = True
        self.info_bot = info_bot
        self.browser = self.info_bot.get("browser") or ""
        self.mode = self.info_bot.get("mode") or ""
        self.method = self.info_bot.get("method") or ""
        self.err = info_bot.get("err") or {}
        if log is None:
            self.log = Log()
        else:
            self.log = log
        self.log.error(str(self))

    def __str__(self):
        """Representation of class"""
        msg = ""
        if self.is_just_msg:
            return self.msg
        msg += " | "
        msg += "browser='{}' ".format(self.browser)
        msg += "mode='{}' ".format(self.mode)
        msg += "method='{}' ".format(self.method)
        if self.err is None:
            return msg
        if isinstance(self.err, WebDriverException):
            msg += "{}{} - args='{}'".format(
                "Selenium error: ", type(self.err), self.err.args)
        return "{}".format(msg)
