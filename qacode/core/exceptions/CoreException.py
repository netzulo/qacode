import logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager


class CoreException(Exception):
    def __init__(self, cause, message, loggerManager=None):
        if loggerManager is None:
            self.loggerManager = LoggerManager()
        self.log = self.loggerManager.get_log()
        self.log.error("Error core: cause=%s , message=%s", cause, message)
