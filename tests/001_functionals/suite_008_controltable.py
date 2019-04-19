# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_table import ControlTable
from qautils.files import settings
from selenium.webdriver.remote.webelement import WebElement


SETTINGS = settings(file_path="qacode/configs/")
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']['control_table']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'


class TestControlTable(TestInfoBotUnique):
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
    # elements from config: page_data
    dd_base = None
    dd_menu_data = None
    dd_menu_data_lists = None
    tbl_ok = None

    @classmethod
    def setup_class(cls, **kwargs):
        """TODO: doc method"""
        super(TestControlTable, cls).setup_class(
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
        cls.add_property('dd_menu_data', cls.cfg_control('dd_menu_data'))
        cls.add_property(
            'dd_menu_data_lists', cls.cfg_control('dd_menu_data_lists'))
        cls.add_property('tbl_ok', cls.cfg_control('tbl_ok'))
        cls.add_property('tbl_html5_ok', cls.cfg_control('tbl_html5_ok'))

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestControlTable, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))
        self.setup_login_to_data()

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
    @pytest.mark.parametrize("strict_rules", [
        [{"tag": "table", "type": "tag", "severity": "hight"}]])
    @pytest.mark.parametrize("ctl_name", ['tbl_ok', 'tbl_html5_ok'])
    def test_controltable_instance(self, on_instance_search,
                                   strict_rules, auto_reload, ctl_name):
        """Testcase: test_controltable_instance"""
        cfg = getattr(self, ctl_name).copy()
        cfg.update({
            "instance": "ControlTable",
            "on_instance_search": on_instance_search,
            "auto_reload": auto_reload,
            "strict_rules": strict_rules
        })
        # functional testcases
        ctl = ControlTable(self.bot, **cfg)
        self.assert_is_instance(ctl, ControlTable)
        self.assert_equals(ctl.selector, cfg.get('selector'))
        self.assert_equals(ctl.instance, cfg.get('instance'))
        self.assert_equals(ctl.name, cfg.get('name'))
        self.assert_equals(ctl.locator, 'css selector')
        self.assert_equals(
            ctl.on_instance_search, cfg.get('on_instance_search'))
        self.assert_equals(ctl.auto_reload, cfg.get('auto_reload'))
        if bool(strict_rules):
            self.assert_equals(
                len(ctl.strict_rules), len(cfg.get('strict_rules')))
        if on_instance_search:
            self.assert_is_instance(ctl.element, WebElement)
        if auto_reload is not None:
            self.assert_none(ctl.table)
            ctl.reload(**ctl.settings)
            self.assert_is_instance(ctl.table, ControlBase)
        self.assert_is_instance(ctl.rows, list)
        # Use case 1. not html5:: TABLE > (TR > TH)+(TR > TD)
        if ctl_name == 'tbl_ok':
            self.assert_lower(len(ctl.rows), 3)
            for row in ctl.rows:
                self.assert_is_instance(row, list)
                self.assert_lower(len(row), 2)
                for cell in row:
                    self.assert_is_instance(cell, ControlBase)
        # Use case 2. html5:: TABLE > (THEAD > (TR > TH))+(TBODY > (TR > TH))
        if ctl_name == 'tbl_html5_ok':
            self.assert_lower(len(ctl.rows), 4)
            for row in ctl.rows:
                self.assert_is_instance(row, list)
                self.assert_lower(len(row), 3)
                for cell in row:
                    self.assert_is_instance(cell, ControlBase)

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    @pytest.mark.parametrize("strict_rules", [None])
    @pytest.mark.parametrize("ctl_name", ['tbl_ok', 'tbl_html5_ok'])
    def test_controltable_instance_raises(self, strict_rules, ctl_name):
        """Testcase: test_controltable_instance_raises"""
        cfg = getattr(self, ctl_name).copy()
        cfg.update({
            "instance": "ControlTable",
            "strict_rules": strict_rules,
            "selector": "span"
        })
        # functional testcases
        ctl = ControlTable(self.bot, **cfg)
        self.assert_is_instance(ctl, ControlTable)
        self.assert_equals(ctl.selector, cfg.get('selector'))
        self.assert_equals(ctl.instance, cfg.get('instance'))
        self.assert_equals(ctl.name, cfg.get('name'))
        self.assert_equals(ctl.locator, 'css selector')

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_controltable_internals_ok(self):
        """Testcase: test_controltable_internals_ok"""
        ctl = ControlTable(self.bot, **self.tbl_ok)
        ctl.__load_table__()
        ctl.__check_reload__form__()

    @pytest.mark.skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_controltable_properties_ok(self):
        """Testcase: test_controltable_properties_ok"""
        ctl = ControlTable(self.bot, **self.tbl_ok)
        rows_before = len(ctl.rows)
        ctl.table = ctl.element
        rows_after = len(ctl.rows)
        self.assert_is_instance(ctl.table, ControlBase)
        self.assert_equals(rows_before, rows_after)
