# -*- coding: utf-8 -*-
"""Test Suite module for tests.browsers package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_browser_open(browser):
    """TODO: doc method"""
    browser.open()


@pytest.mark.dependency(depends=['browser_open'])
def test_common_getmaximizewindow(browser):
    """TODO: doc method"""
    browser.Commons.get_maximize_window(browser.driver)


@pytest.mark.dependency(depends=['browser_open'])
def test_common_gettitle(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.Commons.get_title(browser.driver))


@pytest.mark.dependency(depends=['browser_open'])
def test_common_getwindowhandle(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.Commons.get_window_handle(browser.driver))


@pytest.mark.dependency(depends=['browser_open'])
def test_common_getcapabilities(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.Commons.get_capabilities(browser.driver))


@pytest.mark.dependency(depends=['browser_open'])
def test_common_forward(browser):
    """TODO: doc method"""
    browser.Commons.forward(browser.driver)


@pytest.mark.dependency(depends=['browser_open'])
def test_common_reload(browser):
    """TODO: doc method"""
    browser.Commons.reload(browser.driver)


@pytest.mark.dependency(name="get_url", depends=['browser_open'])
@pytest.mark.parametrize("wait", [0, 100])
def test_common_geturl(browser, wait):
    """TODO: doc method"""
    cfg_url = CFG.get('bot').get('pages')[0].get('url')
    ASSERT.not_none(cfg_url)
    browser.Commons.get_url(browser.driver, cfg_url, wait_for_load=wait)


@pytest.mark.dependency(depends=['browser_open', 'get_url'])
def test_common_getcurrenturl(browser):
    """TODO: doc method"""
    cfg_url = CFG.get('bot').get('pages')[0].get('url')
    ASSERT.not_none(cfg_url)
    url = browser.Commons.get_current_url(browser.driver)
    ASSERT.equals(url, cfg_url)


@pytest.mark.dependency(depends=['browser_open', 'get_url'])
@pytest.mark.parametrize("expected", [False, True])
def test_common_isurl(browser, expected):
    """TODO: doc method"""
    cfg_url = None
    if expected:
        cfg_url = CFG.get('bot').get('pages')[0].get('url')
    _is = browser.Commons.is_url(browser.driver, cfg_url)
    ASSERT.equals(_is, expected)


@pytest.mark.dependency(depends=['browser_open', 'get_url'])
@pytest.mark.parametrize(
    "log", [None, 'browser', 'driver', 'client', 'server'])
def test_getlog_lognames(browser, log):
    """Testcase: test_getlog_lognames"""
    if not log:
        with pytest.raises(Exception):
            logs = browser.Commons.get_log(browser.driver, log_name=log)
        return True
    logs = browser.Commons.get_log(browser.driver, log_name=log)
    ASSERT.not_none(logs)
    ASSERT.is_instance(logs, list)


@pytest.mark.dependency(depends=['browser_open'])
def test_common_setwindowsize(browser):
    """TODO: doc method"""
    browser.Commons.set_window_size(browser.driver)
