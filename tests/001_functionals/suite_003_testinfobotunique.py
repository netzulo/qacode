# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.testing.test_info import TestInfoBotUnique
from qatestlink.core.testlink_manager import TLManager
from qautils.files import settings


SETTINGS = settings(file_path="qacode/configs/")
SKIP_BOT_UNIQUE = SETTINGS['tests']['skip']['bot_unique']
SKIP_BOT_UNIQUE_MSG = 'bot_unique DISABLED by config file'


class TestTestInfoBotUnique(TestInfoBotUnique):
    """Testcases for class TestInfoBot"""

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestTestInfoBotUnique, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_BOT_UNIQUE)

    @pytest.mark.parametrize('run_time', [1, 2])
    @pytest.mark.skipIf(SKIP_BOT_UNIQUE, SKIP_BOT_UNIQUE_MSG)
    def test_unique_bot_multiple_tests(self, run_time):
        """TODO: doc method"""
        self.log.debug("TestInfoBotUnique, test='{}'".format(run_time))
        self.assert_is_instance(self, object)
        self.assert_is_instance(self, TestInfoBotUnique)
        self.assert_is_instance(self.log, logging.Logger)
        self.assert_is_instance(self.bot, BotBase)
        self.assert_is_instance(self.tlm, TLManager)
