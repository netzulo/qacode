# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.utils import settings
from qacode.core.webs.controls.control_base import ControlBase
from selenium.webdriver.remote.webelement import WebElement


SETTINGS = settings()
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'


class TestControlBase(TestInfoBotUnique):
    """Test Suite for ControlBase class"""

    app = None
    page_login_config = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestControlBase, cls).setup_class(
            config=settings(),
            skip_force=SKIP_CONTROLS)

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlBase, self).setup_method(
            test_method, config=settings())
        self.add_property(
            'app', value=self.settings_app('pages_tests'))
        self.add_property(
            'page_login_config', value=self.settings_page('page_login'))
        self.add_property(
            'url', value=self.page_login_config.get('url'))
        self.bot.navigation.get_url(self.url)
        curr_url = self.bot.curr_driver.current_url
        self.assert_equals_url(curr_url, self.url)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("selector", ["#username"])
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

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("on_instance_load", [None])
    @pytest.mark.parametrize("on_instance_search", [None, True])
    @pytest.mark.parametrize("instance", ["ControlBase"])
    @pytest.mark.parametrize("selector", [None, "#username"])
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
        login_container_config = self.settings_control('login_container')
        login_container_title_config = self.settings_control(
            'login_container_title')
        control = ControlBase(self.bot, **login_container_config)
        self.assert_is_instance(
            control.find_child(
                login_container_title_config.get('selector')),
            ControlBase)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_gettext(self):
        """Testcase: test_property_gettext"""
        login_container_title_config = self.settings_control(
            'login_container_title').copy()
        login_container_title_config.update({
            "on_instance_load": True
        })
        control = ControlBase(
            self.bot, **login_container_title_config)
        self.assert_equals(control.text, 'Login Page')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_raises_gettext(self):
        """Testcase: test_property_raises_gettext"""
        login_container_title_config = self.settings_control(
            'login_container_title')
        control = ControlBase(
            self.bot, **login_container_title_config)
        self.assert_equals(control.text, None)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_gettext(self):
        """Testcase: test_method_gettext"""
        login_container_title_config = self.settings_control(
            'login_container_title')
        login_container_title_config.update({
            "on_instance_load": True
        })
        control = ControlBase(
            self.bot, **login_container_title_config)
        self.assert_equals(control.get_text(), 'Login Page')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_attr_id(self):
        """Testcase: test_property_attr_id"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        self.assert_equals(control.attr_id, 'username')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_attr_class(self):
        """Testcase: test_property_attr_class"""
        login_container_config = self.settings_control(
            'login_container')
        login_container_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_config)
        self.assert_in('large-12', control.attr_class)
        self.assert_in('columns', control.attr_class)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_getattrvalue(self):
        """Testcase: test_method_getattrvalue"""
        login_container_config = self.settings_control(
            'login_container')
        login_container_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_config)
        self.assert_equals(control.get_attr_value('id'), 'content')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_get_attrs(self):
        """Testcase: test_method_get_attrs"""
        login_container_config = self.settings_control(
            'login_container')
        login_container_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_config)
        attrs = control.get_attrs(['id', 'class'])
        self.assert_equals(attrs[0]['name'], 'id')
        self.assert_equals(attrs[0]['value'], 'content')
        self.assert_equals(attrs[1]['name'], 'class')
        self.assert_in('large-12', attrs[1]['value'])
        self.assert_in('columns', attrs[1]['value'])

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_property_tag(self):
        """Testcase: test_property_tag"""
        login_container_config = self.settings_control(
            'login_container')
        login_container_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_config)
        self.assert_equals(control.tag, 'div')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_typetext_withproperty(self):
        """Testcase: test_method_typetext_withproperty"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        control.type_text('test')
        self.assert_equals(control.text, 'test')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_typetext_withmethod(self):
        """Testcase: test_method_typetext_withmethod"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        control.type_text('test')
        self.assert_equals(control.get_attr_value('value'), 'test')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_typetext_cleartrue(self):
        """Testcase: test_method_typetext_cleartrue"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        control.type_text('test', clear=True)
        self.assert_equals(control.get_attr_value('value'), 'test')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_getcssvalue(self):
        """Testcase: test_method_getcssvalue"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        self.assert_equals(
            control.get_css_value('color'), 'rgba(0, 0, 0, 0.75)')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_setcssrule(self):
        """Testcase: test_method_setcssrule"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        control.type_text('test')
        control.set_css_value('color', 'red')
        self.assert_equals(
            control.get_css_value('color'), 'rgba(255, 0, 0, 1)')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_method_gettext_onscreenfalse(self):
        """Testcase: test_method_gettext_onscreenfalse"""
        login_container_title_config = self.settings_control(
            'login_container_title')
        login_container_title_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_title_config)
        control.set_css_value('display', 'none')
        text = control.get_text(on_screen=False)
        self.assert_greater(
            len(text), 0, msg='Failed at obtain text, open issue on Github')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("selector", ["#username"])
    @pytest.mark.parametrize("instance", ["ControlBase"])
    def test_method_reload_base(self, selector, instance):
        """Testcase: test_method_setcssrule"""
        # must be supported
        control_config = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
            "on_instance_search": False,
            "on_instance_load": False,
        }
        control = ControlBase(self.bot, **control_config)
        self.assert_equals(control.on_instance_search, False)
        self.assert_equals(control.on_instance_load, False)
        self.assert_none(control.element)
        # Real test behaviour
        update_config = {
            "on_instance_search": True,
            "on_instance_load": True
        }
        control_config.update(update_config)
        control.reload(**control_config)
        self.assert_equals(control.on_instance_search, True)
        self.assert_equals(control.on_instance_load, True)
        self.assert_is_instance(control.element, WebElement)
