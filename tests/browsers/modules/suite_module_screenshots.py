# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_screenshot_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()


@pytest.mark.dependency(depends=['browser_open'])
def test_screenshot_asbase64(browser):
    """TODO: doc method"""
    base64 = browser.Screenshots.as_base64(browser.driver)
    ASSERT.is_instance(base64, str)


@pytest.mark.dependency(depends=['browser_open'])
def test_screenshot_asfile(browser):
    """TODO: doc method"""
    ASSERT.true(browser.Screenshots.as_file(browser.driver, "qacode.jpg"))


@pytest.mark.dependency(depends=['browser_open'])
def test_screenshot_aspng(browser):
    """TODO: doc method"""
    _bytes = browser.Screenshots.as_png(browser.driver)
    ASSERT.is_instance(_bytes, bytes)


@pytest.mark.dependency(depends=['browser_open'])
def test_screenshot_save(browser):
    """TODO: doc method"""
    ASSERT.true(browser.Screenshots.save(browser.driver, "qacode.jpeg"))
