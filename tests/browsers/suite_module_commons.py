# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers package"""


import pytest
from qacode.core.browsers.browser import Browser
from qacode.core.browsers.browser_config import BrowserConfig
from qacode.core.browsers.modules.commons import ModuleCommons
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()


def test_common_geturl(browser, url):
    """TODO: doc method"""
    browser.open()
    ASSERT.not_none(browser.Commons.get_url(
        browser.driver,
        "http://netzulo.tk:89"))

def test_common_gettitle(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.Commons.get_title(browser.driver))

