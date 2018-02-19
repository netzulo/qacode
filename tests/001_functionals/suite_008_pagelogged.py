# -*- coding: utf-8 -*-
# pylint: disable=too-many-instance-attributes
"""Test suite for pages package"""


from unittest import skipIf
from qacode.core.exceptions.page_exception import PageException
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.utils import settings
from qacode.core.webs.pages.page_logged import PageLogged
from qacode.core.webs.pages.page_login import PageLogin


SETTINGS = settings()
SKIP_PAGES = SETTINGS['tests']['skip']['web_pages']
SKIP_PAGES_MSG = 'web_pages DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestPageLogged(TestInfoBot):
    """Test Suite for class PageLogin"""

    def __init__(self, method_name="suite_TestPageLogged"):
        """Just call to parent constructor class, see TestInfoBot."""
        super(TestPageLogged, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )
        self.url_login = self.test_config.get(
            'tests')['functionals']['pages'][0]['url']
        self.url_logout = self.test_config.get(
            'tests')['functionals']['pages'][0]['url_logout']
        self.url_logged = self.test_config.get(
            'tests')['functionals']['pages'][0]['url_logged']
        self.url_404 = self.test_config.get(
            'tests')['functionals']['pages'][0]['url_404']
        self.p_login_controls = self.test_config.get(
            'tests')['functionals']['pages'][0]['controls']
        self.selectors = [
            self.p_login_controls[0]['selector'],
            self.p_login_controls[1]['selector'],
            self.p_login_controls[2]['selector']
        ]
        self.creed_user = self.test_config.get(
            'tests')['functionals']['pages'][0]['creeds']['name']
        self.creed_pass = self.test_config.get(
            'tests')['functionals']['pages'][0]['creeds']['pass']
        self.msg_logged = "Logged success on url={}".format(
            self.url_logged)
        self.msg_fail_ok = "Login fail success on url={}".format(
            self.url_logged)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_001_page_logged_instance(self):
        """Testcase: test_001_page_login_instance"""
        try:
            p_login = PageLogin(
                self.bot,
                self.url_login,
                self.url_logged,
                selectors=self.selectors)
            p_login.login(self.creed_user, self.creed_pass)
            PageLogged(
                self.bot,
                self.url_logged,
                self.url_logout)
        except PageException as err:
            self.bot.log.error(err.args)
            raise Exception(err)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_002_page_logged_method_islogged_true(self):
        """Testcase: test_002_page_logged_method_islogged_true"""
        p_login = PageLogin(self.bot, self.url_login, self.url_logged,
                            selectors=self.selectors)
        p_login.login(self.creed_user, self.creed_pass)
        p_logged = PageLogged(self.bot, self.url_logged, self.url_logout)
        self.assertTrue(p_logged.is_logged(p_login))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_003_page_logged_method_islogged_false(self):
        """Testcase: test_002_page_logged_method_islogged_true"""
        p_login = PageLogin(self.bot, self.url_login, self.url_logged,
                            selectors=self.selectors)
        p_login.login("thistest", "willfail")
        p_logged = PageLogged(self.bot, self.url_logged, self.url_logout)
        self.assertFalse(p_logged.is_logged(p_login))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_004_page_logged_raises_noneurllogged(self):
        """Testcase: test_002_page_logged_method_islogged_true"""
        self.assertRaises(
            PageException,
            PageLogged,
            self.bot,
            None,
            self.url_logout)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_005_page_logged_raises_noneurllogout(self):
        """Testcase: test_002_page_logged_method_islogged_true"""
        self.assertRaises(
            PageException,
            PageLogged,
            self.bot,
            self.url_logged,
            None)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_006_page_logged_method_islogged_raises_notplogin(self):
        """Testcase: test_002_page_logged_method_islogged_true"""
        p_login = PageLogin(self.bot, self.url_login, self.url_logged,
                            selectors=self.selectors)
        p_login.login(self.creed_user, self.creed_pass)
        p_logged = PageLogged(self.bot, self.url_logged, self.url_logout)
        self.assertRaises(PageException, p_logged.is_logged, None)
