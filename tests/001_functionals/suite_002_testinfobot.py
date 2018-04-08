# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.testing.test_info import TestInfoBot
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_BOT_MULTIPLE = SETTINGS['tests']['skip']['bot_multiple']
SKIP_BOT_MULTIPLE_MSG = 'bot_multiple DISABLED by config file'


class TestTestInfoBot(TestInfoBot):
    """Testcases for class TestInfoBot"""

    @pytest.mark.parametrize('run_time', [1, 2])
    @pytest.mark.skipIf(SKIP_BOT_MULTIPLE, SKIP_BOT_MULTIPLE_MSG)
    def test_002_multiple_bots(self, run_time):
        """TODO: doc method"""
        self.log.debug("TestInfoBotUnique, test='{}'".format(run_time))
        self.assert_is_instance(self, object)
        self.assert_is_instance(self, TestInfoBot)
        self.assert_is_instance(self.log, logging.Logger)
        self.assert_is_instance(self.bot, BotBase)
