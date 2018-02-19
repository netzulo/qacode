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


class TestInfoBotMultiple(TestInfoBot):
    """Tests for class TestInfoBot"""

    def __init__(self, method_name="suite_TestTestInfoBot"):
        """Just call to parent constructor class, see TestTestInfoBot

        Keyword Arguments:
            method_name {str} -- name for test info bot testsuite
                (default: {"suite_TestTestInfoBot"})
        """
        super(TestInfoBotMultiple, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_001_inheritance(self):
        """Testcase: test_001_inheritance"""
        self.log.info("assertIsInstance : unittest.TestCase class inheritance "
                      "it's working")
        self.assertIsInstance(self, TestCase)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_002_instance(self):
        """Testcase: test_002_instance"""
        self.log.info("assertIsInstance : TestInfoBase class inheritance it's "
                      "working")
        self.assertIsInstance(self, TestInfoBot)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_003_bot_instance(self):
        """Testcase: test_003_bot_instance"""
        self.log.info("Check bot instance")
        self.assertIsInstance(self.bot, BotBase)
