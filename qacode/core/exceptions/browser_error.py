# -*- coding: utf-8 -*-
"""Main Exceptions for qacode.bot classes"""


from qacode.core.exceptions.core_error import CoreError


class BrowserError(CoreError):
    """TODO: doc class"""

    def __init__(self, message, bot):
        """TODO: doc method"""
        self._message = "{} [at browser: {}]".format(message, str(bot))
        super(BrowserError, self).__init__(self._message)
