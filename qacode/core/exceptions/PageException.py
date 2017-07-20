from qacode.core.exceptions.CoreException import CoreException


class PageException(CoreException):
    def __init__(self, cause, message, logger=None):
        super(PageException, self).__init__(cause, message,logger)
