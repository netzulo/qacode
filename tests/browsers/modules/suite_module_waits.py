# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_waits_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_eleinvisible(browser):
    """TODO: doc method"""
    # browser.Waits.ele_invisible(browser._driver_wait)
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_elevisible(browser):
    """TODO: doc method"""
    # browser.Waits.ele_visible(browser._driver_wait)
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_eletext(browser):
    """TODO: doc method"""
    # browser.Waits.ele_text(browser._driver_wait)
    raise NotImplementedError("WIP: not developed yet")


@pytest.mark.dependency(depends=['browser_open'])
def test_waits_elevalue(browser):
    """TODO: doc method"""
    # browser.Waits.ele_value(browser._driver_wait)
    raise NotImplementedError("WIP: not developed yet")
