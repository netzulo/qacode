# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers package"""


import pytest
from qacode.core.browsers.browser import Browser
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")
BROWSERS = CFG.get('bot').get('browsers')
HUB_URL = CFG.get("bot").get("hub_url")
LOG = Log(**CFG.get('log'))


def config():
    """TODO: doc method"""
    cfg = BROWSERS[0]
    cfg.update({"hub_url": HUB_URL})
    return cfg


def browser_close(browser):
    """TODO: doc method"""
    browser.close()


@pytest.mark.dependency(name="browser_create")
@pytest.mark.parametrize("cfg_update", [
    {"mode": "doesnotexist"},
    {"hub_url": "doesnotexist"},
    {"browser": "doesnotexist"},
])
def test_browser_create_raises(cfg_update):
    """TODO: doc method"""
    cfg = config().copy()
    cfg.update()
    with pytest.raises(Exception):
        Browser(LOG, **cfg())


@pytest.mark.dependency(name="browser_open", depends=['browser_create'])
def test_browser_open_raises():
    """TODO: doc method"""
    raise NotImplementedError("WIP: not developed yet")
