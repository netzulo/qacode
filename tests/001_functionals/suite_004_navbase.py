# -*- coding: utf-8 -*-
"""Package for suites and tests related to bots.modules package"""


import pytest
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_REMOTES = SETTINGS['tests']['skip']['drivers_remote']
SKIP_REMOTES_MSG = 'drivers_remote DISABLED by config file'


class TestNavBase(TestInfoBotUnique):
    """Test Suite for class NavBase"""

    app = None
    page_home = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestNavBase, cls).setup_class(
            config=settings(),
            skip_force=SKIP_REMOTES)

    def setup_method(self, test_method, close=True):
        """Configure self.attribute"""
        super(TestNavBase, self).setup_method(test_method, config=settings())
        self.add_property('app', self.settings_app('nav_tests'))
        self.add_property('page_home', self.settings_page('nav_tests_home'))

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_navbase_instance(self):
        """Testcase: test_000_navbase_instance"""
        self.assert_is_instance(self.bot.navigation, NavBase)

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_gourl_without_waits(self):
        """Testcase: test_001_gourl_without_waitsparam"""
        self.bot.navigation.get_url(self.page_home.get('url'))

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_gourl_with_waitsparam(self):
        """Testcase: test_002_gourl_with_waitsparam"""
        self.bot.navigation.get_url(
            self.page_home.get('url'), wait_for_load=0)

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_getmaximizewindow(self):
        """Testcase: test_003_getmaximizewindow"""
        self.bot.navigation.get_maximize_window()

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_getcapabilities(self):
        """Testcase: test_004_getcapabilities"""
        caps = self.bot.navigation.get_capabilities()
        self.assert_is_instance(caps, dict)
        self.assert_is_instance(caps['chrome'], dict)
        self.assert_equals(caps['browserName'], 'chrome')

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_getlog(self):
        """Testcase: test_005_getlog"""
        self.bot.navigation.get_url(self.page_home.get('url'))
        log_data = self.bot.navigation.get_log()
        self.assert_not_none(log_data)
        self.log.debug("selenium logs, browser={}".format(log_data))

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_getlog_browser(self):
        """Testcase: test_006_getlog_browser"""
        self.bot.navigation.get_url(self.page_home.get('url'))
        log_data = self.bot.navigation.get_log(log_name='browser')
        self.assert_not_none(log_data)
        self.log.debug("selenium logs, browser={}".format(log_data))

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_getlog_driver(self):
        """Testcase: test_007_getlog_driver"""
        self.bot.navigation.get_url(self.page_home.get('url'))
        log_data = self.bot.navigation.get_log(log_name='driver')
        self.assert_not_none(log_data)
        self.log.debug("selenium logs, driver={}".format(log_data))

    @pytest.mark.skip('Issue opened on github selenium, waiting...')
    def test_getlog_client(self):
        """Testcase: test_008_getlog_client
        https://github.com/SeleniumHQ/selenium/issues/5410
        """
        self.bot.navigation.get_url(self.page_home.get('url'))
        log_data = self.bot.navigation.get_log(log_name='client')
        self.assert_not_none(log_data)
        self.log.debug("selenium logs, client={}".format(log_data))

    @pytest.mark.skipIf(SKIP_REMOTES, SKIP_REMOTES_MSG)
    def test_getlog_server(self):
        """Testcase: test_008_getlog_client"""
        self.bot.navigation.get_url(self.page_home.get('url'))
        log_data = self.bot.navigation.get_log(log_name='server')
        self.assert_not_none(log_data)
        self.log.debug("selenium logs, server={}".format(log_data))
