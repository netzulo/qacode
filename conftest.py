# -*- coding: utf-8 -*-
"""Tests fixtures"""

import pytest
from qacode.core.bots.bot import Bot
from qacode.utils import settings


@pytest.fixture(scope="session")
def browser():
    CFG = settings(file_path="qacode/configs/", file_name="settings.json")
    bot = Bot(**CFG)
    try:
        yield bot.browser_create(bot.config.browsers[0])
    except Exception as err:
        raise err
    finally:
        bot.browsers[0].close()
