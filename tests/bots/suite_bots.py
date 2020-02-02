# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.bots.bot import Bot
from qacode.core.browsers.browser import Browser
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(file_path="qacode/configs/", file_name="settings.json")


@pytest.mark.dependency(name="bot_create")
def test_bot_create():
    """TODO: doc method"""
    bot = Bot(**CFG)
    ASSERT.is_instance(bot, Bot)


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_browsers():
    """TODO: doc method"""
    pytest.fail("Not developed yet")


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_pages():
    """TODO: doc method"""
    pytest.fail("Not developed yet")


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_controls():
    """TODO: doc method"""
    pytest.fail("Not developed yet")


@pytest.mark.dependency(name="bot_browser_create", depends=['bot_create'])
def test_bot_browser_create():
    """TODO: doc method"""
    bot = Bot(**CFG)
    browser = bot.browser_create(bot.config.browsers[0])
    ASSERT.is_instance(browser, Browser)
