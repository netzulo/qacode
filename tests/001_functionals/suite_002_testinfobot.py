# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.testing.test_info import TestInfoBot


class TestTestInfoBot(TestInfoBot):
    """Testcases for class TestInfoBot"""

    def test_001_inheritance(self):
        """Test: test_001_inheritance"""
        self.assert_is_instance(self, object)
        self.assert_is_instance(self, TestInfoBot)
        self.assert_is_instance(self.log, logging.Logger)

    @pytest.mark.parametrize('run_time', [1, 2, 3])
    def test_002_multiple_bots(self, run_time):
        """TODO: doc method"""
        self.log.debug(
            "Starting bot number '{}'".format(
                run_time))
        self.assert_is_instance(
            self.bot, BotBase)
