# -*- coding: utf-8 -*-
"""Main Exceptions for qacode library"""


from qacode.core.loggers.LoggerManager import LoggerManager


class CoreException(Exception):
    """Base Exception class for inherit new exceptions on library"""
    log = None

    def __init__(self, err=None, message='Exception without message', log=None):
        """Raise an exception from any part of qacode package"""
        super(CoreException, self).__init__(err, message)
        msg = "FAILED qacode.core: message={}"
        if log is None:
            self.log = LoggerManager().get_log()
        else:
            self.log = log
        self.log.error(str(msg.format(message)))
