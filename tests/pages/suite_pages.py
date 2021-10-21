# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.pages.page import Page
from qacode.core.pages.page_config import PageConfig
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_page_browser_open(browser):
    """TODO: doc method"""
    if browser.driver is None:
        browser.open()


@pytest.mark.dependency(name="page_open", depends=["browser_open"])
def test_page_create(browser):
    """TODO: doc method"""
    cfg = CFG.get('bot').get('pages')[0]
    ASSERT.not_none(cfg)
    page = Page(browser, **cfg)
    ASSERT.is_instance(page, Page)
    ASSERT.is_instance(page.config, PageConfig)
    ASSERT.is_instance(page.config.name, str)
    ASSERT.is_instance(page.config.url, str)


@pytest.mark.dependency(name="page_gourl", depends=["browser_open"])
def test_page_gourl(browser):
    """TODO: doc method"""
    cfg = CFG.get('bot').get('pages')[0]
    ASSERT.not_none(cfg)
    page = Page(browser, **cfg)
    page.go_url(wait=3)


@pytest.mark.dependency(name="page_open", depends=["browser_open"])
def test_page_isurl(browser):
    """TODO: doc method"""
    cfg = CFG.get('bot').get('pages')[0]
    ASSERT.not_none(cfg)
    page = Page(browser, **cfg)
    page.go_url(wait=3)
    page.is_url()
