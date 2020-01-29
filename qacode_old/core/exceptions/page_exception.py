# -*- coding: utf-8 -*-
"""Package qacode.core.exceptions"""

from qacode.core.exceptions.core_exception import CoreException


NOT_MSG_PAGE = "Message Exception not defined for PageException class"


class PageException(CoreException):
    """Exception class that can be raise from Page classes"""

    def __init__(self, msg=NOT_MSG_PAGE, log=None, info_bot=None):
        """This exception must be raised from PageBase or inherit classes"""
        self.url = info_bot.get("url") or ""
        super(PageException, self).__init__(
            msg=msg, log=log, info_bot=info_bot)

    def __str__(self):
        """Representation of class"""
        return self.msg_info_bot(self.info_bot)

    def msg_info_bot(self, info_bot):
        """Generate str message from param 'info_bot'"""
        msg = super(PageException, self).msg_info_bot(info_bot)
        msg += "url='{}' ".format(self.url)
        return msg
