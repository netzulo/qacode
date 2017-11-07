# -*- coding: utf-8 -*-
"""Testsuite for package testing"""


import unittest
from qacode.core.bots.BotBase import BotBase
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.utils.Utils import settings

LOGGER_MANAGER = LoggerManager()
SETTINGS = settings()
BOT = None

class TestInfoBotUnique(TestInfoBot):
    """Tests for class TestInfoBot"""

    @classmethod
    def setUpClass(cls):
        global BOT
        BOT = TestInfoBot.bot_open(SETTINGS, LOGGER_MANAGER)
    @classmethod
    def tearDownClass(cls):
        global BOT
        TestInfoBot.bot_close(BOT)

    def __init__(self, method_name="TestTestInfoBotUnique"):
        super(TestInfoBotUnique, self).__init__(
            method_name, bot=BOT)

    def test_001_inheritance(self):
        """Testcase: test_001_inheritance"""
        self.log.info("assertIsInstance : unittest.TestCase class inheritance "
                      "it's working")
        self.assertIsInstance(self, unittest.TestCase)

    def test_002_instance(self):
        """Testcase: test_002_instance"""
        self.log.info("assertIsInstance : TestInfoBase class inheritance it's "
                      "working")
        self.assertIsInstance(self, TestInfoBot)

    def test_003_bot_instance(self):
        """Testcase: test_003_bot_instance"""
        self.log.info("Check bot instance")
        self.assertIsInstance(self.bot, BotBase)
