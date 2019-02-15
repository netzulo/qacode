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
        return [name for name, member in cls.__members__.items()]

    @classmethod
    def has_property(cls, value):
        """Returns True if enum have value"""
        return cls(value)
