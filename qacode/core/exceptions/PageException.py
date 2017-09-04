from qacode.core.exceptions.CoreException import CoreException


class PageException(CoreException):
    def __init__(self, message="Message Exception not defined for PageException class", log=None):
        super(PageException, self).__init__(message,log)
