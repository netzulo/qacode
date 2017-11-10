# -*- coding: utf-8 -*-
# pylint: disable=too-many-instance-attributes
"""Test suite for pages package"""


from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.pages.PageLogin import PageLogin
from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.loggers.LoggerManager import LoggerManager


LOGGER_MANAGER = LoggerManager()


class TestPageLogin(TestInfoBot):
    """Test Suite for class PageLogin"""

    def __init__(self, method_name="TestPageLogin"):
        """Just call to parent constructor class, see TestInfoBot"""
        super(TestPageLogin, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER
        )
        self.url_login = self.test_config['tests']['functionals']['url_login']
        self.url_logout = self.test_config['tests']['functionals']['url_logout']
        self.url_logged = self.test_config['tests']['functionals']['url_logged']
        self.url_404 = self.test_config['tests']['functionals']['url_404']
        self.selectors = self.test_config['tests']['functionals']['selectors_login']
        self.creed_user = self.test_config['tests']['functionals']['creed_user']
        self.creed_pass = self.test_config['tests']['functionals']['creed_pass']
        self.msg_logged = "Logged success on url={}".format(self.url_logged)
        self.msg_fail_ok = "Login fail success on url={}".format(self.url_logged)

    def test_001_page_login_instance(self):
        """Testcase: test_001_page_login_instance"""
        try:
            PageLogin(self.bot, self.url_login, selectors=self.selectors)
            assert self.url_login in self.bot.curr_driver.current_url
        except PageException as err:
            self.bot.log.error(err.args)
            raise Exception(err)

    def test_002_login_no_selectors(self):
        """Testcase: test_002_login_no_selectors"""
        message_error = "PageLogin must fail at instance without selectors"
        try:
            PageLogin(self.bot, self.url_login)
            self.fail(message_error)
        except PageException as err:
            if not isinstance(err, PageException):
                raise Exception(message_error)
            else:
                self.log.info("PageLogin failed success")

    def test_003_login_ok(self):
        """Testcase: test_003_login_ok"""
        page = PageLogin(self.bot, self.url_login, selectors=self.selectors)
        assert self.url_login in self.bot.curr_driver.current_url
        page.login(self.creed_user, self.creed_pass)
        assert self.url_logged in self.bot.curr_driver.current_url
        self.log.debug(self.msg_logged)

    def test_004_login_baduser(self):
        """Testcase: test_004_login_baduser"""
        page = PageLogin(self.bot, self.url_login, selectors=self.selectors)
        assert self.url_login in self.bot.curr_driver.current_url
        page.login(" ", self.creed_pass)
        assert self.url_404 in self.bot.curr_driver.current_url
        self.log.debug(self.msg_fail_ok)

    def test_005_login_emptypass(self):
        """Testcase: test_005_login_emptypass"""
        page = PageLogin(self.bot, self.url_login, selectors=self.selectors)
        assert self.url_login in self.bot.curr_driver.current_url
        page.login(self.creed_user, " ")
        assert self.url_404 in self.bot.curr_driver.current_url
        self.log.debug(self.msg_fail_ok)

    def test_006_login_creedsempty(self):
        """Testcase: test_006_login_creedsempty"""
        page = PageLogin(self.bot, self.url_login, selectors=self.selectors)
        assert self.url_login in self.bot.curr_driver.current_url
        page.login(" ", " ")
        assert self.url_logged in self.bot.curr_driver.current_url
        self.log.debug(self.msg_fail_ok)
