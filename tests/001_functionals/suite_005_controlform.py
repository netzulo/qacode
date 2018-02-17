# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Testsuite for package qacode.core.webs.controls"""


from unittest import skipIf
from selenium.webdriver.remote.webelement import WebElement
from qacode.core.utils import settings
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_bot import TestInfoBot
from qacode.core.webs.controls.control_form import ControlForm
from qacode.core.exceptions.control_exception import ControlException


SETTINGS = settings()
SKIP_CONTROLS = SETTINGS['tests']['skip']['web_controls']
SKIP_CONTROLS_MSG = 'web_controls DISABLED by config file'
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
BOT = None


class TestControlForm(TestInfoBot):
    """Test Suite for ControlBase class"""

    @classmethod
    def setUpClass(cls):
        global BOT
        if not SKIP_CONTROLS:
            BOT = TestInfoBot.bot_open(SETTINGS, LOGGER_MANAGER)

    @classmethod
    def tearDownClass(cls):
        global BOT
        if not SKIP_CONTROLS:
            TestInfoBot.bot_close(BOT)

    def __init__(self, method_name="TestControlForm"):
        super(TestControlForm, self).__init__(
            method_name=method_name,
            bot=BOT
        )

    def setUp(self):
        super(TestControlForm, self).setUp()
        self.url = SETTINGS.get(
            'tests')['functionals']['url_login']
        self.selector_txt_username = SETTINGS.get(
            'tests')['functionals']['selectors_login'][0]
        self.selector_txt_password = SETTINGS.get(
            'tests')['functionals']['selectors_login'][1]
        self.bot.navigation.get_url(self.url)
        self.assert_equals_url(
            self.bot.curr_driver.current_url, self.url)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_000_instance_byelement(self):
        """Testcase: test_000_instance_byelement"""
        element = self.bot.navigation.find_element(
            self.selector_txt_username)
        control = ControlForm(self.bot, element=element)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlForm)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_001_instance_byselector(self):
        """Testcase: test_001_instance_byselector"""
        control = ControlForm(
            self.bot, selector=self.selector_txt_username)
        self.assertIsInstance(control.element, WebElement)
        self.assertIsInstance(control, ControlForm)

    @skipIf(SKIP_CONTROLS, SKIP_CONTROLS_MSG)
    def test_002_raises_nosearchselector(self):
        """Testcase: test_002_raises_nosearch"""
        self.assertRaises(
            ControlException,
            ControlForm,
            self.bot,
            self.selector_txt_username,
            search=False)
