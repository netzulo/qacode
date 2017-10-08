# -*- coding: utf-8 -*-
"""Testsuite for package pages"""


from selenium.webdriver.remote.webelement import WebElement
from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.webs.pages.PageBase import PageBase
from qacode.core.loggers.LoggerManager import LoggerManager


LOGGER_MANAGER = LoggerManager()


class TestPageBase(TestInfoBot):
    """Test Suite for PageBase class"""

    def __init__(self, method_name="TestPageBase"):
        """Just call to parent constructor class, see TestInfoBot"""
        super(TestPageBase, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER
        )

    def test_001_page_base_instance(self):
        """Testcase: test_001_page_base_instance"""
        url = self.test_config['tests']['unitaries']['url']
        PageBase(self.bot, url)
        assert url in self.bot.curr_driver.current_url

    def test_002_page_gourl(self):
        """Testcase: test_002_page_gourl"""
        url = self.test_config['tests']['unitaries']['url']
        PageBase(self.bot, url, go_url=False)
        assert url not in self.bot.curr_driver.current_url

    def test_003_method_gopageurl(self):
        """Testcase: test_003_method_gopageurl"""
        url = self.test_config['tests']['unitaries']['url']
        url_second_page = "https://www.netzulo.com"
        page = PageBase(self.bot, url)
        assert url in self.bot.curr_driver.current_url
        page.go_page_url(url_second_page)
        assert url_second_page in self.bot.curr_driver.current_url

    def test_004_method_getelements_one(self):
        """Testcase: test_004_method_getelements_one"""
        url = self.test_config['tests']['unitaries']['url']
        selectors = [".logo-dark[alt='Netzulo Testing Lab']"]
        page = PageBase(self.bot, url, selectors=selectors)
        assert isinstance(page.elements[0], WebElement)

    def test_005_method_getelements(self):
        """Testcase: test_005_method_getelements"""
        url = self.test_config['tests']['unitaries']['url']
        selectors = [".logo-dark[alt='Netzulo Testing Lab']", ".ti-menu"]
        page = PageBase(self.bot, url, selectors=selectors)
        assert isinstance(page.elements[0], WebElement)
        assert isinstance(page.elements[1], WebElement)
