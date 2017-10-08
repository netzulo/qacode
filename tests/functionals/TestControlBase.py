# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""

from selenium.webdriver.remote.webelement import WebElement
from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.webs.controls.ControlBase import ControlBase
from qacode.core.loggers.LoggerManager import LoggerManager


LOGGER_MANAGER = LoggerManager()


class TestControlBase(TestInfoBot):
    """Test Suite for ControlBase class"""

    def __init__(self, method_name="TestControlBase"):
        super(TestControlBase, self).__init__(
            method_name=method_name,
            logger_manager=LOGGER_MANAGER
        )

    def setUp(self):
        super(TestControlBase, self).setUp()
        self.url = self.test_config['tests']['unitaries']['url']
        self.selector = "[href='http://www.netzulo.com/?page_id=116']"
        self.bot.navigation.get_url(self.url)
        assert self.url in self.bot.curr_driver.current_url

    def test_001_control_findselector(self):
        """Testcase: test_001_control_findselector"""
        control = ControlBase(self.bot, selector=self.selector)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    def test_002_control_instance(self):
        """Testcase: test_002_control_instance"""
        element = self.bot.navigation.find_element(self.selector)
        control = ControlBase(self.bot, element=element)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)
