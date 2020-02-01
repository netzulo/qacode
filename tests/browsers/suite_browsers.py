# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.bots.bot import Bot
from qacode.core.browsers.browser import Browser
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")

@pytest.mark.dependency(name="bot_browser_create", depends=['bot_create'])
def test_bot_browser_create():
    """TODO: doc method"""
    browser = Browser(**CFG)
    ASSERT.is_instance(browser, Browser)
