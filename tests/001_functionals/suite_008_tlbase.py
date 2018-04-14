# -*- coding: utf-8 -*-
"""Package qacode.core.testing.testlink"""


import pytest
from qacode.core.testing.test_info import TestInfoBase
from qacode.core.utils import settings


SETTINGS = settings()


class TestTlBase(TestInfoBase):
    """Test Suite for class TlBase"""

    @pytest.mark.skipIf(True, "Functionality it's not working yet")
    def test_001_instance(self):
        """Test: test_001_instance"""
        pytest.skip(msg="Functionality it's not working yet")
