# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.utils import settings
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_form import ControlForm
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


SETTINGS = settings()
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'


class TestControlForm(TestInfoBotUnique):
    """Test Suite for ControlBase class"""

    app = None
    page_dropdown_config = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestControlForm, cls).setup_class(
            config=settings(),
            skip_force=SKIP_CONTROLS)

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlForm, self).setup_method(
            test_method, config=settings())
        self.add_property(
            'app', value=self.settings_app('pages_tests'))
        self.add_property(
            'page_dropdown_config', value=self.settings_page('page_dropdown'))
        self.add_property(
            'url', value=self.page_dropdown_config.get('url'))
        self.bot.navigation.get_url(self.url)
        curr_url = self.bot.curr_driver.current_url
        self.assert_equals_url(curr_url, self.url)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("selector", ["#dropdown"])
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
    @pytest.mark.parametrize("selector", ["#dropdown"])
    @pytest.mark.parametrize("instance", ["ControlForm"])
    def test_method_reload_form(self, selector, instance):
        """Testcase: test_method_setcssrule"""
        # must be supported
        control_config = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
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
