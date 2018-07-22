# -*- coding: utf-8 -*-
"""Package for suites and tests related to bots.modules package"""


import pytest
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.testing.test_info import TestInfoBotUnique
from qautils.files import settings


SETTINGS = settings(file_path="qacode/configs/")
SKIP_NAVS = SETTINGS['tests']['skip']['bot_navigations']
SKIP_NAVS_MSG = 'bot_navigations DISABLED by config file'


class TestNavBase(TestInfoBotUnique):
    """Test Suite for class NavBase"""

    app = None
    page = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestNavBase, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_NAVS)

    def setup_method(self, test_method, close=True):
        """Configure self.attribute"""
        super(TestNavBase, self).setup_method(
            test_method,
            config=settings(file_path="qacode/configs/"))
        self.add_property('app', self.settings_app('qadmin'))
        self.add_property('page', self.settings_page('qacode_login'))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_navbase_instance(self):
        """Testcase: test_navbase_instance"""
        self.assert_is_instance(self.bot.navigation, NavBase)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_gourl_without_waits(self):
        """Testcase: test_gourl_without_waits"""
        self.bot.navigation.get_url(self.page.get('url'))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_gourl_with_waitsparam(self):
        """Testcase: test_gourl_with_waitsparam"""
        self.bot.navigation.get_url(
            self.page.get('url'), wait_for_load=0)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_get_maximizewindow(self):
        """Testcase: test_getmaximizewindow"""
        self.bot.navigation.get_maximize_window()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getcapabilities(self):
        """Testcase: test_getcapabilities"""
        caps = self.bot.navigation.get_capabilities()
        self.assert_is_instance(caps, dict)
        self.assert_is_instance(caps['chrome'], dict)
        self.assert_equals(caps['browserName'], 'chrome')

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getlog_default(self):
        """Testcase: test_getlog_default"""
        self.bot.navigation.get_url(self.page.get('url'))
        log_data = self.bot.navigation.get_log()
        self.assert_not_none(log_data)
        self.log.debug("selenium logs, browser={}".format(log_data))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    @pytest.mark.parametrize(
        "log_name", ['browser', 'driver', 'client', 'server'])
    def test_getlog_lognames(self, log_name):
        """Testcase: test_getlog_logname"""
        self.bot.navigation.get_url(self.page.get('url'))
        log_data = self.bot.navigation.get_log(log_name=log_name)
        self.assert_not_none(log_data)
        msg = "selenium logs, log_name={}, log_data={}".format(
            log_name, log_data)
        self.log.debug(msg)
