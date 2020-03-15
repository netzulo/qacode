# -*- coding: utf-8 -*-
"""Test Suite module for qacode.core.bots package"""


import pytest
from qacode.core.exceptions.bot_error import BotError
from qacode.core.loggers.log import Log
from qacode.core.testing.asserts import Assert
from qacode.utils import settings


ASSERTS = Assert()
CFG = settings(path="qacode/configs/", name="settings.json")
LOG = Log(**CFG.get('log'))


@pytest.mark.parametrize("message", ["Failed bot"])
def test_bot_error(bot, message):
    """TODO: doc method"""
    exception = BotError(message, bot)
    ASSERTS.in_list(message, exception.message)
    with pytest.raises(BotError):
        raise exception
