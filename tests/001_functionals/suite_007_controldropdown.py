# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_dropdown import ControlDropdown
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


ASSERT = Assert()
SETTINGS = settings(file_path="qacode/configs/")
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']['control_dropdown']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'


class TestControlDropdown(TestInfoBotUnique):
    """Test Suite for ControlBase class"""

    # app from config
    app = None
    # page from config: app
    page = None
    url = None
    # page from config: app
    page_inputs = None
    url_inputs = None
    # elements from config: page
    form_login = None
    txt_username = None
    txt_password = None
    btn_submit = None
    # elements from config: page_inputs
    dd_base = None
    dd_multiple = None

    @classmethod
    def setup_class(cls, **kwargs):
        """Setup class (suite) to be executed"""
        super(TestControlDropdown, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_CONTROLS)
        cls.add_property('app', cls.cfg_app('qadmin'))
        # page
        cls.add_property('page', cls.cfg_page('qacode_login'))
        cls.add_property('url', cls.page.get('url'))
        cls.add_property('form_login', cls.cfg_control('form_login'))
        cls.add_property('txt_username', cls.cfg_control('txt_username'))
        cls.add_property('txt_password', cls.cfg_control('txt_password'))
        cls.add_property('btn_submit', cls.cfg_control('btn_submit'))
        # page_inputs
        cls.add_property('page_inputs', cls.cfg_page('qacode_inputs'))
        cls.add_property('url_inputs', cls.page_inputs.get('url'))
        cls.add_property('dd_base', cls.cfg_control('dd_base'))
        cls.add_property('dd_multiple', cls.cfg_control('dd_multiple'))
        # start setup
        cls.bot.navigation.get_url(cls.url)
        # login
        txt_username = cls.bot.navigation.find_element(
            cls.txt_username.get('selector'))
        txt_password = cls.bot.navigation.find_element(
            cls.txt_password.get('selector'))
        btn_submit = cls.bot.navigation.find_element(
            cls.btn_submit.get('selector'))
        txt_username.send_keys('admin')
        txt_password.send_keys('admin')
        btn_submit.click()

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlDropdown, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("on_instance_search", [True, False])
    @pytest.mark.parametrize("auto_reload", [True, False])
    @pytest.mark.parametrize("rules", [
        [{"tag": "select", "type": "tag", "severity": "hight"}],
        []
    ])
    def test_controldropdown_instance(self, on_instance_search,
                                      rules, auto_reload):
        """Testcase: test_001_instance_selector"""
        cfg = self.dd_base
        cfg.update({
            "instance": "ControlDropdown",
            "on_instance_search": on_instance_search,
            "auto_reload": auto_reload,
            "rules": rules
        })
        # functional testcases
        ctl = ControlDropdown(self.bot, **cfg)
        ASSERT.is_instance(ctl, ControlDropdown)
        ASSERT.equals(ctl.selector, cfg.get('selector'))
        ASSERT.equals(ctl.name, cfg.get('name'))
        ASSERT.equals(ctl.locator, 'css selector')
        ASSERT.equals(
            ctl.on_instance_search, cfg.get('on_instance_search'))
        ASSERT.equals(ctl.auto_reload, cfg.get('auto_reload'))
        if on_instance_search:
            ASSERT.is_instance(ctl.element, WebElement)
        if auto_reload is not None:
            ASSERT.none(ctl.dropdown)
            ctl.reload(**ctl.settings)
            ASSERT.is_instance(ctl.dropdown, Select)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("auto_reload", [True, False])
    def test_method_reload_form(self, auto_reload):
        """Testcase: test_method_reload_form"""
        # must be supported
        cfg = self.dd_base
        cfg.update({
            "auto_reload": auto_reload,
            "on_instance_search": False,
        })
        ctl = ControlDropdown(self.bot, **cfg)
        ASSERT.equals(ctl.on_instance_search, False)
        ASSERT.none(ctl.element)
        ASSERT.none(ctl.dropdown)
        # Real test behaviour
        cfg.update({"on_instance_search": True})
        ctl.reload(**cfg)
        ASSERT.equals(ctl.on_instance_search, True)
        ASSERT.is_instance(ctl.element, WebElement)
        ASSERT.is_instance(ctl.dropdown, Select)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1", "Link 1.2"])
    def test_method_select_by_text(self, text):
        """Testcase: test_method_select_by_text"""
        control = ControlDropdown(self.bot, **self.dd_base)
        control.select(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_select_reload(self, text):
        """Testcase: test_method_select_reload"""
        control = ControlDropdown(self.bot, **self.dd_base)
        control.element = None
        control.select(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_select_notdropdown(self, text):
        """Testcase: test_method_select_notdropdown"""
        control = ControlDropdown(self.bot, **self.dd_base)
        control.dropdown = None
        control.select(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_select_badparams(self, text):
        """Testcase: test_method_select_badparams"""
        control = ControlDropdown(self.bot, **self.dd_base)
        control.element = None
        with pytest.raises(ControlException):
            control.select(text, by_value=True, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["1", "2"])
    def test_method_select_by_value(self, text):
        """Testcase: test_method_select_by_value"""
        control = ControlDropdown(self.bot, **self.dd_base)
        control.select(text, by_value=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [0, 1])
    def test_method_select_by_index(self, index):
        """Testcase: test_method_select_by_index"""
        control = ControlDropdown(self.bot, **self.dd_base)
        control.select(index, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [{}, [], None])
    def test_method_select_by_index_raises(self, index):
        """Testcase: test_method_select_by_index_raises"""
        control = ControlDropdown(self.bot, **self.dd_base)
        with pytest.raises(ControlException):
            control.select(index, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1", "Link 1.2"])
    def test_method_deselect_by_text(self, text):
        """Testcase: test_method_deselect_by_text"""
        control = ControlDropdown(self.bot, **self.dd_multiple)
        control.select(text)
        control.deselect(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_deselect_reload(self, text):
        """Testcase: test_method_deselect_reload"""
        control = ControlDropdown(self.bot, **self.dd_multiple)
        control.select(text)
        control.element = None
        control.deselect(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_deselect_notdropdown(self, text):
        """Testcase: test_method_deselect_notdropdown"""
        control = ControlDropdown(self.bot, **self.dd_multiple)
        control.select(text)
        control.dropdown = None
        control.deselect(text)
        ASSERT.is_instance(control.dropdown, Select)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_deselect_badparams(self, text):
        """Testcase: test_method_deselect_badparams"""
        control = ControlDropdown(self.bot, **self.dd_multiple)
        control.select(text)
        with pytest.raises(ControlException):
            control.deselect(text, by_value=True, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["1", "2"])
    def test_method_deselect_by_value(self, text):
        """Testcase: test_method_deselect_by_value"""
        control = ControlDropdown(self.bot, **self.dd_multiple)
        control.select(text, by_value=True)
        control.deselect(text, by_value=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [0, 1])
    def test_method_deselect_by_index(self, index):
        """Testcase: test_method_deselect_by_index"""
        control = ControlDropdown(self.bot, **self.dd_multiple)
        control.select(index, by_index=True)
        control.deselect(index, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", [{}, []])
    def test_method_deselect_by_index_raises(self, text):
        """Testcase: test_method_deselect_by_text"""
        control = ControlDropdown(self.bot, **self.dd_multiple)
        control.select(0, by_index=True)
        with pytest.raises(ControlException):
            control.deselect(text, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_deselect_all(self):
        """Testcase: test_method_deselect_all"""
        texts = ["Link 1.1", "Link 1.2"]
        control = ControlDropdown(self.bot, **self.dd_multiple)
        for text in texts:
            control.select(text)
        control.deselect_all()

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_deselect_all_reload(self):
        """Testcase: test_method_deselect_all_reload"""
        texts = ["Link 1.1", "Link 1.2"]
        control = ControlDropdown(self.bot, **self.dd_multiple)
        for text in texts:
            control.select(text)
        control.element = None
        control.deselect_all()

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_deselect_all_notdropdown(self):
        """Testcase: test_method_deselect_all_notdropdown"""
        texts = ["Link 1.1", "Link 1.2"]
        control = ControlDropdown(self.bot, **self.dd_multiple)
        for text in texts:
            control.select(text)
        control.dropdown = None
        control.deselect_all()
        ASSERT.is_instance(control.dropdown, Select)
