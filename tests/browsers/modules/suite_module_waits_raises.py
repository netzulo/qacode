# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from tests.utils import do_login


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_waits_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()
    do_login(browser)


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_eleinvisible_raises(browser):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Waits.ele_invisible(browser._driver_wait, None)


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_elevisible(browser):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Waits.ele_visible(browser._driver_wait, None)


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_eletext(browser):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Waits.ele_text(browser._driver_wait, None, "")


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_elevalue(browser):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Waits.ele_value(browser._driver_wait, None, "bad_text")
