# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_group import ControlGroup
from qautils.files import settings
from selenium.webdriver.remote.webelement import WebElement


SETTINGS = settings(file_path="qacode/configs/")
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'


class TestControlGroup(TestInfoBotUnique):
    """Test Suite for ControlBase class"""

    app = None
    page_login_config = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestControlGroup, cls).setup_class(
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP_CONTROLS)

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlGroup, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))
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
    @pytest.mark.parametrize("selector", [
        "#username", "replace_for_multiple_selector"])
    @pytest.mark.parametrize("instance", ["ControlGroup"])
    @pytest.mark.parametrize("on_instance_search", [False, True])
    @pytest.mark.parametrize("on_instance_load", [False, True])
    @pytest.mark.parametrize("auto_reload", [True])
    @pytest.mark.parametrize("on_instance_group", [False, True])
    def test_instance_base(self, selector, instance, on_instance_search,
                           on_instance_load, auto_reload, on_instance_group):
        """Testcase: test_instance_base"""
        # must be supported at: test_instance_raises_base
        if not on_instance_search and on_instance_load:
            pytest.skip(
                "Test must be supported at: test_instance_raises_group")
        # must be supported
        control_config = {
            "name": "txt_username_base",
            "locator": "css selector",
            "selector": selector,
            "instance": instance,
            "on_instance_search": on_instance_search,
            "on_instance_load": on_instance_load,
            "auto_reload": auto_reload,
            "on_instance_group": on_instance_group,
        }
        control = ControlGroup(self.bot, **control_config)
        self.assert_is_instance(control, ControlGroup)
        if on_instance_search:
            for ele in control.group:
                self.assert_is_instance(ele, WebElement)
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
        self.assert_equals(
            control.on_instance_group,
            control_config.get('on_instance_group'))
        if control_config.get('on_instance_group'):
            self.assert_greater(len(control.group), 1)
        else:
            self.assert_equals(len(control.group), 0)
