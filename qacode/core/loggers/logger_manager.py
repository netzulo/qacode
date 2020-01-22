# -*- coding: utf-8 -*-
"""Module related with all logging tasks"""


from logging import (
    FileHandler, Formatter, INFO, StreamHandler, getLogger)


class Log(object):
    """Manager for logger"""

    # ATTRIBUTES
    _name = None
    _path = None
    _level = None
    _formatter = None
    _logger = None

    def __init__(self, *args, **kwargs):
        """TODO: doc method"""
        self._name = kwargs.get('log_name') or "qacode"
        self._path = kwargs.get('log_path') or 'logs/{}.log'.format(self._name)
        self._level = kwargs.get('log_level') or INFO

        self._formatter = Formatter(
            ("[pid:%(process)d][%(asctime)s][%(name)s]"
             "[%(levelname)s]: %(message)s"))
        self._handlers = self.__handlers__() or {}
        self.__logger__()

    def __logger__(self):
        """TODO: doc method"""
        self._logger = getLogger(self._name)
        self._logger.setLevel(self._level)
        # Remove handlers added to logging module
        for old_handler in self._logger.handlers:
            self._logger.removeHandler(old_handler)
        # Add new handlers
        if not self._logger.handlers:
            self._logger.addHandler(self._handlers['console'])
            self._logger.addHandler(self._handlers['file'])

    def __handlers__(self):
        """TODO: doc method"""
        handlers = [StreamHandler(), FileHandler(self._path)]
        for handler in handlers:
            handler.setFormatter(self._formatter)
            handler.setLevel(self._level)
        return {
            "console": handlers[0],
            "file": handlers[1],
        }

    # PUBLIC METHODS

    def debug(self, msg):
        """TODO: doc method"""
        self._logger.debug(msg)

    def info(self, msg):
        """TODO: doc method"""
        self._logger.info(msg)

    def warning(self, msg):
        """TODO: doc method"""
        self._logger.warning(msg)

    def error(self, msg):
        """TODO: doc method"""
        self._logger.warning(msg)
