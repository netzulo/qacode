# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.browsers.browser import Browser
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


@pytest.mark.dependency(name="browser_create")
def test_browser_create():
    """TODO: doc method"""
    browser = Browser(LOG, **config_browser_remote())
    ASSERT.is_instance(browser, Browser)


@pytest.mark.dependency(name="browser_open", depends=['browser_create'])
def test_browser_open():
    """TODO: doc method"""
    browser = Browser(LOG, **config_browser_remote())
    browser.open()
