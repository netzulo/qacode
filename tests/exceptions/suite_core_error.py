# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.exceptions.core_error import CoreError
from qacode.core.testing.asserts import Assert


ASSERTS = Assert()


@pytest.mark.parametrize("message", ["Failed core"])
def test_core_error(message):
    """TODO: doc method"""
    exception = CoreError(message)
    ASSERTS.equals(exception.message, message)
    with pytest.raises(CoreError):
        raise exception
