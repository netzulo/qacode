# -*- coding: utf-8 -*-
"""Tests fixtures"""

import pytest
import sys
from qacode.core.bots.bot import Bot
from qacode.utils import settings


sys.dont_write_bytecode = True


@pytest.fixture(scope="session")
def bot():
    CFG = settings(path="qacode/configs/", name="settings.json")
    bot = Bot(**CFG)
    try:
        yield bot
    except Exception as err:
        raise err


@pytest.fixture(scope="session")
def browser():
    CFG = settings(path="qacode/configs/", name="settings.json")
    bot = Bot(**CFG)
    try:
        yield bot.browser_create(bot.config.browsers[0])
    except Exception as err:
        raise err
    finally:
        bot.browsers[0].close()
