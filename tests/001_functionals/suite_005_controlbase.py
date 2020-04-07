# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_base import ControlBase
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement


ASSERT = Assert()
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
        """Setup class (suite) to be executed"""
        super(TestControlBase, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_CONTROLS)

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))
        self.add_property('app', self.cfg_app('qadmin'))
        self.add_property('page', self.cfg_page('qacode_login'))
        self.add_property('url', self.page.get('url'))
        self.add_property('txt_username', self.cfg_control('txt_username'))
        self.add_property('txt_password', self.cfg_control('txt_password'))
        self.add_property('btn_submit', self.cfg_control('btn_submit'))
        self.add_property('form_login', self.cfg_control('form_login'))
        self.add_property('lst_ordered', self.cfg_control('lst_ordered'))
        self.add_property(
            'lst_ordered_child', self.cfg_control('lst_ordered_child'))
        self.add_property('dd_menu_data', self.cfg_control('dd_menu_data'))
        self.add_property(
            'dd_menu_data_lists', self.cfg_control('dd_menu_data_lists'))
        self.bot.navigation.get_url(self.url, wait_for_load=10)
        self.add_property(
            'btn_click_invisible', self.cfg_control('btn_click_invisible'))
        self.add_property(
            'btn_click_visible', self.cfg_control('btn_click_visible'))
        self.add_property('title_buttons', self.cfg_control('title_buttons'))

    def setup_login_to_inputs(self):
        """Do login before to exec some testcases"""
        # setup_login
        self.bot.navigation.get_url(self.page.get('url'), wait_for_load=10)
        txt_username = self.bot.navigation.find_element(
            self.txt_username.get("selector"))
        txt_password = self.bot.navigation.find_element(
            self.txt_password.get("selector"))
        btn_submit = self.bot.navigation.find_element(
            self.btn_submit.get("selector"))
        self.bot.navigation.ele_write(txt_username, "admin")
        self.bot.navigation.ele_write(txt_password, "admin")
        self.bot.navigation.ele_click(btn_submit)
        # end setup_login

    def setup_login_to_data(self):
        """Do login before to exec some testcases"""
        # setup_login
        self.bot.navigation.get_url(self.page.get('url'), wait_for_load=10)
        txt_username = self.bot.navigation.find_element(
            self.txt_username.get("selector"))
        txt_password = self.bot.navigation.find_element(
            self.txt_password.get("selector"))
        btn_submit = self.bot.navigation.find_element(
            self.btn_submit.get("selector"))
        self.bot.navigation.ele_write(txt_username, "admin")
        self.bot.navigation.ele_write(txt_password, "admin")
        self.bot.navigation.ele_click(btn_submit)
        self.bot.navigation.ele_click(
            self.bot.navigation.find_element_wait(
                self.dd_menu_data.get("selector")))
        self.bot.navigation.ele_click(
            self.bot.navigation.find_element_wait(
                self.dd_menu_data_lists.get("selector")))
        # end setup_login

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("on_instance_search", [True, False])
    @pytest.mark.parametrize("auto_reload", [True, False])
    def test_controlbase_instance(self, on_instance_search, auto_reload):
        """Testcase: test_instance_base"""
        tag_name = "input"
        cfg = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": "#txtUsername-field",
            "instance": "ControlBase",
            "on_instance_search": on_instance_search,
            "auto_reload": auto_reload,
        }
        # functional testcases
        ctl = ControlBase(self.bot, **cfg)
        ASSERT.is_instance(ctl, ControlBase)
        # main config
        ASSERT.equals(ctl.selector, cfg.get('selector'))
        ASSERT.equals(ctl.name, cfg.get('name'))
        ASSERT.equals(ctl.locator, cfg.get('locator'))
        ASSERT.equals(
            ctl.on_instance_search, cfg.get('on_instance_search'))
        ASSERT.equals(ctl.auto_reload, cfg.get('auto_reload'))
        if on_instance_search:
            ASSERT.is_instance(ctl.element, WebElement)
            ASSERT.equals(ctl.tag, tag_name)
        else:
            ASSERT.none(ctl.element)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_controlbase_instance_raises(self):
        """Testcase: test_instance_raises_base"""
        cfg = {
            "name": "controlbase_raises",
            "selector": None,
            "instance": None,
            "on_instance_search": None,
            "auto_reload": None,
        }
        with pytest.raises(CoreException):
            ControlBase(self.bot, **cfg)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_gettext(self):
        """Testcase: test_property_gettext"""
        cfg_btn = self.btn_submit.copy()
        cfg_btn.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_btn)
        ASSERT.equals(control.text, 'Login')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_gettext(self):
        """Testcase: test_method_gettext"""
        cfg_btn = self.btn_submit.copy()
        cfg_btn.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_btn)
        ASSERT.equals(control.get_text(), 'Login')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_getattrvalue(self):
        """Testcase: test_method_getattrvalue"""
        cfg_form = self.form_login.copy()
        cfg_form.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_form)
        ASSERT.not_none(control.get_attr_value('id'))

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_get_attrs(self):
        """Testcase: test_method_get_attrs"""
        cfg_form = self.form_login.copy()
        cfg_form.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_form)
        attrs = control.get_attrs(['id', 'class'])
        ASSERT.equals(attrs[0]['name'], 'id')
        ASSERT.equals(attrs[0]['value'], 'frmLogin')
        ASSERT.equals(attrs[1]['name'], 'class')
        ASSERT.in_list('ember-view', attrs[1]['value'])

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_tag(self):
        """Testcase: test_property_tag"""
        cfg_form = self.form_login.copy()
        cfg_form.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_form)
        ASSERT.equals(control.tag, 'form')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("retry", [False, True])
    def test_method_click(self, retry):
        """Testcase: test_method_click"""
        ctl_config = self.txt_username.copy()
        control = ControlBase(self.bot, **ctl_config)
        control.click(retry=retry)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("clear", [True, False])
    @pytest.mark.parametrize(
        "control_config",
        [
            {"on_instance_search": True},
            {"auto_reload": True}
        ])
    def test_method_typetext(self, control_config, clear):
        """Testcase: test_method_typetext_cleartrue"""
        text_to_type = 'test'
        ctl_config = self.txt_username.copy()
        ctl_config.update(control_config)
        control = ControlBase(self.bot, **ctl_config)
        control.type_text(text_to_type, clear=clear)
        ASSERT.equals(control.text, text_to_type)
        ASSERT.equals(control.get_attr_value('value'), text_to_type)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_getcssvalue(self):
        """Testcase: test_method_getcssvalue"""
        cfg_input = self.txt_username.copy()
        cfg_input.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_input)
        ASSERT.equals(
            control.get_css_value('color'),
            'rgba(73, 80, 87, 1)')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_setcssrule(self):
        """Testcase: test_method_setcssrule"""
        cfg_input = self.txt_username.copy()
        cfg_input.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_input)
        control.type_text('test')
        control.set_css_value('color', 'red')
        ASSERT.equals(
            control.get_css_value('color'),
            'rgba(255, 0, 0, 1)')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_gettext_onscreenfalse(self):
        """Testcase: test_method_gettext_onscreenfalse"""
        msg_err = 'Failed at obtain text, open issue on Github'
        cfg_btn = self.btn_submit.copy()
        cfg_btn.update({"on_instance_search": True})
        control = ControlBase(self.bot, **cfg_btn)
        control.set_css_value('display', 'none')
        text = control.get_text(on_screen=False)
        ASSERT.greater(len(text), 0, msg=msg_err)

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
        }
        control = ControlBase(self.bot, **cfg_base)
        ASSERT.equals(control.on_instance_search, False)
        ASSERT.none(control.element)
        # Real test behaviour
        cfg_base.update({"on_instance_search": True})
        control.reload(**cfg_base)
        ASSERT.equals(control.on_instance_search, True)
        ASSERT.is_instance(control.element, WebElement)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_findchild(self):
        """Testcase: test_method_findchild"""
        self.setup_login_to_data()
        control = ControlBase(self.bot, **self.lst_ordered)
        selector_child = self.lst_ordered_child.get("selector")
        ctl_child = control.find_child(selector_child)
        ASSERT.is_instance(ctl_child, ControlBase)
        ASSERT.is_instance(ctl_child.element, WebElement)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_findchildren(self):
        """Testcase: test_method_findchildren"""
        self.setup_login_to_data()
        control = ControlBase(self.bot, **self.lst_ordered)
        selector_child = self.lst_ordered_child.get("selector")
        children = control.find_children(selector_child)
        ASSERT.lower(len(children), 5)
        for ctl_child in children:
            ASSERT.is_instance(ctl_child, ControlBase)
            ASSERT.is_instance(ctl_child.element, WebElement)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_waitinvisible(self):
        """Testcase: test_method_waitinvisible"""
        self.setup_login_to_inputs()
        # end setup
        ctl = ControlBase(self.bot, **self.btn_click_invisible)
        ctl.click()
        ctl_invisible = ctl.wait_invisible(timeout=7)
        ASSERT.is_instance(ctl_invisible, ControlBase)
        ASSERT.is_instance(ctl_invisible.element, WebElement)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_waitvisible(self):
        """Testcase: test_method_waitvisible"""
        self.setup_login_to_inputs()
        ControlBase(self.bot, **self.btn_click_invisible).click()
        # end setup
        ctl = ControlBase(self.bot, **self.btn_click_visible)
        ctl_visible = ctl.wait_visible(timeout=7)
        ASSERT.is_instance(ctl_visible, ControlBase)
        ASSERT.is_instance(ctl_visible.element, WebElement)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_waitblink(self):
        """Testcase: test_method_waitblink"""
        self.setup_login_to_inputs()
        ctl = ControlBase(self.bot, **self.btn_click_invisible)
        ctl.click()
        # end setup
        ctl_blink = ctl.wait_blink(timeout=7)
        ASSERT.is_instance(ctl_blink, ControlBase)
        ASSERT.is_instance(ctl_blink.element, WebElement)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize(
        "ctl_cfg", [
            ("title_buttons", "Buttonss"),
            ("btn_click_invisible", "bad_text")
        ]
    )
    def test_method_waittext(self, ctl_cfg):
        """Testcase: test_method_waittext"""
        self.setup_login_to_inputs()
        ctl_setup = ControlBase(self.bot, **self.btn_click_invisible)
        ctl_setup.click()
        ctl_setup.wait_visible(timeout=7)
        # end setup
        ctl = ControlBase(self.bot, **getattr(self, ctl_cfg[0]))
        ctl.reload()
        ASSERT.true(ctl.wait_text(ctl_cfg[1], timeout=7))
        ASSERT.equals(ctl.text, ctl_cfg[1])
