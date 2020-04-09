# -*- coding: utf-8 -*-
"""Main Exceptions for qacode.bot classes"""


from qacode.core.exceptions.core_error import CoreError


class ControlError(CoreError):
    """TODO: doc class"""

    def __init__(self, message, control):
        """TODO: doc method"""
        self._message = "{} [at control: {}]".format(message, str(control))
        super(ControlError, self).__init__(self._message)
