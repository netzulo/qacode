# -*- coding: utf-8 -*-
"""Tests fixtures"""

import pytest
import sys
from qacode.core.bots.bot_base import BotBase
from qacode.utils import settings


sys.dont_write_bytecode = True


@pytest.fixture(scope="session")
def browser():
    CFG = settings(file_path="qacode/configs/", file_name="settings.json")
    bot = None
    try:
        bot = BotBase(**CFG)
        yield bot
    except Exception as err:
        raise err
    finally:
        if bot:
            bot.close()
