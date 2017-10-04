# -*- coding: utf-8 -*-
"""Testsuite for package testing"""


import unittest
from qacode.core.bots.BotBase import BotBase
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.testing.TestInfoBot import TestInfoBot

LOGGER_MANAGER = LoggerManager()


class TestTestInfoBot(TestInfoBot):
    """Tests for class TestInfoBot"""

    def __init__(self, method_name="TestTestInfoBot"):
        super(TestTestInfoBot, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER
        )

    def test_001_inheritance(self):
        """Testcase: test_001_inheritance"""
        self.assertIsInstance(self, unittest.TestCase)
        self.log.info("assertIsInstance : unittest.TestCase class inheritance "
                      "it's working")
        self.assertIsInstance(self, TestInfoBot)
        self.log.info("assertIsInstance : TestInfoBase class inheritance it's "
                      "working")

    def test_002_dummy_test(self):
        """Testcase: test_002_dummy_test"""
        self.log.info("dummy test to check setup and teardown methods")
        self.assertIsInstance(self.bot, BotBase)
