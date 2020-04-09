# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.exceptions.control_error import ControlError
from qacode.core.testing.asserts import Assert


ASSERTS = Assert()


@pytest.mark.parametrize("message", ["Failed control"])
def test_core_error(message):
    """TODO: doc method"""
    exception = ControlError(message)
    ASSERTS.equals(exception.message, message)
    with pytest.raises(ControlError):
        raise exception
