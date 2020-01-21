# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_form import ControlForm
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import (
    StrictRule, StrictSeverity, StrictType)
from qacode.utils import settings
from selenium.webdriver.remote.webelement import WebElement


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
        """Setup class (suite) to be executed"""
        super(TestControlForm, cls).setup_class(
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
        super(TestControlForm, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("on_instance_search", [True, False])
    @pytest.mark.parametrize("auto_reload", [True, False])
    @pytest.mark.parametrize("rules", [
        [{"tag": "select", "type": "tag", "severity": "hight"}],
        []
    ])
    def test_controlform_instance(self, on_instance_search,
                                  rules, auto_reload):
        """Testcase: test_001_instance_selector"""
        cfg = self.dd_base
        cfg.update({
            "instance": "ControlForm",
            "on_instance_search": on_instance_search,
            "auto_reload": auto_reload,
            "rules": rules
        })
        # functional testcases
        ctl = ControlForm(self.bot, **cfg)
        self.assert_is_instance(ctl, ControlForm)
        self.assert_equals(ctl.selector, cfg.get('selector'))
        self.assert_equals(ctl.name, cfg.get('name'))
        self.assert_equals(ctl.locator, 'css selector')
        self.assert_equals(
            ctl.on_instance_search, cfg.get('on_instance_search'))
        self.assert_equals(ctl.auto_reload, cfg.get('auto_reload'))
        self.assert_equals(
            len(ctl.rules), len(cfg.get('rules')))
        if on_instance_search:
            self.assert_is_instance(ctl.element, WebElement)
        if not bool(rules):
            self.assert_lower(len(ctl.rules), 0)
            # this lane just for testing purpose, avoid indent 1 lane more
            rules = ctl.rules
        # don't care number of rules at checking
        for i, rule in enumerate(rules):
            self.assert_is_instance(rule["tag"], str)
            self.assert_is_instance(rule["type"], str)
            self.assert_is_instance(rule["severity"], str)
            # params ok at this point
            ctl_rule = ctl.rules[i]
            if isinstance(ctl_rule, dict):
                self.assert_is_instance(ctl_rule["tag"], str)
                self.assert_is_instance(ctl_rule["type"], str)
                self.assert_is_instance(ctl_rule["severity"], str)
                self.assert_equals(rule["tag"], ctl_rule["tag"])
                self.assert_equals(rule["type"], ctl_rule["type"])
                self.assert_equals(rule["severity"], ctl_rule["severity"])
            elif isinstance(ctl_rule, StrictRule):
                self.assert_is_instance(ctl_rule.name, str)
                self.assert_is_instance(ctl_rule.strict_type, StrictType)
                self.assert_is_instance(ctl_rule.enum_type, HtmlTag)
                self.assert_is_instance(ctl_rule.severity, StrictSeverity)
                if ctl.tag == 'select':
                    self.assert_equals(
                        ctl_rule.enum_type.value, HtmlTag.TAG_SELECT.value)
            else:
                pytest.fail("Unkown type for this rule")

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("auto_reload", [True, False])
    @pytest.mark.parametrize("rules", [
        [{"tag": "select", "type": "tag", "severity": "hight"}],
        []
    ])
    def test_method_reload_form(self, auto_reload, rules):
        """Testcase: test_method_setcssrule"""
        # must be supported
        cfg = self.dd_base
        cfg.update({
            "auto_reload": auto_reload,
            "on_instance_search": False,
            "rules": rules
        })
        ctl = ControlForm(self.bot, **cfg)
        self.assert_equals(ctl.on_instance_search, False)
        self.assert_none(ctl.element)
        # Real test behaviour
        cfg.update({"on_instance_search": True})
        ctl.reload(**cfg)
        self.assert_equals(ctl.on_instance_search, True)
        self.assert_is_instance(ctl.element, WebElement)
