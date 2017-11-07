# -*- coding: utf-8 -*-
"""Testsuite for package pages"""


from selenium.webdriver.remote.webelement import WebElement
from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.webs.pages.PageBase import PageBase
from qacode.core.webs.controls.ControlBase import ControlBase
from qacode.core.loggers.LoggerManager import LoggerManager


LOGGER_MANAGER = LoggerManager()


class TestPageBase(TestInfoBot):
    """Test Suite for PageBase class"""

    def __init__(self, method_name="TestPageBase"):
        """Just call to parent constructor class, see TestInfoBot"""
        super(TestPageBase, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER)

    def setUp(self):
        super(TestPageBase, self).setUp()
        self.url = self.test_config['tests']['functionals']['url_login']
        self.selectors = self.test_config.get(
            'tests')['functionals']['selectors_login']

    def test_001_instance_url(self):
        """Testcase: test_001_instance_url"""
        page = PageBase(self.bot, self.url)
        self.assertIsInstance(page, PageBase)
        self.assert_equals_url(self.bot.curr_driver.current_url, self.url)

    def test_002_instance_notgourl(self):
        """Testcase: test_002_instance_notgourl"""
        page = PageBase(self.bot, self.url, go_url=False)
        self.assertIsInstance(page, PageBase)
        self.assert_not_equals_url(self.bot.curr_driver.current_url, self.url)

    def test_003_instance_element(self):
        """Testcase: test_003_instance_element"""
        page = PageBase(self.bot, self.url, selectors=[self.selectors[0]])
        self.assertIsInstance(page, PageBase)
        self.assertIsInstance(page.elements[0], ControlBase)
        self.assertIsInstance(page.elements[0].element, WebElement)

    def test_004_instance_elements(self):
        """Testcase: test_004_instance_elements"""
        page = PageBase(self.bot, self.url, selectors=self.selectors)
        self.assertIsInstance(page, PageBase)
        self.assertIsInstance(page.elements[1], ControlBase)
        self.assertIsInstance(page.elements[1].element, WebElement)

    def test_005_method_gopageurl(self):
        """Testcase: test_005_method_gopageurl"""
        page = PageBase(self.bot, '', go_url=False)
        page.go_page_url(self.url)
        self.assert_equals_url(self.bot.curr_driver.current_url, self.url)
