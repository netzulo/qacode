# -*- coding: utf-8 -*-
"""Package for suites and tests related to qacode.core.webs.pages package"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_form import ControlForm
from qacode.core.webs.pages.page_base import PageBase
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_PAGES = SETTINGS['tests']['skip']['web_pages']
SKIP_PAGES_MSG = 'web_pages DISABLED by config file'


class TestPageBase(TestInfoBotUnique):
    """Test Suite for class NavBase"""

    app = None
    page_base_config = None
    page_login_config = None

    def setup_method(self, test_method, close=True):
        """Unload self.attribute"""
        super(TestPageBase, self).setup_method(test_method)
        self.add_property('app', self.settings_app('pages_tests'))
        self.page_base_config = self.settings_page('page_base')
        self.page_login_config = self.settings_page('page_login')

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_001_instance_url(self):
        """Testcase: test_001_instance_url"""
        cfg = self.page_base_config.copy()
        cfg.update({
            "go_url": True
        })
        page = PageBase(self.bot, **cfg)
        self.assert_is_instance(page, PageBase)
        self.assert_equals_url(
            self.bot.curr_driver.current_url,
            self.page_base_config.get('url'))

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_002_instance_notgourl(self):
        """Testcase: test_002_instance_notgourl"""
        cfg = self.page_login_config.copy()
        cfg.update({
            "go_url": False,
            "controls": []
        })
        page = PageBase(self.bot, **cfg)
        self.assert_is_instance(page, PageBase)
        self.assert_not_equals_url(
            self.bot.curr_driver.current_url,
            cfg.get('url'))

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_003_instance_element(self):
        "Testcase: test_003_instance_element"
        cfg = self.page_login_config.copy()
        page = PageBase(self.bot, **cfg)
        self.assert_is_instance(page, PageBase)
        self.assert_equals_url(
            self.bot.curr_driver.current_url,
            cfg.get('url'))
        for control in self.page_login_config.get('controls'):
            name = control.get('name')
            self.assert_in(name, dir(page))
            element = page.__dict__[name]
            self.assert_is_instance(element, ControlBase)

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_004_instance_maximized(self):
        """Testcase: test_004_instance_maximized"""
        cfg = self.page_login_config.copy()
        cfg.update({
            "go_url": True,
            "maximize": True,
            "controls": []
        })
        page = PageBase(self.bot, **cfg)
        self.assert_is_instance(page, PageBase)
        self.assert_equals_url(
            self.bot.curr_driver.current_url,
            cfg.get('url'))

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_005_method_getelement(self):
        """Testcase: test_004_instance_maximized"""
        cfg = self.page_login_config.copy()
        page = PageBase(self.bot, **cfg)
        self.assert_is_instance(page, PageBase)
        self.assert_equals_url(
            self.bot.curr_driver.current_url,
            cfg.get('url'))
        for config_control in self.page_login_config.get('controls'):
            name = config_control.get('name')
            instance_name = config_control.get('instance')
            ctl = page.get_element(config_control)
            if instance_name == 'ControlBase':
                self.assert_is_instance(ctl, ControlBase)
            elif instance_name == 'ControlForm':
                self.assert_is_instance(ctl, ControlForm)
            self.assert_in(name, dir(page))

"""

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_011_method_gopageurl(self):
        Testcase: test_011_method_gopageurl
        page = PageBase(self.bot, '', go_url=False)
        page.go_page_url(self.url)
        self.assert_equals_url(
            self.bot.curr_driver.current_url, self.url)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_012_method_getelement_aswebelement(self):
        Testcase: test_012_method_getelement_aswebelement
        page = PageBase(self.bot, self.url)
        element = page.get_element(self.selectors[0])
        self.assertIsInstance(element, WebElement)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_013_method_getelement_ascontrol(self):
        Testcase: test_013_method_getelement_ascontrol
        page = PageBase(self.bot, self.url)
        element = page.get_element(self.selectors[0], as_control=True)
        self.assertIsInstance(element, ControlBase)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_014_method_getelements_aswebelements(self):
        Testcase: test_014_method_getelements_aswebelements
        page = PageBase(self.bot, self.url)
        elements = page.get_elements(self.selectors)
        self.assertIsInstance(elements[1], WebElement)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_015_method_getelements_ascontrols(self):
        Testcase: test_015_method_getelements_ascontrols
        page = PageBase(self.bot, self.url)
        elements = page.get_elements(self.selectors, as_controls=True)
        self.assertIsInstance(elements[1], ControlBase)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_016_method_getelements_raises_noneselectors(self):
        Testcase: test_016_method_getelements_raises_noneselectors
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.get_elements,
            None, as_controls=True)

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_017_method_getelements_raises_emptyselector(self):
        Testcase: test_017_method_getelements_raises_emptyselector
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.get_elements,
            [''])

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_018_method_isurl_default(self):
        Testcase: test_018_method_isurl_default
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url())

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_019_method_isurl_true(self):
        Testcase: test_019_method_isurl_true
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url(self.url))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_020_method_isurl_false(self):
        Testcase: test_020_method_isurl_false
        page = PageBase(self.bot, self.url)
        self.assertFalse(page.is_url(self.url_other))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_021_method_isurl_notignoreraises(self):
        Testcase: test_021_method_isurl_notignoreraises
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url(ignore_raises=False))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_022_method_isurl_true_notignoreraises(self):
        Testcase: test_022_method_isurl_true_notignoreraises
        page = PageBase(self.bot, self.url)
        self.assertTrue(page.is_url(
            url=self.url,
            ignore_raises=False))

    @skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_023_method_isurl_raises_false_notignoreraises(self):
        Testcase: test_023_method_isurl_raises_false_notignoreraises
        page = PageBase(self.bot, self.url)
        self.assertRaises(
            PageException,
            page.is_url,
            url=self.url_other,
            ignore_raises=False)
"""
