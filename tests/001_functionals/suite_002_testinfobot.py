# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.testing.test_info import TestInfoBot


class TestTestInfoBot(TestInfoBot):
    """Testcases for class TestInfoBot"""

    @pytest.mark.parametrize('run_time', [0, 1, 2])
    def test_multiple_bots(self, run_time):
        self.log.debug(
            "Starting bot number '{}'".format(
                run_time))
        self.assert_is_instance(
            self.bot, BotBase)
