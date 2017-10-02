# -*- coding: utf-8 -*-
"""TODO"""


import unittest

import time

from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.utils.Utils import settings


LOGGER_MANAGER = LoggerManager()
CONFIG = settings()


class TestBotBase(TestInfoBase):
    """Tests for class BotBase"""

    def __init__(self, method_name="TestBotBase"):
        super(TestBotBase, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER
        )

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support local drivers")
    def test_001_bot_local_chrome(self):
        """Testcase: test_001_bot_local_chrome"""
        self.log.debug("TestBotBase: LOCAL started for CHROME")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "chrome"
        bot_config.bot_mode = "local"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for CHROME")

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support local drivers")
    def test_002_bot_local_firefox(self):
        """Testcase: test_002_bot_local_firefox"""
        self.log.debug("TestBotBase: LOCAL started for FIREFOX")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "firefox"
        bot_config.bot_mode = "local"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for FIREFOX")

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support local drivers")
    def test_003_bot_local_phantomjs(self):
        """Testcase: test_003_bot_local_phantomjs"""
        self.log.debug("TestBotBase: LOCAL started for PHANTOMJS")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "phantomjs"
        bot_config.bot_mode = "local"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for PHANTOMJS")

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support local drivers")
    def test_004_bot_local_iexplorer(self):
        """Testcase: test_004_bot_local_iexplorer"""
        self.log.debug("TestBotBase: LOCAL started for IEXPLORER")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "iexplorer"
        bot_config.bot_mode = "local"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for IEXPLORER")

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support local drivers")
    def test_005_bot_local_edge(self):
        """Testcase: test_005_bot_local_edge"""
        self.log.debug("TestBotBase: LOCAL started for EDGE")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "edge"
        bot_config.bot_mode = "local"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for EDGE")

    def test_006_bot_remote_chrome(self):
        """Testcase: test_006_bot_remote_chrome"""
        self.log.debug("TestBotBase: REMOTE started for CHROME")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "chrome"
        bot_config.bot_mode = "remote"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for CHROME")

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support remote firefox drivers")
    def test_007_bot_remote_firefox(self):
        """Testcase: test_007_bot_remote_firefox"""
        self.log.debug("TestBotBase: REMOTE started for FIREFOX")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "firefox"
        bot_config.bot_mode = "remote"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for FIREFOX")

    def test_008_bot_remote_phantomjs(self):
        """Testcase: test_008_bot_remote_phantomjs"""
        self.log.debug("TestBotBase: REMOTE started for PHANTOMJS")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "phantomjs"
        bot_config.bot_mode = "remote"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for PHANTOMJS")

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support remote windows drivers")
    def test_009_bot_remote_iexplorer(self):
        """Testcase: test_009_bot_remote_iexplorer"""
        self.log.debug("TestBotBase: REMOTE started for IEXPLORER")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "iexplorer"
        bot_config.bot_mode = "remote"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for IEXPLORER")

    @unittest.skipIf(CONFIG["BUILD"]["skip_travis_tests"],
                     "TRAVIS build not support remote windows drivers")
    def test_010_bot_remote_edge(self):
        """Testcase: test_010_bot_remote_edge"""
        self.log.debug("TestBotBase: REMOTE started for EDGE")
        bot_config = BotConfig(nose_config=self.test_config,
                               logger_manager=self.logger_manager)
        bot_config.bot_browser = "edge"
        bot_config.bot_mode = "remote"
        bot = BotBase(bot_config)
        time.sleep(10)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for EDGE")
