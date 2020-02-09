# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_elements_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()
    cfg_url = CFG.get('bot').get('pages')[0].get('url')
    ASSERT.not_none(cfg_url)
    browser.Commons.get_url(browser.driver, cfg_url)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_find(browser):
    """TODO: doc method"""
    selector = CFG.get('bot').get('controls')[0].get('selector')
    ASSERT.is_instance(selector, str)
    ASSERT.greater(len(selector), 0, "invalid empty selector")
    element = browser.Elements.find(browser.driver, selector)
    ASSERT.is_instance(element, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_finds(browser):
    """TODO: doc method"""
    _selector = CFG.get('bot').get('controls')[0].get('selector')
    selector = "{}{}".format(_selector, " input")
    ASSERT.is_instance(selector, str)
    ASSERT.greater(len(selector), 0, "invalid empty selector")
    elements = browser.Elements.finds(browser.driver, selector)
    ASSERT.is_instance(elements, list)
    for element in elements:
        ASSERT.is_instance(element, WebElement)
