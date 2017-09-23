from qacode.core.exceptions.CoreException import CoreException


class ControlException(object):
    """ControlBase and inherit classes can use this exception"""    

    def __init__(self, message="Message Exception not defined for ControlException class", log=None):
        super(ControlException, self).__init__(message,log)