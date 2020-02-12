# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.common.by import By
from tests.utils import setup_selectors


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_elements_raises_browser_open(browser):
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
    ("invalid", None), ("invalid", By.CSS_SELECTOR),
])
def test_elements_finds_raises(browser, selector, locator):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Elements.finds(browser.driver, selector, locator=locator)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("selector, locator", [("invalid", None)])
def test_elements_findwait_raises(browser, selector, locator):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Elements.find_wait(browser.driver, selector, locator=locator)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("selector, locator", [("invalid", None)])
def test_elements_findswait_raises(browser, selector, locator):
    """TODO: doc method"""
    with pytest.raises(Exception):
        browser.Elements.finds_wait(browser.driver, selector, locator=locator)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("parent_sel,child_sel,locator", [
    ("body", "invalid", None)
])
def test_elements_findchild_raises(browser, parent_sel, child_sel, locator):
    """TODO: doc method"""
    element = browser.Elements.find(browser.driver, parent_sel)
    with pytest.raises(Exception):
        browser.Elements.find_child(element, child_sel, locator=locator)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("parent_sel,child_sel,locator", [
    ("body", "invalid", None)
])
def test_elements_findchildren_raises(browser, parent_sel, child_sel, locator):
    """TODO: doc method"""
    element = browser.Elements.find(browser.driver, parent_sel)
    with pytest.raises(Exception):
        browser.Elements.find_children(element, child_sel, locator=locator)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("selector, locator", [("invalid", None)])
def test_elements_findschild_raises(browser, selector, locator):
    """TODO: doc method"""
    with pytest.raises(NotImplementedError):
        browser.Elements.finds_child()


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("selector, locator", [("invalid", None)])
def test_elements_findschildren_raises(browser, selector, locator):
    """TODO: doc method"""
    with pytest.raises(NotImplementedError):
        browser.Elements.finds_children()


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("attr_name", ["doesnotexist"])
def test_elements_eleattribute_raises(browser, attr_name):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.Elements.find(browser.driver, selectors.get('child'))
    with pytest.raises(Exception):
        browser.Elements.ele_attribute(element, attr_name)