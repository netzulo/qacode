# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement
from tests.utils import (do_login, setup_input_selectors)


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


def try_click(browser):
    """TODO: doc method"""
    invisible_sel = setup_input_selectors().get("invisible")
    ele = browser.elements.find_wait(invisible_sel)
    try:
        browser.elements.ele_click(ele)
    except Exception:
        pass


@pytest.mark.dependency(name="browser_open")
def test_waits_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()
    do_login(browser)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("timeout", [0])
def test_waits_eleinvisible(browser, timeout):
    """TODO: doc method"""
    selector = setup_input_selectors().get("invisible")
    try_click(browser)
    invisible = browser.waits.ele_invisible(selector, timeout=timeout)
    ASSERT.is_instance(invisible, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("timeout", [0, 1])
def test_waits_elevisible(browser, timeout):
    """TODO: doc method"""
    selector = setup_input_selectors().get("visible")
    ele = browser.elements.find_wait(selector)
    try_click(browser)
    visible = browser.waits.ele_visible(ele, timeout=timeout)
    ASSERT.is_instance(visible, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_eletext(browser):
    """TODO: doc method"""
    selector = setup_input_selectors().get("title")
    try_click(browser)
    ASSERT.true(browser.waits.ele_text(selector, "Buttonss"))


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_elevalue(browser):
    """TODO: doc method"""
    selector = setup_input_selectors().get("invisible")
    try_click(browser)
    ASSERT.true(browser.waits.ele_value(selector, "bad_text"))
