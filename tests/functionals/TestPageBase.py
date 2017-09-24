import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing. TesInfoBot import TestInfoBot
from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.pages.PageBase import PageBase
from selenium.webdriver.remote.webelement import WebElement
from qacode.core.loggers.LoggerManager import LoggerManager

logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)

class TestPageBase(TestInfoBot):
    """Test Suite for PageBase class"""
    
    def __init__(self, method_name="TestPageBase"):
        super(TestPageBase, self).__init__(method_name, logger_manager=logger_manager)

    def test_001_page_base_instance(self):
        try:
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'])
            assert cfg['TEST_UNITARIES']['url'] in self.bot.curr_driver.current_url
        except PageException as err:
            raise Exception(err)
            
    def test_002_page_base_instance_go_url_False(self):
        try:
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'], go_url=False)
            assert cfg['TEST_UNITARIES']['url'] not in self.bot.curr_driver.current_url
        except PageException as err:
            raise Exception(err)
   
    def test_003_page_base_method_go_page_url(self):
        try:
            url_second_page = "https://www.netzulo.com"
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'])
            assert cfg['TEST_UNITARIES']['url'] in self.bot.curr_driver.current_url
            page.go_page_url(url_second_page )
            assert url_second_page in self.bot.curr_driver.current_url
        except PageException as err:
            raise Exception(err)

    def test_004_page_base_method_get_elements_one_element(self):
        try:
            selectors = [".logo-dark[alt='Netzulo Testing Lab']"]
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'],selectors=selectors)
            assert isinstance(page.elements[0], WebElement)
        except PageException as err:
            raise Exception(err)

    def test_005_page_base_method_get_elements_multiple_elements(self):
        try:
            selectors = [".logo-dark[alt='Netzulo Testing Lab']", ".ti-menu"]
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'],selectors=selectors)
            assert isinstance(page.elements[0], WebElement)
        except PageException as err:
            raise Exception(err)

if __name__ == '__main__':
    unittest.main()
