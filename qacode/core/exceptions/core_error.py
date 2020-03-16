# -*- coding: utf-8 -*-
"""Main Exceptions for qacode library"""


class CoreError(Exception):
    """Base Exception class for inherit new exceptions on library"""

    def __init__(self, message):
        """Allow to handle Qacode and/or Selenium exceptions

        Arguments:
            message {str} -- Exception message
        """
        self._message = message

    @property
    def message(self):
        """GET for 'message' property"""
        return self._message
