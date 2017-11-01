# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""

from selenium.webdriver.remote.webelement import WebElement
from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.webs.controls.ControlBase import ControlBase
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.exceptions.ControlException import ControlException

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
        self.url = self.test_config.get(
            'tests')['functionals']['url_selector_parent']
        self.selector_parent = self.test_config.get(
            'tests')['functionals']['selector_parent']
        self.selector_child = self.test_config.get(
            'tests')['functionals']['selector_child']
        self.bot.navigation.get_url(self.url)
        self.assert_equals_url(self.bot.curr_driver.current_url, self.url)

    def test_000_instance_byelement(self):
        """Testcase: test_000_instance_byelement"""
        element = self.bot.navigation.find_element(self.selector_parent)
        control = ControlBase(self.bot, element=element)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    def test_001_instance_byselector(self):
        """Testcase: test_001_instance_byselector"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    def test_002_raises_nosearch(self):
        """Testcase: test_002_raises_nosearch"""
        self.assertRaises(
            ControlException, ControlBase, self.bot, self.selector_parent, search=False)

    def test_003_method_findchild(self):
        """Testcase: test_003_method_findchild"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertIsInstance(control.find_child(self.selector_child), ControlBase)
