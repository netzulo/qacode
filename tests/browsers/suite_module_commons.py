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
CFG = settings(file_path="qacode/configs/", file_name="settings.json")
BROWSERS = CFG.get('bot').get('browsers')
HUB_URL = CFG.get("bot").get("hub_url")
LOG = Log(**CFG.get('log'))


def browser_remote():
    """TODO: doc method"""
    cfg = BROWSERS[0]
    cfg.update({"hub_url": HUB_URL})
    browser = Browser(LOG, **cfg)
    ASSERT.is_instance(browser, Browser)
    return browser


@pytest.mark.dependency(name="browser_create")
def test_mod_common_dummy():
    """TODO: doc method"""
    browser = browser_remote()
    try:
        pytest.fail("WIP: not developed yet")
    except:
        pytest.fail("Failed")
    finally:
        browser.close()
