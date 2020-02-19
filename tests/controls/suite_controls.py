# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.controls.control import Control
from qacode.core.controls.control_config import ControlConfig
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement
from tests.utils import do_login


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_control_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()
    do_login(browser)


@pytest.mark.dependency(name="control_create", depends=["browser_open"])
@pytest.mark.parametrize("cfg", [
    CFG.get('bot').get('controls')[0],
    dict(CFG.get('bot').get('controls')[6], search=True)
])
def test_control_create(browser, cfg):
    """TODO: doc method"""
    ASSERT.not_none(cfg)
    ctl = Control(browser, **cfg)
    ASSERT.is_instance(ctl, Control)
    ASSERT.is_instance(ctl.config, ControlConfig)
    ASSERT.is_instance(ctl.config.name, str)
    ASSERT.is_instance(ctl.config.selector, str)
    ASSERT.is_instance(ctl.config.locator, str)
    ASSERT.is_instance(ctl.config.search, bool)
    ASSERT.is_instance(ctl.config.pages, list)
    for page in ctl.config.pages:
        ASSERT.is_instance(page, str)
    if cfg.get("search"):
        ASSERT.is_instance(ctl._element, WebElement)
