# -*- coding: utf-8 -*-
"""Package qacode.core.testing.testlink"""


import pytest
from qacode.core.testing.test_info import TestInfoBase
from qautils.files import settings


SETTINGS = settings(file_path="qacode/configs/")


class TestTlBase(TestInfoBase):
    """Test Suite for class TlBase"""

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestTlBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    @pytest.mark.skipIf(True, "Functionality it's not working yet")
    def test_001_instance(self):
        """Test: test_001_instance"""
        pytest.skip(msg="Functionality it's not working yet")
