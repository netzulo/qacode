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

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlBase, self).setup_method(test_method)
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
    def test_001_instance(self):
        """Testcase: test_001_instance_selector"""
        control_config = self.settings_control(
            'txt_username',
            page_name='page_login')
        control = ControlBase(self.bot, **control_config)
        self.assert_is_instance(control, ControlBase)
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

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_002_raises_nonebot(self):
        """Testcase: test_002_raises_nonebot"""
        self.assert_raises(
            ControlException,
            ControlBase,
            None)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_003_raises_nonesettings(self):
        """Testcase: test_003_raises_nonesettings"""
        self.assert_raises(
            ControlException,
            ControlBase,
            self.bot)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_004_method_findchild(self):
        """Testcase: test_004_method_findchild"""
        login_container_config = self.settings_control('login_container')
        login_container_title_config = self.settings_control(
            'login_container_title')
        control = ControlBase(self.bot, **login_container_config)
        self.assert_is_instance(
            control.find_child(
                login_container_title_config.get('selector')),
            ControlBase)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_005_property_gettext(self):
        """Testcase: test_005_property_gettext"""
        login_container_title_config = self.settings_control(
            'login_container_title').copy()
        login_container_title_config.update({
            "on_instance_load": True
        })
        control = ControlBase(
            self.bot, **login_container_title_config)
        self.assert_equals(control.text, 'Login Page')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_006_property_raises_gettext(self):
        """Testcase: test_006_property_raises_gettext"""
        login_container_title_config = self.settings_control(
            'login_container_title')
        control = ControlBase(
            self.bot, **login_container_title_config)
        self.assert_equals(control.text, None)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_007_method_gettext(self):
        """Testcase: test_007_method_gettext"""
        login_container_title_config = self.settings_control(
            'login_container_title')
        login_container_title_config.update({
            "on_instance_load": True
        })
        control = ControlBase(
            self.bot, **login_container_title_config)
        self.assert_equals(control.get_text(), 'Login Page')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_008_property_attr_id(self):
        """Testcase: test_008_property_attr_id"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        self.assert_equals(control.attr_id, 'username')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_009_property_attr_class(self):
        """Testcase: test_009_property_attr_class"""
        login_container_config = self.settings_control(
            'login_container')
        login_container_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_config)
        self.assert_in('large-12', control.attr_class)
        self.assert_in('columns', control.attr_class)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_010_method_getattrvalue(self):
        """Testcase: test_010_method_getattrvalue"""
        login_container_config = self.settings_control(
            'login_container')
        login_container_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_config)
        self.assert_equals(control.get_attr_value('id'), 'content')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_011_method_get_attrs(self):
        """Testcase: test_011_method_get_attrs"""
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
    def test_012_property_tag(self):
        """Testcase: test_012_property_tag"""
        login_container_config = self.settings_control(
            'login_container')
        login_container_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **login_container_config)
        self.assert_equals(control.tag, 'div')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_013_method_typetext_withproperty(self):
        """Testcase: test_013_method_typetext_withproperty"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        control.type_text('test')
        self.assert_equals(control.text, 'test')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_014_method_typetext_withmethod(self):
        """Testcase: test_014_method_typetext_withmethod"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        control.type_text('test')
        self.assert_equals(control.get_attr_value('value'), 'test')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_015_method_typetext_cleartrue(self):
        """Testcase: test_015_method_typetext_cleartrue"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        control.type_text('test', clear=True)
        self.assert_equals(control.get_attr_value('value'), 'test')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_016_method_getcssvalue(self):
        """Testcase: test_016_method_getcssvalue"""
        txt_username_config = self.settings_control(
            'txt_username')
        txt_username_config.update({
            "on_instance_load": True
        })
        control = ControlBase(self.bot, **txt_username_config)
        self.assert_equals(
            control.get_css_value('color'), 'rgba(0, 0, 0, 0.75)')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_017_method_setcssrule(self):
        """Testcase: test_017_method_setcssrule"""
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
    def test_018_method_gettext_onscreenfalse(self):
        """Testcase: test_018_method_gettext_onscreenfalse"""
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
