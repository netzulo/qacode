# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.testing.asserts import Assert


ASSERTS = Assert()


@pytest.mark.parametrize("ignore_raises", [True, False])
def test_core_exception(ignore_raises):
    """TODO: doc method"""
    pytest.skip("WIP")
    exception = CoreException("Failed core")
    ASSERTS.equals(exception.msg, "Failed core")
    with pytest.raises(CoreException):
        raise exception()
