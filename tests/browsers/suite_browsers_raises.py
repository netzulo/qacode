# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers package"""


import pytest
from qacode.core.browsers.browser import Browser
from qacode.core.exceptions.browser_error import BrowserError
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from tests.utils import config_browser


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")
LOG = Log(**CFG.get('log'))


@pytest.mark.parametrize("browser", [("browserinvalidname")])
def test_browser_create_raises(browser):
    """TODO: doc method"""
    with pytest.raises(BrowserError):
        Browser(LOG, **dict(config_browser(), browser=browser))


@pytest.mark.parametrize("mode", ["hola"])
def test_browser_open_raises(mode):
    """TODO: doc method"""
    browser = Browser(LOG, **dict(config_browser(), mode=mode))
    with pytest.raises(BrowserError):
        browser.open()
