# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers.modules package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_commons_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()


@pytest.mark.dependency(depends=['browser_open'])
def test_common_getmaximizewindow(browser):
    """TODO: doc method"""
    browser.commons.get_maximize_window()


@pytest.mark.dependency(depends=['browser_open'])
def test_common_gettitle(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.commons.get_title())


@pytest.mark.dependency(depends=['browser_open'])
def test_common_getwindowhandle(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.commons.get_window_handle())


@pytest.mark.dependency(depends=['browser_open'])
def test_common_getcapabilities(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.commons.get_capabilities())


@pytest.mark.dependency(depends=['browser_open'])
def test_common_forward(browser):
    """TODO: doc method"""
    browser.commons.forward()


@pytest.mark.dependency(depends=['browser_open'])
def test_common_reload(browser):
    """TODO: doc method"""
    browser.commons.reload()


@pytest.mark.dependency(name="get_url", depends=['browser_open'])
@pytest.mark.parametrize("wait", [0, 100])
def test_common_geturl(browser, wait):
    """TODO: doc method"""
    cfg_url = CFG.get('bot').get('pages')[0].get('url')
    ASSERT.not_none(cfg_url)
    browser.commons.get_url(cfg_url, wait=wait)


@pytest.mark.dependency(depends=['browser_open', 'get_url'])
def test_common_getcurrenturl(browser):
    """TODO: doc method"""
    cfg_url = CFG.get('bot').get('pages')[0].get('url')
    ASSERT.not_none(cfg_url)
    url = browser.commons.get_current_url()
    ASSERT.equals(url, cfg_url)


@pytest.mark.dependency(depends=['browser_open', 'get_url'])
@pytest.mark.parametrize("expected", [False, True])
def test_common_isurl(browser, expected):
    """TODO: doc method"""
    cfg_url = None
    if expected:
        cfg_url = CFG.get('bot').get('pages')[0].get('url')
    _is = browser.commons.is_url(cfg_url)
    ASSERT.equals(_is, expected)


@pytest.mark.dependency(depends=['browser_open', 'get_url'])
@pytest.mark.parametrize(
    "log", [None, 'browser', 'driver', 'client', 'server'])
def test_getlog_lognames(browser, log):
    """Testcase: test_getlog_lognames"""
    if not log:
        with pytest.raises(Exception):
            logs = browser.commons.get_log(log_name=log)
        return True
    logs = browser.commons.get_log(log_name=log)
    ASSERT.not_none(logs)
    ASSERT.is_instance(logs, list)


@pytest.mark.dependency(depends=['browser_open'])
def test_common_setwindowsize(browser):
    """TODO: doc method"""
    browser.commons.set_window_size()


@pytest.mark.dependency(depends=['browser_open'])
def test_common_executejs(browser):
    """TODO: doc method"""
    ele = browser.commons.execute_js("return document.querySelector('body')")
    ASSERT.not_none(ele)


@pytest.mark.dependency(depends=['browser_open'])
@pytest.mark.parametrize("css_important", [False, True])
def test_common_setcssrule(browser, css_important):
    """TODO: doc method"""
    browser.commons.set_css_rule(
        "body", "background", "1px red solid",
        **{"css_important": css_important})
