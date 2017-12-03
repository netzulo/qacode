# -*- coding: utf-8 -*-
"""Testsuite for package qacode.core.webs.controls"""

from selenium.webdriver.remote.webelement import WebElement
from qacode.core.testing.TestInfoBot import TestInfoBot
from qacode.core.webs.controls.ControlBase import ControlBase
from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.exceptions.ControlException import ControlException

LOGGER_MANAGER = LoggerManager()


class TestControlBase(TestInfoBot):
    """Test Suite for ControlBase class"""

    def __init__(self, method_name="TestControlBase"):
        super(TestControlBase, self).__init__(
            method_name=method_name,
            logger_manager=LOGGER_MANAGER
        )

    def setUp(self):
        super(TestControlBase, self).setUp()
        self.url = self.test_config.get(
            'tests')['functionals']['url_selector_parent']
        self.selector_parent = self.test_config.get(
            'tests')['functionals']['selector_parent']
        self.selector_child = self.test_config.get(
            'tests')['functionals']['selector_child']
        self.url = self.test_config.get(
            'tests')['functionals']['url_login']
        self.selector_btn_login = self.test_config.get(
            'tests')['functionals']['selectors_login'][2]
        self.selector_txt_username = self.test_config.get(
            'tests')['functionals']['selectors_login'][0]
        self.bot.navigation.get_url(self.url)
        self.assert_equals_url(self.bot.curr_driver.current_url, self.url)

    def test_000_instance_byelement(self):
        """Testcase: test_000_instance_byelement"""
        element = self.bot.navigation.find_element(self.selector_parent)
        control = ControlBase(self.bot, element=element)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    def test_001_instance_byselector(self):
        """Testcase: test_001_instance_byselector"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    def test_002_raises_nosearch(self):
        """Testcase: test_002_raises_nosearch"""
        self.assertRaises(
            ControlException, ControlBase, self.bot, self.selector_parent, search=False)

    def test_003_method_findchild(self):
        """Testcase: test_003_method_findchild"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertIsInstance(control.find_child(self.selector_child), ControlBase)

    def test_004_property_gettext(self):
        """Testcase: test_004_property_gettext"""
        control = ControlBase(self.bot, selector=self.selector_btn_login)
        self.assertEqual(control.text, 'Log in')

    def test_005_method_gettext(self):
        """Testcase: test_005_method_gettext"""
        control = ControlBase(self.bot, selector=self.selector_btn_login)
        self.assertEqual(control.get_text(), 'Log in')

    def test_006_property_attr_id(self):
        """Testcase: test_006_propertyhtml_id"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertEqual(control.attr_id, 'nonav')

    def test_007_property_attr_class(self):
        """Testcase: test_007_propertyhtml_class"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertEqual(control.attr_class, 'page-simple')

    def test_008_method_getattrname(self):
        """Testcase: test_008_method_getattrname"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertEqual(control.get_attr_name('id'), 'id')

    def test_009_method_getattrvalue(self):
        """Testcase: test_009_method_getattrvalue"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        self.assertEqual(control.get_attr_value('id'), 'nonav')

    def test_010_method_get_attrs(self):
        """Testcase: test_010_method_get_attrs"""
        control = ControlBase(self.bot, selector=self.selector_parent)
        attrs = control.get_attrs(['id', 'class'])
        self.assertEqual(attrs[0]['name'], 'id')
        self.assertEqual(attrs[0]['value'], 'nonav')
        self.assertEqual(attrs[1]['name'], 'class')
        self.assertEqual(attrs[1]['value'], 'page-simple')

    def test_011_property_tag(self):
        """Testcase: test_011_property_tag"""
        control = ControlBase(self.bot, selector=self.selector_txt_username)
        self.assertEqual(control.tag, 'input')

    def test_012_method_typetext_withproperty(self):  # TODO : tag tests
        """Testcase: test_012_method_typetext_withproperty"""
        control = ControlBase(
            self.bot, selector=self.selector_txt_username)
        control.type_text('test')
        self.assertEqual(control.text, 'test')

    def test_013_method_typetext_withmethod(self): # TODO : tag tests
        """Testcase: test_013_method_typetext_withmethod"""
        control = ControlBase(
            self.bot, selector=self.selector_txt_username)
        control.type_text('test')
        self.assertEqual(control.get_attr_value('value'), 'test')