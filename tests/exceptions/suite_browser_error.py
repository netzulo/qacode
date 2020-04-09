# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.exceptions.browser_error import BrowserError
from qacode.core.testing.asserts import Assert


ASSERTS = Assert()


@pytest.mark.parametrize("message", ["Failed browser"])
def test_core_error(message):
    """TODO: doc method"""
    exception = BrowserError(message)
    ASSERTS.equals(exception.message, message)
    with pytest.raises(BrowserError):
        raise exception
