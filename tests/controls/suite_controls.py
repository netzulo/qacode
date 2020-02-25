# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.controls.control import Control
from qacode.core.controls.control_config import ControlConfig
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement
from tests.utils import (do_login, setup_controls)


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
    if not cfg.get("search"):
        ASSERT.none(ctl._element)
        ASSERT.none(ctl._id)
        return True
    # checks just when searched
    ASSERT.is_instance(ctl._element, WebElement)
    ASSERT.is_instance(ctl._id, str)
    ASSERT.is_instance(ctl.id, str)
    ASSERT.is_instance(ctl.text, str)
    ASSERT.is_instance(ctl.is_displayed, bool)
    ASSERT.is_instance(ctl.is_enabled, bool)
    ASSERT.is_instance(ctl.is_selected, bool)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_attr(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = dict(setup_controls()["title"], search=True)
    ctl = Control(browser, **cfg)
    ASSERT.is_instance(ctl.attr("id"), str)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_attrvalue(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["title"]
    ctl = Control(browser, **cfg)
    ASSERT.is_instance(ctl.attr_value("id"), str)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_css(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["title"]
    ctl = Control(browser, **cfg)
    ASSERT.is_instance(ctl.css("background-color"), str)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_clear(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["invisible"]
    ctl = Control(browser, **cfg)
    ctl.clear()


@pytest.mark.dependency(depends=["browser_open"])
def test_control_typetext(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["invisible"]
    ctl = Control(browser, **cfg)
    ctl.type_text("text")


@pytest.mark.dependency(depends=["browser_open"])
def test_control_click(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["invisible"]
    ctl = Control(browser, **cfg)
    ctl.click()


@pytest.mark.dependency(depends=["browser_open"])
def test_control_waitinvisible(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["invisible"]
    ctl = Control(browser, **cfg)
    ctl.wait_invisible()


@pytest.mark.dependency(depends=["browser_open"])
def test_control_waitvisible(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["invisible"]
    ctl = Control(browser, **cfg)
    ctl.wait_visible()


@pytest.mark.dependency(depends=["browser_open"])
def test_control_waittext(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["invisible"]
    ctl = Control(browser, **cfg)
    ctl.wait_text()


@pytest.mark.dependency(depends=["browser_open"])
def test_control_waitblink(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = setup_controls()["invisible"]
    ctl = Control(browser, **cfg)
    ctl.wait_blink()
