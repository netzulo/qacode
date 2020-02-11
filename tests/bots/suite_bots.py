# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.bots.bot import Bot
from qacode.core.bots.bot_config import BotConfig
from qacode.core.browsers.browser import Browser
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


@pytest.mark.dependency(name="bot_create")
def test_bot_create():
    """TODO: doc method"""
    bot = Bot(**CFG)
    ASSERT.is_instance(bot, Bot)
    ASSERT.is_instance(bot.browsers, list)
    ASSERT.is_instance(bot.pages, list)
    ASSERT.is_instance(bot.controls, list)
    ASSERT.is_instance(bot.config, BotConfig)
    ASSERT.is_instance(bot.log, Log)


@pytest.mark.dependency(depends=['bot_create'])
def test_bot_browsers():
    """TODO: doc method"""
    cfg_browsers = CFG.get('bot').get('browsers')
    bot = Bot(**CFG)
    ASSERT.equals(len(bot.config.browsers), len(cfg_browsers))
    ASSERT.is_instance(bot.browsers, list)


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
    ASSERT.equals(before + 1, len(bot.browsers))
    ASSERT.equals(browser, bot.browsers[0])


@pytest.mark.dependency(name="bot_browser_create", depends=['bot_create'])
def test_bot_start():
    """TODO: doc method"""
    bot = Bot(**CFG)
    bot.start()
    ASSERT.is_instance(bot.browsers, list)
    ASSERT.equals(len(bot.config.browsers), len(bot.browsers))
    for browser in bot.browsers:
        ASSERT.is_instance(browser, Browser)
