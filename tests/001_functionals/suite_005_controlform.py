# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Testsuite for package qacode.core.webs.controls"""


from unittest import skipIf
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.utils import settings
from qacode.core.webs.controls.control_form import ControlForm
from qacode.core.webs.css_properties import CssProperty
from qacode.core.webs.html_attrs import HtmlAttr
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import StrictRule
from qacode.core.webs.strict_rules import StrictSeverity
from qacode.core.webs.strict_rules import StrictType
from selenium.webdriver.remote.webelement import WebElement


SETTINGS = settings()
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
BOT = None


class TestControlForm(TestInfoBot):
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

    def __init__(self, method_name="suite_TestControlForm"):
        """Test what probes ControlForm class and methods

        Keyword Arguments:
            method_name {str} -- name for test control form
                (default: {"suite_TestControlForm"})
        """
        super(TestControlForm, self).__init__(
            method_name=method_name,
            bot=BOT
        )

    def setUp(self):
        """Set up test case"""
        super(TestControlForm, self).setUp()
        self.url = SETTINGS.get(
            'tests')['functionals']['pages'][0]['url']
        self.p_login_controls = SETTINGS.get(
            'tests')['functionals']['pages'][0]['controls']
        self.selector_txt_username = self.p_login_controls[0]['selector']
        self.selector_txt_password = self.p_login_controls[1]['selector']
        self.bot.navigation.get_url(self.url)
        self.assert_equals_url(self.bot.curr_driver.current_url, self.url)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_001_instance_byelement(self):
        """Testcase: test_001_instance_byelement"""
        element = self.bot.navigation.find_element(
            self.selector_txt_username)
        control = ControlForm(self.bot, element=element)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlForm)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_002_instance_byselector(self):
        """Testcase: test_002_instance_byselector"""
        control = ControlForm(
            self.bot, selector=self.selector_txt_username)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlForm)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_003_instance_notstrictrules(self):
        """Testcase: test_003_instance_notstrictrules"""
        control = ControlForm(
            self.bot,
            selector=self.selector_txt_username)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlForm)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_004_instance_strictrules_allstricttypes(self):
        """Testcase: test_004_instance_strictrules_allstricttypes"""
        strict_rules = [
            StrictRule(
                HtmlTag.TAG_INPUT, StrictType.TAG, StrictSeverity.HIGHT),
            StrictRule(
                HtmlAttr.ID, StrictType.HTML_ATTR, StrictSeverity.HIGHT),
            StrictRule(
                HtmlAttr.NAME, StrictType.HTML_ATTR, StrictSeverity.HIGHT),
            StrictRule(
                CssProperty.BORDER_RADIUS, StrictType.CSS_PROP,
                StrictSeverity.MEDIUM)
        ]
        control = ControlForm(
            self.bot,
            selector=self.selector_txt_username,
            strict_rules=strict_rules)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlForm)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_001_raises_falsesearch(self):
        """Testcase: test_002_raises_falsesearch"""
        self.assertRaises(
            ControlException,
            ControlForm,
            self.bot,
            self.selector_txt_username,
            search=False)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_002_raises_strictrule_tag_strictmodeenabled(self):
        """Testcase: test_001_raises_strictrule_tag_strictmodeenabled"""
        self.assertRaises(
            ControlException,
            ControlForm,
            self.bot,
            selector=self.selector_txt_username,
            strict_rules=[
                StrictRule(
                    HtmlTag.TAG_DIV, StrictType.TAG, StrictSeverity.HIGHT)
            ],
            strict_mode=True)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_003_raises_strictrule_htmlattr_strictmodeenabled(self):
        """Testcase: test_003_raises_strictrule_htmlattr_strictmodeenabled"""
        self.assertRaises(
            ControlException,
            ControlForm,
            self.bot,
            selector=self.selector_txt_username,
            strict_rules=[
                StrictRule(
                    HtmlAttr.FOR, StrictType.HTML_ATTR, StrictSeverity.HIGHT)
            ],
            strict_mode=True)

    @skipIf(True, "Can't obtain an element what have not a CSS property")
    def test_004_raises_strictrule_css_strictmodeenabled(self):
        """Testcase: test_004_raises_strictrule_css_strictmodeenabled"""
        self.assertRaises(
            ControlException,
            ControlForm,
            self.bot,
            selector=self.selector_txt_username,
            strict_rules=[
                StrictRule(
                    CssProperty.TABLE_LAYOUT,
                    StrictType.CSS_PROP,
                    StrictSeverity.MEDIUM)
            ],
            strict_mode=True)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_005_raises_nonestrictmode(self):
        """Testcase: test_005_raises_nonestrictmode"""
        self.assertRaises(
            ControlException,
            ControlForm,
            self.bot,
            self.selector_txt_username,
            strict_mode=None)
