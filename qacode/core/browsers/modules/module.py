# -*- coding: utf-8 -*-
"""TODO"""


class Module(object):
    """TODO: doc class"""

    def __check_not_none__(self, name, value):
        """TODO: doc method"""
        if value is None:
            raise Exception("Not {} provided".format(name))
