from qacode.core.exceptions.CoreException import CoreException


class ModelException(CoreException):
    def __init__(self, cause, message):
        super(ModelException, self).__init__(cause, message)
