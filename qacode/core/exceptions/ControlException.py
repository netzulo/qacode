from qacode.core.exceptions.CoreException import CoreException


class ControlException(CoreException):
    def __init__(self, cause, message):
        super(ControlException, self).__init__(cause, message)
