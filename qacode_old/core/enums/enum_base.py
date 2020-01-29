# -*- coding: utf-8 -*-
"""package qacode.core.enums.enum_base"""


from enum import Enum


class EnumBase(Enum):
    """Enum Class with base methods to be used
        at inherit classes
    """

    @classmethod
    def get_properties(cls):
        """Return enum values"""
        return list(cls.__members__.keys())

    @classmethod
    def has_property(cls, value):
        """Returns True if enum have value"""
        try:
            cls(value)
        except ValueError:
            return False
        else:
            return True
