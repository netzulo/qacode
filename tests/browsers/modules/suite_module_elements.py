# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement
from tests.utils import setup_selectors


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_elements_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()
    cfg_url = CFG.get('bot').get('pages')[0].get('url')
    ASSERT.not_none(cfg_url)
    browser.commons.get_url(cfg_url)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_find(browser):
    """TODO: doc method"""
    selector = setup_selectors().get('parent')
    element = browser.elements.find(selector)
    ASSERT.is_instance(element, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_finds(browser):
    """TODO: doc method"""
    _selector = CFG.get('bot').get('controls')[0].get('selector')
    selector = "{}{}".format(_selector, " input")
    ASSERT.is_instance(selector, str)
    ASSERT.greater(len(selector), 0, "invalid empty selector")
    elements = browser.elements.finds(selector)
    ASSERT.is_instance(elements, list)
    for element in elements:
        ASSERT.is_instance(element, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_findwait(browser):
    """TODO: doc method"""
    selector = setup_selectors().get('parent')
    element = browser.elements.find_wait(selector)
    ASSERT.is_instance(element, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_findswait(browser):
    """TODO: doc method"""
    selector = "{}{}".format(setup_selectors().get('parent'), " input")
    elements = browser.elements.finds_wait(selector)
    ASSERT.is_instance(elements, list)
    for element in elements:
        ASSERT.is_instance(element, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_findchild(browser):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('parent'))
    ASSERT.is_instance(element, WebElement)
    child = browser.elements.find_child(element, selectors.get('child'))
    ASSERT.is_instance(child, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_findchildren(browser):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('parent'))
    ASSERT.is_instance(element, WebElement)
    children = browser.elements.find_children(
        element, selectors.get('children'))
    ASSERT.is_instance(children, list)
    for child in children:
        ASSERT.is_instance(child, WebElement)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_eleclick(browser):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    ele = browser.elements.ele_click(element)
    ASSERT.equals(element, ele)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("text", [None, "write_something"])
def test_elements_elewrite(browser, text):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    ele = browser.elements.ele_write(element, text=text)
    ASSERT.equals(element, ele)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("attr_name", ["id"])
def test_elements_eleattribute(browser, attr_name):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    attr = browser.elements.ele_attr(element, attr_name)
    ASSERT.is_instance(attr, str)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("attr_name", ["id"])
def test_elements_eleinputvalue(browser, attr_name):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    attr_value = browser.elements.ele_input_value(element)
    ASSERT.is_instance(attr_value, str)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("attr_name", ["id"])
def test_elements_eleclear(browser, attr_name):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    browser.elements.ele_clear(element)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_elecss(browser):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    css_property = browser.elements.ele_css(element, "margin")
    ASSERT.is_instance(css_property, str)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_eleisdisplayed(browser):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    ASSERT.is_instance(element, WebElement)
    ASSERT.is_instance(browser.elements.ele_is_displayed(element), bool)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_eleisenabled(browser):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    ASSERT.is_instance(element, WebElement)
    ASSERT.is_instance(browser.elements.ele_is_enabled(element), bool)


@pytest.mark.dependency(depends=['browser_open'])
def test_elements_eleisselected(browser):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    ASSERT.is_instance(element, WebElement)
    ASSERT.is_instance(browser.elements.ele_is_selected(element), bool)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("attr_name", ["id"])
def test_elements_eleattrvalue(browser, attr_name):
    """TODO: doc method"""
    selectors = setup_selectors()
    element = browser.elements.find(selectors.get('child'))
    ASSERT.is_instance(element, WebElement)
    ASSERT.is_instance(
        browser.elements.ele_attr_value(element, attr_name), str)
