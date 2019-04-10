# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_form import ControlForm
from qautils.files import settings
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


SETTINGS = settings(file_path="qacode/configs/")
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']['control_form']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'


class TestControlForm(TestInfoBotUnique):
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
        """TODO: doc method"""
        super(TestControlForm, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_CONTROLS)
        cls.add_property('app', cls.settings_app('qadmin'))
        # page
        cls.add_property('page', cls.settings_page('qacode_login'))
        cls.add_property('url', cls.page.get('url'))
        cls.add_property('form_login', cls.settings_control('form_login'))
        cls.add_property('txt_username', cls.settings_control('txt_username'))
        cls.add_property('txt_password', cls.settings_control('txt_password'))
        cls.add_property('btn_submit', cls.settings_control('btn_submit'))
        # page_inputs
        cls.add_property('page_inputs', cls.settings_page('qacode_inputs'))
        cls.add_property('url_inputs', cls.page_inputs.get('url'))
        cls.add_property('dd_base', cls.settings_control('dd_base'))
        cls.add_property('dd_multiple', cls.settings_control('dd_multiple'))
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
        super(TestControlForm, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("on_instance_search", [True, False])
    @pytest.mark.parametrize("auto_reload", [True, False])
    @pytest.mark.parametrize("strict_rules", [
        [{"tag": "select", "type": "tag", "severity": "hight"}]
    ])
    def test_controlform_instance(self, on_instance_search,
                                  strict_rules, auto_reload):
        """Testcase: test_001_instance_selector"""
        cfg = self.dd_base
        cfg.update({
            "instance": "ControlForm",
            "on_instance_search": on_instance_search,
            "auto_reload": auto_reload,
            "strict_rules": strict_rules
        })
        # functional testcases
        ctl = ControlForm(self.bot, **cfg)
        self.assert_is_instance(ctl, ControlForm)
        self.assert_equals(ctl.selector, cfg.get('selector'))
        self.assert_equals(ctl.instance, cfg.get('instance'))
        self.assert_equals(ctl.name, cfg.get('name'))
        self.assert_equals(ctl.locator, 'css selector')
        self.assert_equals(
            ctl.on_instance_search, cfg.get('on_instance_search'))
        self.assert_equals(ctl.auto_reload, cfg.get('auto_reload'))
        self.assert_equals(
            len(ctl.strict_rules), len(cfg.get('strict_rules')))
        if on_instance_search:
            self.assert_is_instance(ctl.element, WebElement)
        if ctl.tag == 'select':
            self.assert_is_instance(ctl.dropdown, Select)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("auto_reload", [True, False])
    def test_method_reload_form(self, auto_reload):
        """Testcase: test_method_setcssrule"""
        # must be supported
        cfg = self.dd_base
        cfg.update({
            "auto_reload": auto_reload,
            "on_instance_search": False,
        })
        ctl = ControlForm(self.bot, **cfg)
        self.assert_equals(ctl.on_instance_search, False)
        self.assert_none(ctl.element)
        self.assert_none(ctl.dropdown)
        # Real test behaviour
        cfg.update({"on_instance_search": True})
        ctl.reload(**cfg)
        self.assert_equals(ctl.on_instance_search, True)
        self.assert_is_instance(ctl.element, WebElement)
        self.assert_is_instance(ctl.dropdown, Select)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1", "Link 1.2"])
    def test_method_dropdown_select_by_text(self, text):
        """Testcase: test_method_dropdown_select_by_text"""
        control = ControlForm(self.bot, **self.dd_base)
        control.dropdown_select(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_dropdown_select_reload(self, text):
        """Testcase: test_method_dropdown_select_reload"""
        control = ControlForm(self.bot, **self.dd_base)
        control.element = None
        control.dropdown_select(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_dropdown_select_notdropdown(self, text):
        """Testcase: test_method_dropdown_select_notdropdown"""
        control = ControlForm(self.bot, **self.dd_base)
        control.dropdown = None
        with pytest.raises(ControlException):
            control.dropdown_select(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_dropdown_select_badparams(self, text):
        """Testcase: test_method_dropdown_select_badparams"""
        control = ControlForm(self.bot, **self.dd_base)
        control.element = None
        with pytest.raises(ControlException):
            control.dropdown_select(text, by_value=True, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["1", "2"])
    def test_method_dropdown_select_by_value(self, text):
        """Testcase: test_method_dropdown_select_by_value"""
        control = ControlForm(self.bot, **self.dd_base)
        control.dropdown_select(text, by_value=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [0, 1])
    def test_method_dropdown_select_by_index(self, index):
        """Testcase: test_method_dropdown_select_by_index"""
        control = ControlForm(self.bot, **self.dd_base)
        control.dropdown_select(index, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [{}, [], None])
    def test_method_dropdown_select_by_index_raises(self, index):
        """Testcase: test_method_dropdown_select_by_index_raises"""
        control = ControlForm(self.bot, **self.dd_base)
        with pytest.raises(ControlException):
            control.dropdown_select(index, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1", "Link 1.2"])
    def test_method_dropdown_deselect_by_text(self, text):
        """Testcase: test_method_dropdown_deselect_by_text"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(text)
        control.dropdown_deselect(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_dropdown_deselect_reload(self, text):
        """Testcase: test_method_dropdown_deselect_reload"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(text)
        control.element = None
        control.dropdown_deselect(text)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_dropdown_deselect_notdropdown(self, text):
        """Testcase: test_method_dropdown_deselect_notdropdown"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(text)
        control.dropdown = None
        control.dropdown_deselect(text)
        self.assert_is_instance(control.dropdown, Select)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1"])
    def test_method_dropdown_deselect_badparams(self, text):
        """Testcase: test_method_dropdown_deselect_badparams"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(text)
        with pytest.raises(ControlException):
            control.dropdown_deselect(text, by_value=True, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["1", "2"])
    def test_method_dropdown_deselect_by_value(self, text):
        """Testcase: test_method_dropdown_deselect_by_value"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(text, by_value=True)
        control.dropdown_deselect(text, by_value=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [0, 1])
    def test_method_dropdown_deselect_by_index(self, index):
        """Testcase: test_method_dropdown_deselect_by_index"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(index, by_index=True)
        control.dropdown_deselect(index, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", [{}, []])
    def test_method_dropdown_deselect_by_index_raises(self, text):
        """Testcase: test_method_dropdown_deselect_by_text"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(0, by_index=True)
        with pytest.raises(ControlException):
            control.dropdown_deselect(text, by_index=True)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_dropdown_deselect_all(self):
        """Testcase: test_method_dropdown_deselect_all"""
        texts = ["Link 1.1", "Link 1.2"]
        control = ControlForm(self.bot, **self.dd_multiple)
        for text in texts:
            control.dropdown_select(text)
        control.dropdown_deselect_all()

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_dropdown_deselect_all_reload(self):
        """Testcase: test_method_dropdown_deselect_all_reload"""
        texts = ["Link 1.1", "Link 1.2"]
        control = ControlForm(self.bot, **self.dd_multiple)
        for text in texts:
            control.dropdown_select(text)
        control.element = None
        control.dropdown_deselect_all()

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_dropdown_deselect_all_notdropdown(self):
        """Testcase: test_method_dropdown_deselect_all_notdropdown"""
        texts = ["Link 1.1", "Link 1.2"]
        control = ControlForm(self.bot, **self.dd_multiple)
        for text in texts:
            control.dropdown_select(text)
        control.dropdown = None
        control.dropdown_deselect_all()
        self.assert_is_instance(control.dropdown, Select)
