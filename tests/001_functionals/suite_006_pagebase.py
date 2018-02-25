# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Testsuite for package pages"""


import time
from unittest import skipIf
from qacode.core.exceptions.page_exception import PageException
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.utils import settings
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.pages.page_base import PageBase
from selenium.webdriver.remote.webelement import WebElement


SETTINGS = settings()
SKIP_PAGES = SETTINGS['tests']['skip']['web_pages']
SKIP_PAGES_MSG = 'web_pages DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
BOT = None


class TestPageBase(TestInfoBot):
    """Test Suite for PageBase class"""

    @classmethod
    def setUpClass(cls):
        """Set up test suite"""
        global BOT
        if not SKIP_PAGES:
            BOT = TestInfoBot.bot_open(SETTINGS, LOGGER_MANAGER)

    @classmethod
    def tearDownClass(cls):
        """Tear down test suite"""
        global BOT
        if not SKIP_PAGES:
            TestInfoBot.bot_close(BOT)

    def __init__(self, method_name="suite_TestPageBase"):
        """Test what probes PageBase class and methods

        Keyword Arguments:
            method_name {str} -- name for test page base
                (default: {"suite_TestPageBase"})
        """
        super(TestPageBase, self).__init__(
            method_name=method_name,
            bot=BOT
        )

    def setUp(self):
        """Set up test case"""
        super(TestPageBase, self).setUp()
        self.p_login_config = SETTINGS['tests']['functionals']['pages'][0]
        self.url = self.p_login_config['url']
        self.p_login_controls = self.p_login_config['controls']
        self.selectors = [
            self.p_login_controls[0]['selector'],
            self.p_login_controls[1]['selector'],
            self.p_login_controls[2]['selector']
        ]
        self.url_other = self.p_login_config['url_logout']
        time.sleep(2)

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
        self.bot.navigation.get_url(self.url_other)
        time.sleep(3)
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
    def test_012_method_getelement_aswebelement(self):
        """Testcase: test_012_method_getelement_aswebelement"""
        page = PageBase(self.bot, self.url)
        element = page.get_element(self.selectors[0])
        self.assertIsInstance(element, WebElement)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_013_method_getelement_ascontrol(self):
        """Testcase: test_013_method_getelement_ascontrol"""
        page = PageBase(self.bot, self.url)
        element = page.get_element(self.selectors[0], as_control=True)
        self.assertIsInstance(element, ControlBase)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_014_method_getelements_aswebelements(self):
        """Testcase: test_014_method_getelements_aswebelements"""
        page = PageBase(self.bot, self.url)
        elements = page.get_elements(self.selectors)
        self.assertIsInstance(elements[1], WebElement)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_015_method_getelements_ascontrols(self):
        """Testcase: test_015_method_getelements_ascontrols"""
        page = PageBase(self.bot, self.url)
        elements = page.get_elements(self.selectors, as_controls=True)
        self.assertIsInstance(elements[1], ControlBase)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_016_method_getelements_raises_noneselectors(self):
        """Testcase: test_016_method_getelements_raises_noneselectors"""
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.get_elements,
            None, as_controls=True)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_017_method_getelements_raises_emptyselector(self):
        """Testcase: test_017_method_getelements_raises_emptyselector"""
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.get_elements,
            [''])

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_018_method_isurl_default(self):
        """Testcase: test_018_method_isurl_default"""
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url())

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_019_method_isurl_true(self):
        """Testcase: test_019_method_isurl_true"""
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url(self.url))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_020_method_isurl_false(self):
        """Testcase: test_020_method_isurl_false"""
        page = PageBase(self.bot, self.url)
        self.assertFalse(page.is_url(self.url_other))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_021_method_isurl_notignoreraises(self):
        """Testcase: test_021_method_isurl_notignoreraises"""
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url(ignore_raises=False))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_022_method_isurl_true_notignoreraises(self):
        """Testcase: test_022_method_isurl_true_notignoreraises"""
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url(
            url=self.url,
            ignore_raises=False))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_023_method_isurl_raises_false_notignoreraises(self):
        """Testcase: test_023_method_isurl_raises_false_notignoreraises"""
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.is_url,
            url=self.url_other,
            ignore_raises=False)
