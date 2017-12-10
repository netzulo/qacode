# -*- coding: utf-8 -*-
"""Package for suites and tests related to bots.modules package"""


from unittest import skipIf
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.utils import settings


LOGGER_MANAGER = LoggerManager()
SETTINGS = settings()
SKIP_REMOTES = SETTINGS['tests']['skip']['drivers_remote']
SKIP_REMOTES_MSG = 'drivers_remote DISABLED by config file'


class TestNavBase(TestInfoBot):
    """Test Suite for class NavBase"""

    def __init__(self, method_name="TestNavBase"):
        """Test what probes NavBase class and methods"""
        super(TestNavBase, self).__init__(
            method_name=method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )

    def setUp(self):
        """Test setup"""
        super(TestNavBase, self).setUp()
        self.url = self.test_config['tests']['unitaries']['url']

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
