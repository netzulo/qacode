# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.pages.page import Page
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="browser_open")
def test_page_browser_open(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    if browser.driver is None:
        browser.open()


@pytest.mark.dependency(name="page_open", depends=["browser_open"])
def test_page_create(browser):
    """TODO: doc method"""
    pytest.skip("WIP")
    cfg = CFG.get('bot').get('pages')[0]
    ASSERT.not_none(cfg)
    page = Page(**cfg)
    ASSERT.is_instance(page, Page)
