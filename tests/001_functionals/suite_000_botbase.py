# -*- coding: utf-8 -*-
"""Testsuite for package bots"""


from unittest import skipIf
from qacode.core.bots.bot_base import BotBase
from qacode.core.bots.bot_config import BotConfig
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_base import TestInfoBase
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_LOCALS = SETTINGS['tests']['skip']['drivers_local']
SKIP_LOCALS_MSG = 'drivers_local DISABLED by config file'
SKIP_REMOTES = SETTINGS['tests']['skip']['drivers_remote']
SKIP_REMOTES_MSG = 'drivers_remote DISABLED by config file'
# TODO: must be setteable from config JSON
WAIT_TO_CLOSE = int(3)
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestBotBase(TestInfoBase):
    """Testcases for class BotBase"""

    def __init__(self, method_name='suite_TestBotBase'):
        """Just call to parent constructor class, see TestInfoBase

        Keyword Arguments:
            method_name {str} -- name for test info base testsuite
                (default: {"suite_TestBotBase"})
        """
        super(TestBotBase, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )

    def setUp(self):
        """Testcases setup"""
        self.bot_config = BotConfig(
            config=self.test_config,
            logger_manager=self.logger_manager)

    @skipIf(SKIP_LOCALS, SKIP_LOCALS_MSG)
    def test_001_bot_local_chrome(self):
        """Testcase: test_001_bot_local_chrome"""
        self.log.debug('TestBotBase: LOCAL started for CHROME')
        self.bot_config.config['browser'] = 'chrome'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'chrome')
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for CHROME")

    @skipIf(SKIP_LOCALS, SKIP_LOCALS_MSG)
    def test_002_bot_local_firefox(self):
        """Testcase: test_002_bot_local_firefox"""
        self.log.debug("TestBotBase: LOCAL started for FIREFOX")
        self.bot_config.config['browser'] = 'firefox'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'firefox')
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for FIREFOX")

    @skipIf(SKIP_LOCALS, SKIP_LOCALS_MSG)
    def test_003_bot_local_phantomjs(self):
        """Testcase: test_003_bot_local_phantomjs"""
        self.log.debug("TestBotBase: LOCAL started for PHANTOMJS")
        self.bot_config.config['browser'] = 'phantomjs'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'phantomjs')
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for PHANTOMJS")

    @skipIf(SKIP_LOCALS, SKIP_LOCALS_MSG)
    def test_004_bot_local_iexplorer(self):
        """Testcase: test_004_bot_local_iexplorer"""
        self.log.debug("TestBotBase: LOCAL started for IEXPLORER")
        self.bot_config.config['browser'] = 'iexplorer'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'internet explorer')
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for IEXPLORER")

    @skipIf(True, "Need to setup on my local before to run this test again")
    def test_005_bot_local_edge(self):
        """Testcase: test_005_bot_local_edge"""
        self.log.debug("TestBotBase: LOCAL started for EDGE")
        self.bot_config.config['browser'] = 'edge'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'MicrosoftEdge')
        bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for EDGE")

    @skipIf(True, 'Issue opened on official opera chromium github')
    def test_006_bot_local_opera(self):
        """Testcase: test_006_bot_local_opera

        ISSUE OPENED :
         https://github.com/operasoftware/operachromiumdriver/issues/9
        """
        self.log.debug("TestBotBase: REMOTE started for OPERA")
        self.bot_config.config['browser'] = 'opera'
        self.bot_config.config['mode'] = 'local'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'opera')
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for OPERA")

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_007_bot_remote_chrome(self):
        """Testcase: test_007_bot_remote_chrome"""
        self.log.debug("TestBotBase: REMOTE started for CHROME")
        self.bot_config.config['browser'] = 'chrome'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        self.assertEqual(bot.curr_caps['browserName'], 'chrome')
        self.timer(wait=WAIT_TO_CLOSE)
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for CHROME")

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_008_bot_remote_firefox(self):
        """Testcase: test_008_bot_remote_firefox"""
        self.log.debug("TestBotBase: REMOTE started for FIREFOX")
        self.bot_config.config['browser'] = 'firefox'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'firefox')
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for FIREFOX")

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_009_bot_remote_phantomjs(self):
        """Testcase: test_009_bot_remote_phantomjs"""
        self.log.debug("TestBotBase: REMOTE started for PHANTOMJS")
        self.bot_config.config['browser'] = "phantomjs"
        self.bot_config.config['mode'] = "remote"
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'phantomjs')
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for PHANTOMJS")

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_010_bot_remote_iexplorer(self):
        """Testcase: test_010_bot_remote_iexplorer"""
        self.log.debug("TestBotBase: REMOTE started for IEXPLORER")
        self.bot_config.config['browser'] = 'iexplorer'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'internet explorer')
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for IEXPLORER")

    @skipIf(True, 'Still not public node with edge support')
    def test_011_bot_remote_edge(self):
        """Testcase: test_011_bot_remote_edge"""
        self.log.debug("TestBotBase: REMOTE started for EDGE")
        self.bot_config.config['browser'] = 'edge'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'MicrosoftEdge')
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for EDGE")

    @skipIf(True, 'Issue opened on official opera chromium github')
    def test_012_bot_remote_opera(self):
        """Testcase: test_012_bot_remote_opera

        ISSUE OPENED :
         https://github.com/operasoftware/operachromiumdriver/issues/9
        """
        self.log.debug("TestBotBase: REMOTE started for OPERA")
        self.bot_config.config['browser'] = 'opera'
        self.bot_config.config['mode'] = 'remote'
        bot = BotBase(self.bot_config)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assertEqual(bot.curr_caps['browserName'], 'opera')
        bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for OPERA")

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_013_raises_botconfig_noneconfig(self):
        """Testcase: test_013_raises_botconfig_noneconfig"""
        self.assertRaises(
            CoreException,
            BotConfig,
            None,
            self.logger_manager)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_014_raises_bot_nonebotconfig(self):
        """Testcase: test_014_raises_bot_nonebotconfig"""
        self.assertRaises(
            CoreException,
            BotBase,
            None)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_015_raises_botconfig_nonekeybot(self):
        """Testcase: test_015_raises_botconfig_nonekeybot"""
        config = self.test_config.copy()
        config.pop('bot', None)
        self.assertRaises(
            CoreException,
            BotConfig,
            config,
            self.logger_manager)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_016_raises_botconfig_nonelogger(self):
        """Testcase: test_016_raises_botconfig_nonelogger"""
        self.assertRaises(
            CoreException,
            BotConfig,
            self.test_config,
            None)
