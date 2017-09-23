import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.pages.PageLogin import PageLogin

from qacode.core.testing. TesInfoBot import TestInfoBot

class TestPageLogin(TestInfoBot):
    """Test Suite for class PageLogin"""

    def __init__(self, method_name="TestPageLogin"):
        super(TestPageLogin, self).__init__(method_name, logger_manager=None)

    def test_001_page_login_instance(self):
        selectors = ["#login", "#password", "[name='commit']"]
        url_login = cfg['TEST_FUNCTIONALS']['url_login']
        try:
            page = PageLogin(self.bot,url_login, selectors=selectors)
            assert url_login in self.bot.curr_driver.current_url
        except PageException as err:
            self.bot.log.error(err.args)
            raise Exception(err)

    def test_002_page_login_instance_without_selectors(self):
        message_error = "PageLogin must fail at instance without selectors"
        url_login = cfg['TEST_FUNCTIONALS']['url_login']
        try:
            page = PageLogin(self.bot,url_login)
            self.fail(message_error)
        except PageException as err:
            if not isinstance(err, PageException):
                raise Exception(message_error)
            else:
                self.log.info("PageLogin failed success")

if __name__ == '__main__':
    unittest.main()
