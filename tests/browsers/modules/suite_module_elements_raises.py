# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.common.by import By


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
@pytest.mark.parametrize("selector, locator", [("invalid", None)])
def test_elements_find_raises(browser, selector, locator):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Elements.find(browser.driver, selector, locator=locator)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("selector, locator", [
    ("invalid", None), ("invalid", By.CSS_SELECTOR)
])
def test_elements_finds_raises(browser, selector, locator):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Elements.finds(browser.driver, selector, locator=locator)
