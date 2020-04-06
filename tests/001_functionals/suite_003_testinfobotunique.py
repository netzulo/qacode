# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.utils import settings
from qatestlink.core.testlink_manager import TLManager


ASSERT = Assert()
SETTINGS = settings(file_path="qacode/configs/")
SKIP_BOT_UNIQUE = SETTINGS['tests']['skip']['bot_unique']
SKIP_BOT_UNIQUE_MSG = 'bot_unique DISABLED by config file'


class TestTestInfoBotUnique(TestInfoBotUnique):
    """Testcases for class TestInfoBot"""

    @classmethod
    def setup_class(cls, **kwargs):
        """Setup class (suite) to be executed"""
        super(TestTestInfoBotUnique, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_BOT_UNIQUE)

    @pytest.mark.parametrize('run_time', [1, 2])
    @pytest.mark.skipIf(SKIP_BOT_UNIQUE, SKIP_BOT_UNIQUE_MSG)
    def test_unique_bot_multiple_tests(self, run_time):
        """Testcase: test_unique_bot_multiple_tests"""
        self.log.debug("TestInfoBotUnique, test='{}'".format(run_time))
        ASSERT.is_instance(self, object)
        ASSERT.is_instance(self, TestInfoBotUnique)
        ASSERT.is_instance(self.log._logger, logging.Logger)
        ASSERT.is_instance(self.bot, BotBase)
        ASSERT.is_instance(self.tlm, TLManager)
