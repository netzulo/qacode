# -*- coding: utf-8 -*-


from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.bots.modules.NavBase import NavBase


LOGGER_MANAGER = LoggerManager()


class TestNavBase(TestInfoBot):
    """Test Suite for class NavBase"""

    def __init__(self, method_name="TestNavBase"):
        super(TestNavBase, self).__init__(
            method_name=method_name,
            logger_manager=LOGGER_MANAGER
        )

    def setUp(self):
        """Test setup"""
        super(TestNavBase, self).setUp()
        self.url = self.test_config['tests']['unitaries']['url']

    def test_000_navbase_instance(self):
        """Testcase: test_000_navbase_instance"""
        assert isinstance(self.bot.navigation, NavBase) is True


    def test_001_gourl_without_waits(self):
        """Testcase: test_001_gourl_without_waitsparam"""
        self.bot.navigation.get_url(self.url)

    def test_002_gourl_with_waitsparam(self):
        """Testcase: test_002_gourl_with_waitsparam"""
        self.bot.navigation.get_url(self.url, wait_for_load=0)
