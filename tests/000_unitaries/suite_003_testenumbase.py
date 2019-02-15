# -*- coding: utf-8 -*-
"""Test Suite module for enums package"""


import logging
import pytest
from qacode.core.testing.test_info import TestInfoBase
from qacode.core.enums.enum_base import EnumBase
from qautils.files import settings

class TestEnum(EnumBase):
            ONE = 1
            TWO = 2

class TestTestInfoBase(TestInfoBase):
    """Testcases for class TestInfoBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestTestInfoBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))
        t = TestEnum(1)
        self.add_property("test_enum", t)
        self.add_property("test_values", ['ONE', 'TWO'])

    def test_001_enums_instance(self):
        """Test: test_001_enums_instance"""
        self.assert_is_instance(self.test_enum, EnumBase)
        self.assert_is_instance(self.test_enum, TestEnum)

    def test_002_enums_hasproperty(self):
        """Test: test_002_enums_hasproperty"""
        value = 1
        e = self.test_enum.has_property(value)
        self.assert_not_none(e)
        self.assert_in(str(e.name), self.test_values)
        self.assert_equals(e.value, value)

    def test_003_enums_getproperties(self):
        """Test: test_003_enums_getproperties"""
        e = self.test_enum.has_property(1)
        self.assert_equals(len(e.get_properties()), 2)
        for prop in e.get_properties():
            self.assert_in(prop, self.test_values)
