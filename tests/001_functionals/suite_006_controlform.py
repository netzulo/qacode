# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_base import ControlBase
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
        cls.add_property(
            'app', value=cls.settings_app('qadmin'))
        # page
        cls.add_property(
            'page', value=cls.settings_page('qacode_login'))
        cls.add_property(
            'url', value=cls.page.get('url'))
        cls.add_property(
            'form_login',
            value=cls.settings_control('form_login'))
        cls.add_property(
            'txt_username',
            value=cls.settings_control('txt_username'))
        cls.add_property(
            'txt_password',
            value=cls.settings_control('txt_password'))
        cls.add_property(
            'btn_submit',
            value=cls.settings_control('btn_submit'))
        # page_inputs
        cls.add_property(
            'page_inputs', value=cls.settings_page('qacode_inputs'))
        cls.add_property(
            'url_inputs', value=cls.page_inputs.get('url'))
        cls.add_property(
            'dd_base',
            value=cls.settings_control('dd_base'))
        cls.add_property(
            'dd_multiple',
            value=cls.settings_control('dd_multiple'))
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
    @pytest.mark.parametrize("selector", ["#txtTest002"])
    @pytest.mark.parametrize("instance", ["ControlForm"])
    @pytest.mark.parametrize("on_instance_search", [True])
    @pytest.mark.parametrize("on_instance_load", [True])
    @pytest.mark.parametrize("auto_reload", [True])
    @pytest.mark.parametrize("on_instance_strict", [True, False])
    @pytest.mark.parametrize("strict_rules", [
        [
            {"tag": "select", "type": "tag", "severity": "hight"}
        ]
    ])
    def test_instance_form(self, selector, instance, on_instance_search,
                           on_instance_load, on_instance_strict, strict_rules,
                           auto_reload):
        """Testcase: test_001_instance_selector"""
        control_config = {
            "name": "txt_username_strict",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
            "on_instance_search": on_instance_search,
            "on_instance_load": on_instance_load,
            "auto_reload": auto_reload,
            "on_instance_strict": on_instance_strict,
            "strict_rules": strict_rules
        }
        control = ControlForm(self.bot, **control_config)
        self.assert_is_instance(control, ControlBase)
        self.assert_is_instance(control, ControlForm)
        self.assert_is_instance(control.element, WebElement)
        self.assert_equals(
            control.selector, control_config.get('selector'))
        self.assert_equals(
            control.name, control_config.get('name'))
        self.assert_equals(
            control.locator, control_config.get('locator'))
        self.assert_equals(
            control.on_instance_search,
            control_config.get('on_instance_search'))
        self.assert_equals(
            control.on_instance_load,
            control_config.get('on_instance_load'))
        self.assert_equals(
            control.auto_reload,
            control_config.get('auto_reload'))
        self.assert_equals(
            control.instance,
            control_config.get('instance'))
        self.assert_equals(
            control.on_instance_strict,
            control_config.get('on_instance_strict'))
        self.assert_equals(
            len(control.strict_rules),
            len(control_config.get('strict_rules')))
        if control.tag == 'select' and on_instance_strict:
            self.assert_is_instance(
                control.dropdown,
                Select)
        elif control.tag == 'select' and not on_instance_strict:
            self.assert_none(
                control.dropdown)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("selector", ["#txtTest002"])
    @pytest.mark.parametrize("instance", ["ControlForm"])
    @pytest.mark.parametrize("auto_reload", [True])
    def test_method_reload_form(self, selector, instance, auto_reload):
        """Testcase: test_method_setcssrule"""
        # must be supported
        control_config = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
            "auto_reload": auto_reload,
            "on_instance_search": False,
            "on_instance_load": False,
            "on_instance_strict": False,
            "strict_rules": [],
        }
        control = ControlForm(self.bot, **control_config)
        self.assert_equals(control.on_instance_search, False)
        self.assert_equals(control.on_instance_load, False)
        self.assert_equals(control.on_instance_strict, False)
        self.assert_none(control.element)
        # Real test behaviour
        update_config = {
            "on_instance_search": True,
            "on_instance_load": True,
            "on_instance_strict": True,
        }
        control_config.update(update_config)
        control.reload(**control_config)
        self.assert_equals(control.on_instance_search, True)
        self.assert_equals(control.on_instance_load, True)
        self.assert_equals(control.on_instance_strict, True)
        self.assert_is_instance(control.element, WebElement)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1", "Link 1.2"])
    def test_method_dropdown_select_by_text(self, text):
        """Testcase: test_method_dropdown_select_by_text"""
        control = ControlForm(self.bot, **self.dd_base)
        control.dropdown_select(text)
        # TODO: an assert here

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["1", "2"])
    def test_method_dropdown_select_by_value(self, text):
        """Testcase: test_method_dropdown_select_by_value"""
        control = ControlForm(self.bot, **self.dd_base)
        control.dropdown_select(text, by_value=True)
        # TODO: an assert here

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [0, 1])
    def test_method_dropdown_select_by_index(self, index):
        """Testcase: test_method_dropdown_select_by_index"""
        control = ControlForm(self.bot, **self.dd_base)
        control.dropdown_select(index, by_index=True)
        # TODO: an assert here

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["Link 1.1", "Link 1.2"])
    def test_method_dropdown_deselect_by_text(self, text):
        """Testcase: test_method_dropdown_deselect_by_text"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(text)
        control.dropdown_deselect(text)
        # TODO: an assert here

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("text", ["1", "2"])
    def test_method_dropdown_deselect_by_value(self, text):
        """Testcase: test_method_dropdown_deselect_by_value"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(text, by_value=True)
        control.dropdown_deselect(text, by_value=True)
        # TODO: an assert here

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("index", [0, 1])
    def test_method_dropdown_deselect_by_index(self, index):
        """Testcase: test_method_dropdown_deselect_by_index"""
        control = ControlForm(self.bot, **self.dd_multiple)
        control.dropdown_select(index, by_index=True)
        control.dropdown_deselect(index, by_index=True)
        # TODO: an assert here

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_dropdown_deselect_all(self):
        """Testcase: test_method_dropdown_deselect_all"""
        texts = ["Link 1.1", "Link 1.2"]
        control = ControlForm(self.bot, **self.dd_multiple)
        for text in texts:
            control.dropdown_select(text)
        control.dropdown_deselect_all()
        # TODO: an assert here
