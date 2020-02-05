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


@pytest.mark.dependency(depends=['browser_open'])
def test_common_gettitle(browser):
    """TODO: doc method"""
    ASSERT.not_none(browser.Commons.get_title(browser.driver))
