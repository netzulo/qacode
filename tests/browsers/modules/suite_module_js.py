# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_js_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()


@pytest.mark.dependency(depends=['browser_open'])
def test_js_executejs(browser):
    """TODO: doc method"""
    ele = browser.js.execute_js("return document.querySelector('body')")
    ASSERT.not_none(ele)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("css_important", [False, True])
def test_js_setcssrule(browser, css_important):
    """TODO: doc method"""
    browser.js.set_css_rule(
        "body", "background", "1px red solid",
        **{"css_important": css_important})
