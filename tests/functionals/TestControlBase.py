import unittest, logging
from testconfig import config as cfg
from selenium.webdriver.remote.webelement import WebElement
from qacode.core.testing.TesInfoBot import TestInfoBot
from qacode.core.webs.controls.ControlBase import ControlBase
from qacode.core.exceptions.ControlException import ControlException
from qacode.core.loggers.LoggerManager import LoggerManager

logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)

class TestControlBase(TestInfoBot):
    """Test Suite for ControlBase class"""

    def __init__(self, method_name="TestControlBase"):
        super(TestControlBase, self).__init__(method_name, logger_manager=logger_manager)

    def test_001_controlbase_instance_selector(self):
        url = cfg['TEST_UNITARIES']['url']
        selector = "[href='http://www.netzulo.com/?page_id=116']"
        self.bot.navigation.get_url(url)            
        assert url in self.bot.curr_driver.current_url
        control = ControlBase(self.bot,selector=selector)
        self.assertIsInstance(control.element,WebElement)
        self.assertIsInstance(control,ControlBase)

    def test_002_controlbase_instance_element(self):
        url = cfg['TEST_UNITARIES']['url']
        selector = "[href='http://www.netzulo.com/?page_id=116']"
        self.bot.navigation.get_url(url)            
        assert url in self.bot.curr_driver.current_url               
        element = self.bot.navigation.find_element(selector)        
        control = ControlBase(self.bot,element=element)
        self.assertIsInstance(control.element,WebElement)
        self.assertIsInstance(control,ControlBase)