# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.controls.control import Control
from qacode.core.controls.control_config import ControlConfig
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement
from tests.utils import (do_login, menu_left, setup_controls, try_click)


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
    dict(CFG.get('bot').get('controls')[6], search=True),
    dict(CFG.get('bot').get('controls')[6], search=True, timeout=1)
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
    cfg = dict(setup_controls()["title"], search=True)
    ctl = Control(browser, **cfg)
    ASSERT.is_instance(ctl.attr("id"), str)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_attrvalue(browser):
    """TODO: doc method"""
    cfg = dict(setup_controls()["title"], search=True)
    ctl = Control(browser, **cfg)
    ASSERT.is_instance(ctl.attr_value("id"), str)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_css(browser):
    """TODO: doc method"""
    cfg = dict(setup_controls()["title"], search=True)
    ctl = Control(browser, **cfg)
    ASSERT.is_instance(ctl.css("background-color"), str)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_clear(browser):
    """TODO: doc method"""
    cfg = dict(setup_controls()["input_text"], search=True)
    ctl = Control(browser, **cfg)
    ctl.clear()


@pytest.mark.dependency(depends=["browser_open"])
@pytest.mark.parametrize("clear", [False, True])
def test_control_typetext(browser, clear):
    """TODO: doc method"""
    cfg = dict(setup_controls()["input_text"], search=True)
    ctl = Control(browser, **cfg)
    ctl.type_text("text", clear=clear)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_click(browser):
    """TODO: doc method"""
    cfg = dict(setup_controls()["input_text"], search=True)
    ctl = Control(browser, **cfg)
    ctl.click()


@pytest.mark.dependency(name="wait_invisible", depends=["browser_open"])
def test_control_waitinvisible(browser):
    """TODO: doc method"""
    cfg = dict(setup_controls()["invisible"], search=True)
    ctl = Control(browser, **cfg)
    try_click(browser)
    ctl.wait_invisible(timeout=0)


@pytest.mark.dependency(depends=["browser_open", "wait_invisible"])
def test_control_waitvisible(browser):
    """TODO: doc method"""
    cfg = dict(setup_controls()["visible"], search=True)
    ctl = Control(browser, **cfg)
    try_click(browser)
    ctl.wait_visible()


@pytest.mark.dependency(depends=["browser_open"])
@pytest.mark.parametrize("ctl_name, expected", [
    ("title", "Buttonss"), ("invisible", "bad_text")])
def test_control_waittext(browser, ctl_name, expected):
    """TODO: doc method"""
    cfg = dict(setup_controls()[ctl_name], search=True)
    ctl = Control(browser, **cfg)
    try_click(browser)
    ctl.wait_text(expected, timeout=7)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_waitblink(browser):
    """TODO: doc method"""
    do_login(browser)
    cfg = dict(setup_controls()["invisible"], search=True)
    ctl = Control(browser, **cfg)
    try_click(browser)
    ctl.wait_blink(to_invisible=7, to_visible=8)


@pytest.mark.dependency(depends=["browser_open"])
def test_control_reload(browser):
    """TODO: doc method"""
    # 1. confirmar una recarga sobre un elemento
    #   que no la necesita (no estancando)
    # cfg = dict(setup_controls()["title"], search=True)
    # ctl = Control(browser, **cfg)
    # ctl.reload()
    # 2. confirmar un reload en un cambio de pagina con una modificacion
    #   de parte de la misma sobre un selector que exista en ambas
    do_login(browser)
    menu_left(browser, "login")
    ele_h4 = Control(browser, **{"selector": ".alert-heading", "search": True})
    menu_left(browser, "logout")
    ele_h4.reload()
    ele_h4.click()
    # 3. confirmar un reload en un hijo
