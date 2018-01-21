# -*- coding: utf-8 -*-
""""TODO: doc module"""


from enum import Enum


class HtmlAttr(Enum):
    """TODO: doc class"""

    ID = 'id'
    CLASS = 'class'
    NAME = 'name'
    FOR = 'for'

    @classmethod
    def get_attr(cls):
        """return enum values"""
        return [item.value for item in HtmlAttr]

    @classmethod
    def has_attr(cls, value):
        """returns True if enum have value"""
        return any(value == item.value for item in cls)
