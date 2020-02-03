# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.browsers.browser import Browser
from qacode.core.browsers.browser_config import BrowserConfig
from qacode.core.browsers.modules.commons import ModuleCommons
from qacode.core.browsers.modules.elements import ModuleElements
from qacode.core.browsers.modules.waits import ModuleWaits
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")
BROWSERS = CFG.get('bot').get('browsers')
HUB_URL = CFG.get("bot").get("hub_url")
LOG = Log(**CFG.get('log'))


def config_browser_remote():
    """TODO: doc method"""
    cfg = BROWSERS[0]
    cfg.update({"hub_url": HUB_URL})
    return cfg


def browser_close(browser):
    """TODO: doc method"""
    browser.close()


@pytest.mark.dependency(name="browser_create")
def test_browser_create():
    """TODO: doc method"""
    browser = Browser(LOG, **config_browser_remote())
    ASSERT.is_instance(browser, Browser)
    ASSERT.is_instance(browser.config, BrowserConfig)
    ASSERT.not_none(browser.capabilities)
    if browser.config.browser not in ("iexplorer", "edge", "opera"):
        ASSERT.not_none(browser.options)


@pytest.mark.dependency(name="browser_open", depends=['browser_create'])
def test_browser_open():
    """TODO: doc method"""
    browser = Browser(LOG, **config_browser_remote())
    browser.open()
    ASSERT.not_none(browser.driver)
    ASSERT.is_instance(browser.session_id, str)
    ASSERT.not_none(browser._driver_wait)
    ASSERT.not_none(browser._driver_actions)
    ASSERT.not_none(browser._driver_touch)
    ASSERT.equals(browser.Commons, ModuleCommons)
    ASSERT.equals(browser.Elements, ModuleElements)
    ASSERT.equals(browser.Waits, ModuleWaits)
    browser_close(browser)


@pytest.mark.dependency(name="browser_close", depends=['browser_open'])
def test_browser_close():
    """TODO: doc method"""
    browser = Browser(LOG, **config_browser_remote())
    browser.open()
    browser.close()
    ASSERT.none(browser.driver)
    ASSERT.none(browser._driver_wait)
    ASSERT.none(browser._driver_actions)
    ASSERT.none(browser._driver_touch)
    ASSERT.none(browser.modules)
