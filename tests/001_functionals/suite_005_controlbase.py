# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_base import ControlBase
from qautils.files import settings
from selenium.webdriver.remote.webelement import WebElement


SETTINGS = settings(file_path="qacode/configs/")
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']['control_base']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'


class TestControlBase(TestInfoBotUnique):
    """Test Suite for ControlBase class"""

    # app from config
    app = None
    # page from config
    page = None
    url = None
    # elements from config
    form_login = None
    txt_username = None
    txt_password = None
    btn_submit = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestControlBase, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_CONTROLS)

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))
        self.add_property(
            'app', value=self.settings_app('qadmin'))
        self.add_property(
            'page', value=self.settings_page('qacode_login'))
        self.add_property(
            'url', value=self.page.get('url'))
        self.add_property(
            'txt_username',
            value=self.settings_control('txt_username'))
        self.add_property(
            'txt_password',
            value=self.settings_control('txt_password'))
        self.add_property(
            'btn_submit',
            value=self.settings_control('btn_submit'))
        self.add_property(
            'form_login',
            value=self.settings_control('form_login'))
        self.bot.navigation.get_url(self.url)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("selector", ["#txtUsername-field"])
    @pytest.mark.parametrize("instance", ["ControlBase"])
    @pytest.mark.parametrize("on_instance_search", [False, True])
    @pytest.mark.parametrize("on_instance_load", [False, True])
    @pytest.mark.parametrize("auto_reload", [True])
    def test_instance_base(self, selector, instance, on_instance_search,
                           on_instance_load, auto_reload):
        """Testcase: test_instance_base"""
        # must be supported at: test_instance_raises_base
        if not on_instance_search and on_instance_load:
            pytest.skip("Test must be supported at: test_instance_raises_base")
        # must be supported
        control_config = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
            "on_instance_search": on_instance_search,
            "on_instance_load": on_instance_load,
            "auto_reload": auto_reload,
        }
        control = ControlBase(self.bot, **control_config)
        self.assert_is_instance(control, ControlBase)
        if on_instance_search and on_instance_load:
            self.assert_equals(control.tag, 'input')
        if on_instance_search:
            self.assert_is_instance(control.element, WebElement)
        else:
            self.assert_none(control.element)
        # main config
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

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("on_instance_load", [None])
    @pytest.mark.parametrize("on_instance_search", [None, True])
    @pytest.mark.parametrize("instance", ["ControlBase"])
    @pytest.mark.parametrize("selector", [None, "#txtUsername-field"])
    @pytest.mark.parametrize("auto_reload", [False])
    def test_instance_base_raises(self, selector, instance, on_instance_search,
                                  on_instance_load, auto_reload):
        """Testcase: test_instance_raises_base"""
        # must be supported at: test_instance_base
        if on_instance_search and on_instance_load is None:
            pytest.skip("Test must be supported at: test_instance_base")
        # must be supported
        control_config = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
            "on_instance_search": on_instance_search,
            "on_instance_load": on_instance_load,
            "auto_reload": auto_reload,
        }
        if (
                on_instance_search is None and
                on_instance_load is None and
                selector is not None):
            control = ControlBase(self.bot, **control_config)
            # main config
            self.assert_equals(
                control.selector, control_config.get('selector'))
            self.assert_equals(control.name, control_config.get('name'))
            self.assert_equals(
                control.locator, control_config.get('locator'))
            self.assert_equals(control.on_instance_search, False)
            self.assert_equals(control.on_instance_load, False)
            self.assert_none(control.element)
            return True
        pytest.raises(
            ControlException,
            ControlBase, self.bot,
            **control_config)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_instance_raises_nonebot(self):
        """Testcase: test_instance_raises_nonebot"""
        self.assert_raises(
            ControlException,
            ControlBase,
            None)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_instance_raises_nonesettings(self):
        """Testcase: test_instance_raises_nonesettings"""
        self.assert_raises(
            ControlException,
            ControlBase,
            self.bot)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_findchild(self):
        """Testcase: test_method_findchild"""
        cfg_parent = self.form_login.copy()
        child_selector = self.settings_control(
            'txt_username').get('selector')
        control = ControlBase(self.bot, **cfg_parent)
        self.assert_is_instance(
            control.find_child(child_selector),
            ControlBase)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_gettext(self):
        """Testcase: test_property_gettext"""
        cfg_btn = self.btn_submit.copy()
        cfg_btn.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_btn)
        self.assert_equals(control.text, 'Login')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_raises_gettext(self):
        """Testcase: test_property_raises_gettext"""
        cfg_btn = self.btn_submit.copy()
        control = ControlBase(self.bot, **cfg_btn)
        self.assert_equals(control.text, None)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_gettext(self):
        """Testcase: test_method_gettext"""
        cfg_btn = self.btn_submit.copy()
        cfg_btn.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_btn)
        self.assert_equals(control.get_text(), 'Login')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_attr_id(self):
        """Testcase: test_property_attr_id"""
        cfg_input = self.txt_username.copy()
        cfg_input.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_input)
        self.assert_not_none(control.attr_id)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_attr_class(self):
        """Testcase: test_property_attr_class"""
        cfg_form = self.form_login.copy()
        cfg_form.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_form)
        self.assert_in('ember-view', control.attr_class)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_getattrvalue(self):
        """Testcase: test_method_getattrvalue"""
        cfg_form = self.form_login.copy()
        cfg_form.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_form)
        self.assert_not_none(control.get_attr_value('id'))

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_get_attrs(self):
        """Testcase: test_method_get_attrs"""
        cfg_form = self.form_login.copy()
        cfg_form.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_form)
        attrs = control.get_attrs(['id', 'class'])
        self.assert_equals(attrs[0]['name'], 'id')
        self.assert_equals(attrs[0]['value'], 'frmLogin')
        self.assert_equals(attrs[1]['name'], 'class')
        self.assert_in('ember-view', attrs[1]['value'])

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_tag(self):
        """Testcase: test_property_tag"""
        cfg_form = self.form_login.copy()
        cfg_form.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_form)
        self.assert_equals(control.tag, 'form')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("control_name", ['txt_username'])
    @pytest.mark.parametrize("clear", [True, False])
    @pytest.mark.parametrize(
        "control_config",
        [
            {"on_instance_load": True},
            {
                "on_instance_search": False,
                "on_instance_load": False,
                "auto_reload": True
            }
        ])
    def test_method_typetext(self, control_name, control_config, clear):
        """Testcase: test_method_typetext_cleartrue"""
        text_to_type = 'test'
        ctl_config = getattr(self, control_name).copy()
        ctl_config.update(control_config)
        control = ControlBase(self.bot, **ctl_config)
        control.type_text(text_to_type, clear=clear)
        self.assert_equals(control.text, text_to_type)
        self.assert_equals(control.get_attr_value('value'), text_to_type)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_getcssvalue(self):
        """Testcase: test_method_getcssvalue"""
        cfg_input = self.txt_username.copy()
        cfg_input.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_input)
        self.assert_equals(
            control.get_css_value('color'),
            'rgba(73, 80, 87, 1)')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_setcssrule(self):
        """Testcase: test_method_setcssrule"""
        cfg_input = self.txt_username.copy()
        cfg_input.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_input)
        control.type_text('test')
        control.set_css_value('color', 'red')
        self.assert_equals(
            control.get_css_value('color'),
            'rgba(255, 0, 0, 1)')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_gettext_onscreenfalse(self):
        """Testcase: test_method_gettext_onscreenfalse"""
        msg_err = 'Failed at obtain text, open issue on Github'
        cfg_btn = self.btn_submit.copy()
        cfg_btn.update({"on_instance_load": True})
        control = ControlBase(self.bot, **cfg_btn)
        control.set_css_value('display', 'none')
        text = control.get_text(on_screen=False)
        self.assert_greater(len(text), 0, msg=msg_err)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("selector", ["#txtUsername-field"])
    @pytest.mark.parametrize("instance", ["ControlBase"])
    def test_method_reload_base(self, selector, instance):
        """Testcase: test_method_setcssrule"""
        # must be supported
        cfg_base = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
            "on_instance_search": False,
            "on_instance_load": False,
        }
        control = ControlBase(self.bot, **cfg_base)
        self.assert_equals(control.on_instance_search, False)
        self.assert_equals(control.on_instance_load, False)
        self.assert_none(control.element)
        # Real test behaviour
        cfg_update = {
            "on_instance_search": True,
            "on_instance_load": True
        }
        cfg_base.update(cfg_update)
        control.reload(**cfg_base)
        self.assert_equals(control.on_instance_search, True)
        self.assert_equals(control.on_instance_load, True)
        self.assert_is_instance(control.element, WebElement)
