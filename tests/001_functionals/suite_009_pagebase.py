# -*- coding: utf-8 -*-
"""Package for suites and tests related to qacode.core.webs.pages package"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.pages.page_base import PageBase
from qacode.utils import settings


ASSERT = Assert()
SETTINGS = settings(file_path="qacode/configs/")
SKIP_PAGES = SETTINGS['tests']['skip']['web_pages']
SKIP_PAGES_MSG = 'web_pages DISABLED by config file'


class TestPageBase(TestInfoBotUnique):
    """Test Suite for class NavBase"""

    # app from config
    app = None
    # page from config: qacode_logout
    page = None
    url = None
    # page from config: qacode_login
    page_base = None
    # elements from config: page
    form_login = None
    txt_username = None
    txt_password = None
    btn_submit = None

    @classmethod
    def setup_class(cls, **kwargs):
        """Setup class (suite) to be executed"""
        super(TestPageBase, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_PAGES)

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestPageBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))
        self.add_property('app', self.cfg_app('qadmin'))
        # page
        self.add_property('page', self.cfg_page('qacode_logout'))
        self.add_property('url', self.page.get('url'))
        self.add_property('btn_logout', self.cfg_control('btn_logout'))
        self.add_property('btn_login', self.cfg_control('btn_login'))
        self.add_property('page_base', self.cfg_page('qacode_login'))
        self.bot.navigation.get_url(self.page_base.get('url'))

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_instance_url(self):
        """Testcase: test_001_instance_url"""
        cfg = self.page.copy()
        cfg.update({
            "go_url": True
        })
        page = PageBase(self.bot, **cfg)
        ASSERT.is_instance(page, PageBase)
        ASSERT.equals(
            self.bot.curr_driver.current_url,
            self.page.get('url'))

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_instance_notgourl(self):
        """Testcase: test_002_instance_notgourl"""
        cfg = self.page.copy()
        cfg.update({
            "go_url": False, "controls": []
        })
        page = PageBase(self.bot, **cfg)
        ASSERT.is_instance(page, PageBase)
        ASSERT.not_equals(
            self.bot.curr_driver.current_url, cfg.get('url'))

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_instance_element(self):
        """Testcase: test_003_instance_element"""
        cfg = self.page.copy()
        page = PageBase(self.bot, **cfg)
        ASSERT.is_instance(page, PageBase)
        ASSERT.equals(
            self.bot.curr_driver.current_url,
            cfg.get('url'))
        for control in self.page.get('controls'):
            name = control.get('name')
            ASSERT.in_list(name, dir(page))
            element = page.__dict__[name]
            ASSERT.is_instance(element, ControlBase)

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_instance_maximized(self):
        """Testcase: test_004_instance_maximized"""
        cfg = self.page.copy()
        cfg.update({
            "go_url": True,
            "maximize": True,
            "controls": []
        })
        page = PageBase(self.bot, **cfg)
        ASSERT.is_instance(page, PageBase)
        ASSERT.equals(
            self.bot.curr_driver.current_url,
            cfg.get('url'))

    @pytest.mark.skipIf(SKIP_PAGES, SKIP_PAGES_MSG)
    def test_method_getelement(self):
        """Testcase: test_004_instance_maximized"""
        cfg = self.page.copy()
        page = PageBase(self.bot, **cfg)
        ASSERT.is_instance(page, PageBase)
        ASSERT.equals(
            self.bot.curr_driver.current_url,
            cfg.get('url'))
        for config_control in self.page.get('controls'):
            name = config_control.get('name')
            instance_name = config_control.get('instance')
            ctl = page.get_element(config_control)
            ASSERT.in_list(name, dir(page))
            if instance_name == 'ControlBase':
                ASSERT.is_instance(ctl, ControlBase)
