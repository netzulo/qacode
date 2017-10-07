# -*- coding: utf-8 -*-
"""Package qacode.core.exceptions"""


from qacode.core.exceptions.CoreException import CoreException


class ControlException(CoreException):
    """ControlBase and inherit classes can use this exception"""

    def __init__(
            self,
            err=None,
            message="Message Exception not defined for ControlException class",
            log=None
    ):
        super(ControlException, self).__init__(err=err, message=message, log=log)
