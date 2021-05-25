# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.exceptions.browser_error import BrowserError
from qacode.core.testing.asserts import Assert


ASSERTS = Assert()


@pytest.mark.parametrize("message", ["Failed browser"])
def test_browser_error(browser, message):
    """TODO: doc method"""
    exception = BrowserError(message, browser)
    ASSERTS.in_list(message, exception.message)
    with pytest.raises(BrowserError):
        raise exception
