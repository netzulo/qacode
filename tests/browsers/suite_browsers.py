# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers package"""


import pytest
from qacode.core.browsers.browser import Browser
from qacode.core.browsers.browser_config import BrowserConfig
from qacode.core.browsers.modules.commons import ModuleCommons
from qacode.core.browsers.modules.elements import ModuleElements
from qacode.core.browsers.modules.js import ModuleJs
from qacode.core.browsers.modules.screenshots import ModuleScreenshots
from qacode.core.browsers.modules.waits import ModuleWaits
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from tests.utils import config_browser


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")
LOG = Log(**CFG.get('log'))


def browser_close(browser):
    """TODO: doc method"""
    browser.close()


@pytest.mark.dependency(name="browser_create")
def test_browser_create():
    """TODO: doc method"""
    browser = Browser(LOG, **config_browser())
    ASSERT.is_instance(browser, Browser)
    ASSERT.is_instance(browser.config, BrowserConfig)
    ASSERT.not_none(browser.capabilities)
    ASSERT.not_none(browser.driver_abs_path)
    if browser.config.browser not in ("iexplorer", "edge", "opera"):
        ASSERT.not_none(browser.options)


@pytest.mark.dependency(name="browser_open", depends=['browser_create'])
@pytest.mark.parametrize("mode", ["remote"])
def test_browser_open(mode):
    """TODO: doc method"""
    browser = Browser(LOG, **dict(config_browser(), mode=mode))
    browser.open()
    ASSERT.not_none(browser.driver)
    ASSERT.is_instance(browser.session_id, str)
    ASSERT.not_none(browser._driver_wait)
    ASSERT.not_none(browser._driver_actions)
    ASSERT.not_none(browser._driver_touch)
    ASSERT.is_instance(browser.commons, ModuleCommons)
    ASSERT.is_instance(browser.elements, ModuleElements)
    ASSERT.is_instance(browser.screenshots, ModuleScreenshots)
    ASSERT.is_instance(browser.waits, ModuleWaits)
    ASSERT.is_instance(browser.js, ModuleJs)
    browser_close(browser)


@pytest.mark.dependency(name="browser_close", depends=['browser_open'])
def test_browser_close():
    """TODO: doc method"""
    browser = Browser(LOG, **config_browser())
    browser.open()
    browser.close()
    ASSERT.none(browser.driver)
    ASSERT.none(browser._driver_wait)
    ASSERT.none(browser._driver_actions)
    ASSERT.none(browser._driver_touch)
    ASSERT.none(browser.commons)
    ASSERT.none(browser.elements)
    ASSERT.none(browser.screenshots)
    ASSERT.none(browser.waits)
    ASSERT.none(browser.js)
