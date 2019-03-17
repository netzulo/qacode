# -*- coding: utf-8 -*-
"""Package qacode.core.exceptions"""

from qacode.core.exceptions.core_exception import CoreException


MESSAGE_ERROR_DEFAULT_PAGE = ("Message Exception not defined "
                              "for PageException class")


class PageException(CoreException):
    """Exception class that can be raise from Page classes"""

    def __init__(self, msg=MESSAGE_ERROR_DEFAULT_PAGE, err=None, log=None):
        """This exception must be raised from PageBase or inherit classes"""
        super(PageException, self).__init__(msg=msg, err=err, log=log)
