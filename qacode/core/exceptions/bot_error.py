# -*- coding: utf-8 -*-
"""Main Exceptions for qacode.bot classes"""


from qacode.core.exceptions.core_error import CoreError


class BotError(CoreError):
    """TODO: doc class"""

    def __init__(self, message, bot):
        """TODO: doc method"""
        self._message = "{} [at bot: {}]".format(message, str(bot))
        super(BotError, self).__init__(self._message)
