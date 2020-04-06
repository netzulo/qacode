# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBot
from qacode.utils import settings
from qatestlink.core.testlink_manager import TLManager


ASSERT = Assert()
SETTINGS = settings(file_path="qacode/configs/")
SKIP_BOT_MULTIPLE = SETTINGS['tests']['skip']['bot_multiple']
SKIP_BOT_MULTIPLE_MSG = 'bot_multiple DISABLED by config file'


class TestTestInfoBot(TestInfoBot):
    """Testcases for class TestInfoBot"""

    def setup_method(self, test_method):
        """Setup class (suite) to be executed"""
        super(TestTestInfoBot, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    @pytest.mark.parametrize('run_time', [1, 2])
    @pytest.mark.skipIf(SKIP_BOT_MULTIPLE, SKIP_BOT_MULTIPLE_MSG)
    def test_multiple_bots(self, run_time):
        """Testcase: test_multiple_bots"""
        self.log.debug("TestInfoBotUnique, test='{}'".format(run_time))
        ASSERT.is_instance(self, object)
        ASSERT.is_instance(self, TestInfoBot)
        ASSERT.is_instance(self.log._logger, logging.Logger)
        ASSERT.is_instance(self.bot, BotBase)
        ASSERT.is_instance(self.config, dict)
        ASSERT.is_instance(self.tlm, TLManager)
