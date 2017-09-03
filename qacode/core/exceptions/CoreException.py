import logging
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.loggers.LoggerManager import LoggerManager


class CoreException(Exception):
    log = None

    def __init__(self, cause, message, log=None):
        if log is None:
            self.log = LoggerManager().get_log()
        else:
            self.log = log
        self.log.error("Error at core class: cause={} , message={}".format(cause, message))
