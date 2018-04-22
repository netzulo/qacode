# -*- coding: utf-8 -*-
"""Package for suites and tests related to qacode.core.webs.pages package"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.utils import settings
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_form import ControlForm
from qacode.core.webs.pages.page_base import PageBase


SETTINGS = settings()
SKIP_PAGES = SETTINGS['tests']['skip']['web_pages']
SKIP_PAGES_MSG = 'web_pages DISABLED by config file'


class TestPageBase(TestInfoBotUnique):
    """Test Suite for class NavBase"""

    app = None
    page_base_config = None
    page_login_config = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestPageBase, cls).setup_class(
            config=settings(),
            skip_force=SKIP_PAGES)

    def setup_method(self, test_method, close=True):
        """Unload self.attribute"""
        super(TestPageBase, self).setup_method(
            test_method, config=settings())
        self.add_property('app', self.settings_app('pages_tests'))
        self.page_base_config = self.settings_page('page_base')
        self.page_login_config = self.settings_page('page_login')

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_instance_url(self):
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
    def test_instance_notgourl(self):
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
    def test_instance_element(self):
        """Testcase: test_003_instance_element"""
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
    def test_instance_maximized(self):
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
    def test_method_getelement(self):
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
