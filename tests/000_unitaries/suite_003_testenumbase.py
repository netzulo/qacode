# -*- coding: utf-8 -*-
"""Test Suite module for enums package"""


from qacode.core.enums.enum_base import EnumBase
from qacode.core.testing.test_info import TestInfoBase
from qautils.files import settings


class TestEnum(EnumBase):
    """Example class for this test package"""

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
        self.assert_true(self.test_enum.has_property(1))

    def test_003_enums_hasntproperty(self):
        """Test: test_003_enums_hasntproperty"""
        self.assert_false(self.test_enum.has_property(3))

    def test_004_enums_getproperties(self):
        """Test: test_004_enums_getproperties"""
        self.assert_equals(
            self.test_enum.get_properties(),
            self.test_values)
