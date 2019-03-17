# -*- coding: utf-8 -*-
"""Package qacode.core.exceptions"""


from qacode.core.exceptions.core_exception import CoreException


MESSAGE_ERROR_DEFAULT_CONTROL = ("Message Exception not defined "
                                 "for ControlException class")


class ControlException(CoreException):
    """ControlBase and inherit classes can use this exception"""

    def __init__(self, msg=MESSAGE_ERROR_DEFAULT_CONTROL, err=None, log=None):
        """Instance ControlException error to raise message from controls"""
        super(ControlException, self).__init__(msg=msg, err=err, log=log)
