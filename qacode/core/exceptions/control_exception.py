# -*- coding: utf-8 -*-
"""Package qacode.core.exceptions"""


from qacode.core.exceptions.core_exception import CoreException


NOT_MSG_CONTROL = "Message Exception not defined for ControlException class"


class ControlException(CoreException):
    """ControlBase and inherit classes can use this exception"""

    def __init__(self, msg=NOT_MSG_CONTROL, log=None, info_bot=None):
        """Instance ControlException error to raise message from controls"""
        super(ControlException, self).__init__(
            msg=msg, log=log, info_bot=info_bot)
        self.selector = info_bot.get("selector") or ""

    def __str__(self):
        """Representation of class"""
        msg = super(ControlException, self).__str__()
        msg += "selector={}".format(
            self.info_bot.get("selector"))
        return msg
