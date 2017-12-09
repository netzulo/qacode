# -*- coding: utf-8 -*-
"""Package qacode.core.exceptions"""

from qacode.core.exceptions.core_exception import CoreException


class PageException(CoreException):
    """Exception class that can be raise from Page classes"""

    def __init__(self, err=None, message='Raised PageException', log=None):
        """This exception must be raised from PageBase or inherit classes"""
        super(PageException, self).__init__(err=err,
                                            message=message,
                                            log=log)
