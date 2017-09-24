import unittest, logging, time, ast
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.pages.PageLogin import PageLogin
from qacode.core.testing. TesInfoBot import TestInfoBot
from qacode.core.loggers.LoggerManager import LoggerManager

logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)

class TestPageLogin(TestInfoBot):
    """Test Suite for class PageLogin"""

    def __init__(self, method_name="TestPageLogin"):
        super(TestPageLogin, self).__init__(method_name, logger_manager=logger_manager)
        self.url_login = cfg['TEST_FUNCTIONALS']['url_login']
        self.url_logout = cfg['TEST_FUNCTIONALS']['url_logout']
        self.url_logged_ok = cfg['TEST_FUNCTIONALS']['url_logged_ok']
        self.url_logged_ko = cfg['TEST_FUNCTIONALS']['url_logged_ko']
        self.selectors =  ast.literal_eval(cfg['TEST_FUNCTIONALS']['selectors_login'])
        self.creed_user = cfg['TEST_FUNCTIONALS']['creed_user']
        self.creed_pass = cfg['TEST_FUNCTIONALS']['creed_pass']

    def test_001_page_login_instance(self):
        try:
            page = PageLogin(self.bot,self.url_login, selectors=self.selectors)
            assert self.url_login in self.bot.curr_driver.current_url
        except PageException as err:
            self.bot.log.error(err.args)
            raise Exception(err)

    def test_002_page_login_instance_without_selectors(self):
        message_error = "PageLogin must fail at instance without selectors"
        try:
            page = PageLogin(self.bot,self.url_login)
            self.fail(message_error)
        except PageException as err:
            if not isinstance(err, PageException):
                raise Exception(message_error)
            else:
                self.log.info("PageLogin failed success")

    def test_003_page_login_method_loging_creeds_ok(self):
        try:
            page = PageLogin(self.bot,self.url_login, selectors=self.selectors)
            assert self.url_login in self.bot.curr_driver.current_url
            page.login(self.creed_user,self.creed_pass)
            assert self.url_logged_ok in self.bot.curr_driver.current_url
            self.log.debug("Logged on {}".format(self.url_logged_ok))
        except PageException as err:
            self.log.error("Uknown error")
            raise Exception(err)

    def test_004_page_login_method_loging_creeds_empty_user(self):
        try:
            page = PageLogin(self.bot,self.url_login, selectors=self.selectors)
            assert self.url_login in self.bot.curr_driver.current_url
            page.login(" ",self.creed_pass)
            assert self.url_logged_ko in self.bot.curr_driver.current_url
            self.log.debug("Login failed success on {}".format(self.url_logged_ok))
        except PageException as err:
            self.log.error("Uknown error")
            raise Exception(err)

    def test_005_page_login_method_loging_creeds_empty_pass(self):
        try:
            page = PageLogin(self.bot,self.url_login, selectors=self.selectors)
            assert self.url_login in self.bot.curr_driver.current_url
            page.login(self.creed_user," ")
            assert self.url_logged_ko in self.bot.curr_driver.current_url
            self.log.debug("Login failed success on {}".format(self.url_logged_ok))
        except PageException as err:
            self.log.error("Uknown error")
            raise Exception(err)

    def test_006_page_login_method_loging_creeds_empty(self):
        try:
            page = PageLogin(self.bot,self.url_login, selectors=self.selectors)
            assert self.url_login in self.bot.curr_driver.current_url
            page.login(" "," ")
            assert self.url_logged_ko in self.bot.curr_driver.current_url
            self.log.debug("Login failed success on {}".format(self.url_logged_ok))
        except PageException as err:
            self.log.error("Uknown error")
            raise Exception(err)

if __name__ == '__main__':
    unittest.main()
