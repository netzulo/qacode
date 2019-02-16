# -*- coding: utf-8 -*-
"""Package for suites and tests related to bots.modules package"""


import pytest
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.testing.test_info import TestInfoBotUnique
from qautils.files import settings
from selenium.webdriver.remote.webelement import WebElement


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
    def test_gourl_withoutwaits(self):
        """Testcase: test_gourl_withoutwaits"""
        self.bot.navigation.get_url(self.page.get('url'))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_gourl_withwaits(self):
        """Testcase: test_gourl_withwaits"""
        self.bot.navigation.get_url(
            self.page.get('url'), wait_for_load=1)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_reload_ok(self):
        """Testcase: test_reload_ok"""
        self.bot.navigation.reload()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_forward_ok(self):
        """Testcase: test_reload_ok"""
        self.bot.navigation.forward()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getmaximizewindow_ok(self):
        """Testcase: test_getmaximizewindow_ok"""
        self.bot.navigation.get_maximize_window()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getcapabilities_ok(self):
        """Testcase: test_getcapabilities_ok"""
        caps = self.bot.navigation.get_capabilities()
        self.assert_is_instance(caps, dict)
        self.assert_is_instance(caps['chrome'], dict)
        self.assert_equals(caps['browserName'], 'chrome')

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getlog_ok(self):
        """Testcase: test_getlog_ok"""
        self.bot.navigation.get_url(self.page.get('url'))
        log_data = self.bot.navigation.get_log()
        self.assert_not_none(log_data)
        self.log.debug("selenium logs, browser={}".format(log_data))

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    @pytest.mark.parametrize(
        "log_name", ['browser', 'driver', 'client', 'server'])
    def test_getlog_lognames(self, log_name):
        """Testcase: test_getlog_lognames"""
        self.bot.navigation.get_url(self.page.get('url'))
        log_data = self.bot.navigation.get_log(log_name=log_name)
        self.assert_not_none(log_data)
        msg = "selenium logs, log_name={}, log_data={}".format(
            log_name, log_data)
        self.log.debug(msg)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelement_ok(self):
        """Testcase: test_findelement_ok"""
        selector = "body"
        element = self.bot.navigation.find_element(selector)
        self.assert_is_instance(element, WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelement_notfound(self):
        """Testcase: test_findelement_notfound"""
        selector = "article"
        with pytest.raises(CoreException):
            self.bot.navigation.find_element(selector)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelement_notlocator(self):
        """Testcase: test_findelement_notlocator"""
        selector = "body"
        with pytest.raises(CoreException):
            self.bot.navigation.find_element(
                selector, locator=None)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelements_ok(self):
        """Testcase: test_findelement_ok"""
        selector = "body>*"
        elements = self.bot.navigation.find_elements(selector)
        self.assert_not_none(elements)
        self.assert_is_instance(elements, list)
        for element in elements:
            self.assert_is_instance(element, WebElement)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelements_notfound(self):
        """Testcase: test_findelements_notfound"""
        selector = "article"
        with pytest.raises(CoreException):
            self.bot.navigation.find_elements(selector)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_findelements_notlocator(self):
        """Testcase: test_findelements_notlocator"""
        selector = "body"
        with pytest.raises(CoreException):
            self.bot.navigation.find_elements(
                selector, locator=None)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getwindowhandle_ok(self):
        """Testcase: test_getwindowhandle_ok"""
        window = self.bot.navigation.get_window_handle()
        self.assert_not_none(window)
        self.assert_is_instance(window, str)

    @pytest.mark.skipIf(
        True, "Depends of remote webdriver and local to get working")
    def test_addcookie_ok(self):
        """Testcase: test_addcookie_ok"""
        cookie = {"name": "test_cookie", "value": "test_value"}
        self.bot.navigation.add_cookie(cookie)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_getcookies_ok(self):
        """Testcase: test_getcookies_ok"""
        cookies = self.bot.navigation.get_cookies()
        self.assert_not_none(cookies)
        self.assert_is_instance(cookies, list)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_deleteallcookies_ok(self):
        """Testcase: test_deleteallcookies_ok"""
        self.bot.navigation.delete_cookies()

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_setwindowsize_ok(self):
        """Testcase: test_setwindowsize_ok"""
        self.bot.navigation.set_window_size(
            pos_x=1024, pos_y=768)

    @pytest.mark.skipIf(SKIP_NAVS, SKIP_NAVS_MSG)
    def test_gettitle_ok(self):
        """Testcase: test_gettitle_ok"""
        title = self.bot.navigation.get_title()
        self.assert_not_none(title)
        self.assert_is_instance(title, str)
