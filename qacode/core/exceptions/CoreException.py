# -*- coding: utf-8 -*-


from qacode.core.loggers.LoggerManager import LoggerManager


class CoreException(Exception):
    log = None

    def __init__(self, message, log=None):
        if log is None:
            self.log = LoggerManager(log_path="logs").get_log()
        else:
            self.log = log
        self.log.error("FAILED qacode.core: message={}".format(message))
