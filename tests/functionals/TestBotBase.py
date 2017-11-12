# -*- coding: utf-8 -*-
"""Testsuite for package bots"""


import unittest

import time

from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.utils.Utils import settings


LOGGER_MANAGER = LoggerManager()
CONFIG = settings()
SKIP = CONFIG['build']['travis']['skip_tests']
WAIT_TO_CLOSE = int(5)

class TestBotBase(TestInfoBase):
    """Testcases for class BotBase"""

    def __init__(self, method_name='TestBotBase'):
        """Just call to parent constructor class, see TestInfoBase"""
        super(TestBotBase, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=CONFIG)

    def setUp(self):
        """Testcases setup"""
        self.bot_config = BotConfig(
            config=self.test_config,
            logger_manager=self.logger_manager)

    @unittest.skipIf(SKIP, 'TRAVIS build not support local drivers')
    def test_001_bot_local_chrome(self):
        """Testcase: test_001_bot_local_chrome"""
        self.log.debug('TestBotBase: LOCAL started for CHROME')
        self.bot_config.config['browser'] = 'chrome'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for CHROME")

    @unittest.skipIf(SKIP, 'TRAVIS build not support local drivers')
    def test_002_bot_local_firefox(self):
        """Testcase: test_002_bot_local_firefox"""
        self.log.debug("TestBotBase: LOCAL started for FIREFOX")
        self.bot_config.config['browser'] = 'firefox'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for FIREFOX")

    @unittest.skipIf(SKIP, 'TRAVIS build not support local drivers')
    def test_003_bot_local_phantomjs(self):
        """Testcase: test_003_bot_local_phantomjs"""
        self.log.debug("TestBotBase: LOCAL started for PHANTOMJS")
        self.bot_config.config['browser'] = 'phantomjs'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for PHANTOMJS")

    @unittest.skipIf(SKIP, 'TRAVIS build not support local drivers')
    def test_004_bot_local_iexplorer(self):
        """Testcase: test_004_bot_local_iexplorer"""
        self.log.debug("TestBotBase: LOCAL started for IEXPLORER")
        self.bot_config.config['browser'] = 'iexplorer'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for IEXPLORER")

    @unittest.skipIf(SKIP, 'TRAVIS build not support local drivers')
    def test_005_bot_local_edge(self):
        """Testcase: test_005_bot_local_edge"""
        self.log.debug("TestBotBase: LOCAL started for EDGE")
        self.bot_config.config['browser'] = 'edge'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for EDGE")

    def test_006_bot_remote_chrome(self):
        """Testcase: test_006_bot_remote_chrome"""
        self.log.debug("TestBotBase: REMOTE started for CHROME")
        self.bot_config.config['browser'] = 'chrome'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for CHROME")

    def test_007_bot_remote_firefox(self):
        """Testcase: test_007_bot_remote_firefox"""
        self.log.debug("TestBotBase: REMOTE started for FIREFOX")
        self.bot_config.config['browser'] = 'firefox'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for FIREFOX")

    def test_008_bot_remote_phantomjs(self):
        """Testcase: test_008_bot_remote_phantomjs"""
        self.log.debug("TestBotBase: REMOTE started for PHANTOMJS")
        self.bot_config.bot_browser = "phantomjs"
        self.bot_config.bot_mode = "remote"
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for PHANTOMJS")

    def test_009_bot_remote_iexplorer(self):
        """Testcase: test_009_bot_remote_iexplorer"""
        self.log.debug("TestBotBase: REMOTE started for IEXPLORER")
        self.bot_config.config['browser'] = 'iexplorer'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for IEXPLORER")

    @unittest.skipIf(SKIP, 'TRAVIS build not support remote windows drivers')
    def test_010_bot_remote_edge(self):
        """Testcase: test_010_bot_remote_edge"""
        self.log.debug("TestBotBase: REMOTE started for EDGE")
        self.bot_config.config['browser'] = 'edge'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        time.sleep(WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for EDGE")
