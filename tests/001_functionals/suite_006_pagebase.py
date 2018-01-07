# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Testsuite for package pages"""


from unittest import skipIf
from selenium.webdriver.remote.webelement import WebElement
from qacode.core.utils import settings
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.webs.pages.page_base import PageBase
from qacode.core.exceptions.page_exception import PageException
from qacode.core.webs.controls.control_base import ControlBase


SETTINGS = settings()
SKIP_PAGES = SETTINGS['tests']['skip']['web_pages']
SKIP_PAGES_MSG = 'web_pages DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestPageBase(TestInfoBot):
    """Test Suite for PageBase class"""

    def __init__(self, method_name="TestPageBase"):
        """Just call to parent constructor class, see TestInfoBot"""
        super(TestPageBase, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )

    def setUp(self):
        super(TestPageBase, self).setUp()
        self.url = self.test_config.get(
            'tests')['functionals']['url_login']
        self.selectors = self.test_config.get(
            'tests')['functionals']['selectors_login']

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_001_instance_url(self):
        """Testcase: test_001_instance_url"""
        page = PageBase(self.bot, self.url)
        self.assertIsInstance(page, PageBase)
        self.assert_equals_url(
            self.bot.curr_driver.current_url, self.url)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_002_instance_notgourl(self):
        """Testcase: test_002_instance_notgourl"""
        page = PageBase(self.bot, self.url, go_url=False)
        self.assertIsInstance(page, PageBase)
        self.assert_not_equals_url(
            self.bot.curr_driver.current_url, self.url)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_003_instance_element(self):
        """Testcase: test_003_instance_element"""
        page = PageBase(
            self.bot, self.url, selectors=[self.selectors[0]])
        self.assertIsInstance(page, PageBase)
        self.assertIsInstance(page.elements[0], ControlBase)
        self.assertIsInstance(page.elements[0].element, WebElement)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_004_instance_elements(self):
        """Testcase: test_004_instance_elements"""
        page = PageBase(self.bot, self.url, selectors=self.selectors)
        self.assertIsInstance(page, PageBase)
        self.assertIsInstance(page.elements[1], ControlBase)
        self.assertIsInstance(page.elements[1].element, WebElement)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_005_instance_maximized(self):
        """Testcase: test_005_instance_maximized"""
        page = PageBase(self.bot, self.url, maximize=True)
        self.assertIsInstance(page, PageBase)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_006_raises_nonebot(self):
        """Testcase: test_006_raises_nonebot"""
        self.assertRaises(
            PageException,
            PageBase,
            None, self.url)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_007_raises_noneurl(self):
        """Testcase: test_007_raises_noneurl"""
        self.assertRaises(
            PageException,
            PageBase,
            self.bot, None)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_008_raises_nonelocator(self):
        """Testcase: test_008_raises_nonelocator"""
        self.assertRaises(
            PageException,
            PageBase,
            self.bot, self.url, locator=None)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_009_raises_nonegourl(self):
        """Testcase: test_009_raises_nonegourl"""
        self.assertRaises(
            PageException,
            PageBase,
            self.bot, self.url, go_url=None)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_010_raises_nonemaximize(self):
        """Testcase: test_010_raises_nonemaximize"""
        self.assertRaises(
            PageException,
            PageBase,
            self.bot, self.url, maximize=None)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_011_method_gopageurl(self):
        """Testcase: test_011_method_gopageurl"""
        page = PageBase(self.bot, '', go_url=False)
        page.go_page_url(self.url)
        self.assert_equals_url(
            self.bot.curr_driver.current_url, self.url)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_012_method_getelements_aswebelements(self):
        """Testcase: test_012_method_getelements_withselectors"""
        page = PageBase(self.bot, self.url)
        elements = page.get_elements(self.selectors)
        self.assertIsInstance(elements[1], WebElement)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_013_method_getelements_ascontrols(self):
        """Testcase: test_013_method_getelements_paramselectors"""
        page = PageBase(self.bot, self.url)
        elements = page.get_elements(self.selectors, as_controls=True)
        self.assertIsInstance(elements[1], ControlBase)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_014_method_getelements_raises_noneselectors(self):
        """Testcase: test_014_method_getelements_raises_noneselectors"""
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.get_elements,
            None, as_controls=True)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_015_method_getelements_raises_emptyselector(self):
        """Testcase: test_015_method_getelements_raises_emptyselector"""
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.get_elements,
            [''])
