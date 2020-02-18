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
    ASSERT.is_instance(browser.screenshots.as_base64(), str)


@pytest.mark.dependency(depends=['browser_open'])
def test_screenshot_asfile(browser):
    """TODO: doc method"""
    ASSERT.true(browser.screenshots.as_file("qacode.jpg"))


@pytest.mark.dependency(depends=['browser_open'])
def test_screenshot_aspng(browser):
    """TODO: doc method"""
    ASSERT.is_instance(browser.screenshots.as_png(), bytes)


@pytest.mark.dependency(depends=['browser_open'])
def test_screenshot_save(browser):
    """TODO: doc method"""
    ASSERT.true(browser.screenshots.save("qacode.jpeg"))
