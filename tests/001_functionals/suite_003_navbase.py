# -*- coding: utf-8 -*-
"""Package for suites and tests related to bots.modules package"""


from unittest import skipIf
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_REMOTES = SETTINGS['tests']['skip']['drivers_remote']
SKIP_REMOTES_MSG = 'drivers_remote DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
BOT = None


class TestNavBase(TestInfoBot):
    """Test Suite for class NavBase"""

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

    def __init__(self, method_name="suite_TestNavBase"):
        """Test what probes NavBase class and methods

        Keyword Arguments:
            method_name {str} -- name for test nav base
                (default: {"suite_TestNavBase"})
        """
        super(TestNavBase, self).__init__(
            method_name=method_name,
            bot=BOT
        )

    def setUp(self):
        """Test setup"""
        super(TestNavBase, self).setUp()
        self.url = SETTINGS['tests']['unitaries']['url']

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_000_navbase_instance(self):
        """Testcase: test_000_navbase_instance"""
        assert isinstance(self.bot.navigation, NavBase) is True

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_001_gourl_without_waits(self):
        """Testcase: test_001_gourl_without_waitsparam"""
        self.bot.navigation.get_url(self.url)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_002_gourl_with_waitsparam(self):
        """Testcase: test_002_gourl_with_waitsparam"""
        self.bot.navigation.get_url(self.url, wait_for_load=0)

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_003_getmaximizewindow(self):
        """Testcase: test_003_getmaximizewindow"""
        self.bot.navigation.get_maximize_window()

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_004_getcapabilities(self):
        """Testcase: test_004_getcapabilities"""
        caps = self.bot.navigation.get_capabilities()
        self.assert_is_instance(caps, dict)
        self.assert_is_instance(caps['chrome'], dict)
        self.assertEqual(caps['browserName'], 'chrome')

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_005_getlog(self):
        """Testcase: test_005_getlog"""
        self.bot.navigation.get_url(self.url)
        log_data = self.bot.navigation.get_log()
        self.assertIsNotNone(log_data)
        self.log.debug("selenium logs, browser={}".format(log_data))

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_006_getlog_browser(self):
        """Testcase: test_006_getlog_browser"""
        self.bot.navigation.get_url(self.url)
        log_data = self.bot.navigation.get_log(log_name='browser')
        self.assertIsNotNone(log_data)
        self.log.debug("selenium logs, browser={}".format(log_data))

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_007_getlog_driver(self):
        """Testcase: test_007_getlog_driver"""
        self.bot.navigation.get_url(self.url)
        log_data = self.bot.navigation.get_log(log_name='driver')
        self.assertIsNotNone(log_data)
        self.log.debug("selenium logs, driver={}".format(log_data))

    @skipIf(True, 'Issue opened on github selenium, waiting...')
    def test_008_getlog_client(self):
        """Testcase: test_008_getlog_client
        https://github.com/SeleniumHQ/selenium/issues/5410
        """
        self.bot.navigation.get_url(self.url)
        log_data = self.bot.navigation.get_log(log_name='client')
        self.assertIsNotNone(log_data)
        self.log.debug("selenium logs, client={}".format(log_data))

    @skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_009_getlog_server(self):
        """Testcase: test_008_getlog_client"""
        self.bot.navigation.get_url(self.url)
        log_data = self.bot.navigation.get_log(log_name='server')
        self.assertIsNotNone(log_data)
        self.log.debug("selenium logs, server={}".format(log_data))
