# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.bots.bot import Bot
from qacode.core.exceptions.bot_error import BotError
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERT = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")


def test_bot_create_raises():
    """TODO: doc method"""
    with pytest.raises(Exception):
        Bot(None)


def test_bot_browser_raises():
    """TODO: doc method"""
    bot = Bot(**CFG)
    with pytest.raises(BotError):
        bot.browser("")


def test_bot_page_raises():
    """TODO: doc method"""
    bot = Bot(**CFG)
    with pytest.raises(BotError):
        bot.page("")
