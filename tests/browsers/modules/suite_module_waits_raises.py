# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from tests.utils import (do_login, setup_input_selectors)


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_waits_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()
    do_login(browser)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("selector, locator, timeout", [
    ("invalid", None, 1), ("invalid", "css selector", 1)])
def test_elements_findwait_raises(browser, selector, locator, timeout):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.waits.find_wait(selector, locator=locator, timeout=timeout)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("selector, locator, timeout", [
    ("invalid", None, 1), ("invalid", "css selector", 1)])
def test_elements_findswait_raises(browser, selector, locator, timeout):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.waits.finds_wait(
            selector, locator=locator, timeout=timeout)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("timeout", [0, 1])
def test_waits_eleinvisible_raises(browser, timeout):
    """TODO: doc method"""
    selector = None
    if timeout:
        selector = setup_input_selectors().get("invisible")
    with pytest.raises(Exception):
        browser.waits.ele_invisible(selector, timeout=timeout)


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_elevisible(browser):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.waits.ele_visible(None)


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_eletext(browser):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.waits.ele_text(None, "")


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_elevalue(browser):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.waits.ele_value(None, "bad_text")
