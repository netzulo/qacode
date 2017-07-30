import logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager


class CoreException(Exception):
    def __init__(self, cause, message, logger_manager=None):
        if logger_manager is None:
            self.logger_manager = LoggerManager()
        self.log = self.logger_manager.get_log()
        self.log.error("Error core: cause=%s , message=%s", cause, message)
