# -*- coding: utf-8 -*-
# pylint: disable=too-many-instance-attributes
"""Test suite for pages package"""


from unittest import skipIf
from qacode.core.exceptions.page_exception import PageException
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.utils import settings
from qacode.core.webs.pages.page_login import PageLogin


SETTINGS = settings()
SKIP_PAGES = SETTINGS['tests']['skip']['web_pages']
SKIP_PAGES_MSG = 'web_pages DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
BOT = None


class TestPageLogin(TestInfoBot):
    """Test Suite for class PageLogin"""

    @classmethod
    def setUpClass(cls):
        """Set up test suite"""
        global BOT
        if not SKIP_PAGES:
            BOT = TestInfoBot.bot_open(SETTINGS, LOGGER_MANAGER)

    @classmethod
    def tearDownClass(cls):
        """Tear down test suite"""
        global BOT
        if not SKIP_PAGES:
            TestInfoBot.bot_close(BOT)

    def __init__(self, method_name="suite_TestPageLogin"):
        """Test what probes PageLogin class and methods

        Keyword Arguments:
            method_name {str} -- name for test page login
                (default: {"suite_TestPageLogin"})
        """
        super(TestPageLogin, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )
        self.p_login_config = SETTINGS['tests']['functionals']['pages'][0]
        self.url_login = self.p_login_config['url']
        self.url_logout = self.p_login_config['url_logout']
        self.url_logged = self.p_login_config['url_logged']
        self.url_404 = self.p_login_config['url_404']
        self.p_login_controls = self.p_login_config['controls']
        self.selectors = [
            self.p_login_controls[0]['selector'],
            self.p_login_controls[1]['selector'],
            self.p_login_controls[2]['selector']
        ]
        self.creed_user = self.p_login_config['creeds']['name']
        self.creed_pass = self.p_login_config['creeds']['pass']
        self.msg_logged = "Logged success on url={}".format(
            self.url_logged)
        self.msg_fail_ok = "Login fail success on url={}".format(
            self.url_logged)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_001_page_login_instance(self):
        """Testcase: test_001_page_login_instance"""
        try:
            PageLogin(
                self.bot,
                self.url_login,
                self.url_logged,
                selectors=self.selectors)
        except PageException as err:
            self.bot.log.error(err.args)
            raise Exception(err)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_002_login_no_selectors(self):
        """Testcase: test_002_login_no_selectors"""
        message_error = "PageLogin must fail at instance without selectors"
        try:
            PageLogin(self.bot, self.url_login, self.url_logged)
            self.fail(message_error)
        except PageException as err:
            if not isinstance(err, PageException):
                raise Exception(message_error)
            else:
                self.log.info("PageLogin failed success")

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_003_login_ok(self):
        """Testcase: test_003_login_ok"""
        page = PageLogin(
            self.bot,
            self.url_login,
            self.url_logged,
            selectors=self.selectors)
        self.assertFalse(page.is_logged)
        page.login(self.creed_user, self.creed_pass)
        self.assertTrue(page.is_logged)
        self.log.debug(self.msg_logged)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_004_login_baduser(self):
        """Testcase: test_004_login_baduser"""
        page = PageLogin(
            self.bot,
            self.url_login,
            self.url_logged,
            selectors=self.selectors)
        self.assertFalse(page.is_logged)
        page.login(" ", self.creed_pass)
        self.assertFalse(page.is_logged)
        self.log.debug(self.msg_fail_ok)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_005_login_emptypass(self):
        """Testcase: test_005_login_emptypass"""
        page = PageLogin(
            self.bot,
            self.url_login,
            self.url_logged,
            selectors=self.selectors)
        self.assertFalse(page.is_logged)
        page.login(self.creed_user, " ")
        self.assertFalse(page.is_logged)
        self.log.debug(self.msg_fail_ok)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_006_login_creedsempty(self):
        """Testcase: test_006_login_creedsempty"""
        page = PageLogin(
            self.bot,
            self.url_login,
            self.url_logged,
            selectors=self.selectors)
        self.assertFalse(page.is_logged)
        page.login(" ", " ")
        self.assertFalse(page.is_logged)
        self.log.debug(self.msg_fail_ok)
