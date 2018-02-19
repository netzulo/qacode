# -*- coding: utf-8 -*-
"""Testsuite for package testing"""


from unittest import TestCase
from unittest import skipIf
from qacode.core.bots.bot_base import BotBase
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_REMOTES = SETTINGS['tests']['skip']['drivers_remote']
SKIP_REMOTES_MSG = 'drivers_remote DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
BOT = None


class TestInfoBotUnique(TestInfoBot):
    """Tests for class TestInfoBot"""

    @classmethod
    def setUpClass(cls):
        """Set up test suite"""
        global BOT
        if not SKIP_REMOTES:
            BOT = TestInfoBot.bot_open(SETTINGS, LOGGER_MANAGER)

    @classmethod
    def tearDownClass(cls):
        """Tear down test suite"""
        global BOT
        if not SKIP_REMOTES:
            TestInfoBot.bot_close(BOT)

    def __init__(self, method_name="suite_TestTestInfoBotUnique"):
        """Just call to parent constructor class, see TestInfoBase

        Keyword Arguments:
            method_name {str} -- name for test info bot unique testsuite
                (default: {"suite_TestTestInfoBotUnique"})
        """
        super(TestInfoBotUnique, self).__init__(
            method_name, bot=BOT,
        )

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_001_inheritance(self):
        """Testcase: test_001_inheritance"""
        self.log.info(
            "assertIsInstance : TestCase class inheritance "
            "it's working")
        self.assertIsInstance(self, TestCase)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_002_instance(self):
        """Testcase: test_002_instance"""
        self.log.info(
            "assertIsInstance : TestInfoBase class inheritance it's "
            "working")
        self.assertIsInstance(self, TestInfoBot)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_003_bot_instance(self):
        """Testcase: test_003_bot_instance"""
        self.log.info("Check bot instance")
        self.assertIsInstance(self.bot, BotBase)
