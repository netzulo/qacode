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
    cfg_browsers = CFG.get('bot').get('browsers')
    ASSERT.equals(len(Bot(**CFG).config.browsers), len(cfg_browsers))


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_pages():
    """TODO: doc method"""
    cfg_pages = CFG.get('bot').get('pages')
    ASSERT.equals(len(Bot(**CFG).config.pages), len(cfg_pages))


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_controls():
    """TODO: doc method"""
    cfg_controls = CFG.get('bot').get('controls')
    ASSERT.equals(len(Bot(**CFG).config.controls), len(cfg_controls))


@pytest.mark.dependency(name="bot_browser_create", depends=['bot_create'])
def test_bot_browser_create():
    """TODO: doc method"""
    bot = Bot(**CFG)
    before = len(bot.browsers)
    browser = bot.browser_create(bot.config.browsers[0])
    ASSERT.is_instance(browser, Browser)
    ASSERT.equals(before+1, len(bot.browsers))
    ASSERT.equals(browser, bot.browsers[0])
