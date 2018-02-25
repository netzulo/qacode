# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Testsuite for package qacode.core.webs.controls"""


from unittest import skipIf
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.utils import settings
from qacode.core.webs.controls.control_base import ControlBase
from selenium.webdriver.remote.webelement import WebElement


SETTINGS = settings()
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
BOT = None


class TestControlBase(TestInfoBot):
    """Test Suite for ControlBase class"""

    @classmethod
    def setUpClass(cls):
        """Set up test suite"""
        global BOT
        if not SKIP_CONTROLS:
            BOT = TestInfoBot.bot_open(SETTINGS, LOGGER_MANAGER)

    @classmethod
    def tearDownClass(cls):
        """Tear down test suite"""
        global BOT
        if not SKIP_CONTROLS:
            TestInfoBot.bot_close(BOT)

    def __init__(self, method_name="suite_TestControlBase"):
        """Test what probes ControlBase class and methods

        Keyword Arguments:
            method_name {str} -- name for test control base
                (default: {"suite_TestControlBase"})
        """
        super(TestControlBase, self).__init__(
            method_name=method_name,
            bot=BOT
        )

    def setUp(self):
        """Set up test case"""
        super(TestControlBase, self).setUp()
        self.p_tests_config = SETTINGS['tests']['functionals']['pages'][2]
        self.url = self.p_tests_config['url']
        self.ele_searcher = self.p_tests_config['controls'][0]['selector']
        self.ele_menu = self.p_tests_config['controls'][1]['selector']
        self.ele_menu_installation = self.p_tests_config.get(
            'controls')[2]['selector']
        self.ele_menu_common_errors = self.p_tests_config.get(
            'controls')[3]['selector']
        self.bot.navigation.get_url(self.url)
        self.assert_equals_url(self.bot.curr_driver.current_url, self.url)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_001_instance_byelement(self):
        """Testcase: test_001_instance_byelement"""
        element = self.bot.navigation.find_element(self.ele_menu)
        control = ControlBase(self.bot, element=element)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_002_instance_byselector(self):
        """Testcase: test_002_instance_byselector"""
        control = ControlBase(self.bot, selector=self.ele_menu)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_003_instance_bydriverload(self):
        """Testcase: test_003_instance_bydriverload"""
        control = ControlBase(
            self.bot, selector=self.ele_menu, wait_for_load=True)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlBase)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_004_raises_nonebot(self):
        """Testcase: test_004_raises_nonebot"""
        self.assertRaises(
            ControlException,
            ControlBase,
            None,
            self.ele_menu)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_005_raises_noneselector(self):
        """Testcase: test_005_raises_noneselector"""
        self.assertRaises(
            ControlException,
            ControlBase,
            self.bot,
            None)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_006_raises_nosearchselector(self):
        """Testcase: test_006_raises_nosearchselector"""
        self.assertRaises(
            ControlException,
            ControlBase,
            self.bot,
            self.ele_menu,
            search=False)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_007_method_findchild(self):
        """Testcase: test_007_method_findchild"""
        control = ControlBase(self.bot, selector=self.ele_menu)
        self.assertIsInstance(
            control.find_child(self.ele_menu_installation), ControlBase)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_008_property_gettext(self):
        """Testcase: test_008_property_gettext"""
        control = ControlBase(self.bot, selector=self.ele_menu_installation)
        self.assertEqual(control.text, 'Installation')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_009_method_gettext(self):
        """Testcase: test_009_method_gettext"""
        control = ControlBase(self.bot, selector=self.ele_menu_installation)
        self.assertEqual(control.get_text(), 'Installation')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_010_property_attr_id(self):
        """Testcase: test_010_property_attr_id"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        self.assertEqual(control.attr_id, 'docsQuery')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_011_property_attr_class(self):
        """Testcase: test_011_property_attr_class"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        self.assertIn('form-control', control.attr_class)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_012_method_getattrvalue(self):
        """Testcase: test_012_method_getattrvalue"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        self.assertEqual(control.get_attr_value('id'), 'docsQuery')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_013_method_get_attrs(self):
        """Testcase: test_013_method_get_attrs"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        attrs = control.get_attrs(['id', 'class'])
        self.assertEqual(attrs[0]['name'], 'id')
        self.assertEqual(attrs[0]['value'], 'docsQuery')
        self.assertEqual(attrs[1]['name'], 'class')
        self.assertIn('form-control', attrs[1]['value'])

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_014_property_tag(self):
        """Testcase: test_014_property_tag"""
        control = ControlBase(self.bot, selector=self.ele_menu)
        self.assertEqual(control.tag, 'div')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_015_method_typetext_withproperty(self):
        """Testcase: test_015_method_typetext_withproperty"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        control.type_text('test')
        self.assertEqual(control.text, 'test')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_016_method_typetext_withmethod(self):
        """Testcase: test_016_method_typetext_withmethod"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        control.type_text('test')
        self.assertEqual(control.get_attr_value('value'), 'test')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_017_method_typetext_cleartrue(self):
        """Testcase: test_017_method_typetext_cleartrue"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        control.type_text('test', clear=True)
        self.assertEqual(control.get_attr_value('value'), 'test')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_018_method_getcssvalue(self):
        """Testcase: test_018_method_getcssvalue"""
        control = ControlBase(self.bot, selector=self.ele_searcher)
        self.assertEqual(
            control.get_css_value('color'), 'rgba(136, 136, 136, 1)')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_019_method_setcssrule(self):
        """Testcase: test_019_method_setcssrule"""
        control = ControlBase(
            self.bot, selector=self.ele_searcher)
        control.type_text('test')
        control.set_css_value('color', 'red')
        self.assertEqual(
            control.get_css_value('color'), 'rgba(255, 0, 0, 1)')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_020_method_gettext_onscreenfalse(self):
        """Testcase: test_020_method_gettext_onscreenfalse"""
        control = ControlBase(
            self.bot, selector=self.ele_menu_common_errors)
        control
        control.set_css_value('display', 'none')
        text = control.get_text(on_screen=False)
        self.assert_greater(
            len(text), 0, msg='Failed at obtain text, open issue on Github')

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_021_method_gettext_raises_onscreenfalse_whenisdisplayed(self):
        """Testcase:
            test_021_method_gettext_raises_onscreenfalse_whenisdisplayed
        """
        control = ControlBase(self.bot, selector=self.ele_menu_common_errors)
        self.assertRaises(ControlException, control.get_text, on_screen=False)
