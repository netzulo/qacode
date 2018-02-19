# -*- coding: utf-8 -*-
# pylint: disable=deprecated-method
# pylint: disable=invalid-name
"""Test Suite module for configs"""


import os
from unittest import skipIf
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_base import TestInfoBase
from qacode.core.utils import path_format


LOGGER_MANAGER = LoggerManager()
MSG_OBSOLETE = "Test obsolete, need new tests for key tests.functionals.pages"


class TestConfig(TestInfoBase):
    """Testcases for class TestInfoBase"""

    # Error Messages
    ERR_KEY_NOT_FOUND = "Required key '{}', can't be None"
    ERR_KEY_INVALID_VALUE = "Required key '{}', just can be in '{}'"
    ERR_KEY_PATH_NOT_FOUND = "Required key '{}', not found for path '{}'"
    ERR_KEY_EMPTY = "Required key '{}', can't be empty, value='{}'"
    ERR_KEY_REGEX = "Optional key '{}', not provided or not matching regex: {}"
    # Test constants
    PATH_SETTINGS = "qacode/configs/settings.json"
    REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501

    def __init__(self, method_name="TestConfig"):
        """Constructor

        Keyword Arguments:
            method_name {str} -- name for config testsuite
                (default: {"TestConfig"})
        """
        super(TestConfig, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER)

    def test_000_config_exist(self):
        """Test : test_000_config_exist"""
        self.assertEqual(True, os.path.exists(self.PATH_SETTINGS),
                         self.ERR_KEY_PATH_NOT_FOUND.format(
                             "Log file", self.PATH_SETTINGS))

    def test_001_bot_mode(self):
        """Test : Has key bot.mode with valid value"""
        value = self.test_config['bot']['mode']
        valid_values = ["local", "remote"]
        self.assertIn(value, valid_values,
                      self.ERR_KEY_INVALID_VALUE.format(
                          'bot.mode', value))

    def test_002_bot_browser(self):
        """Test : Has key bot.browser with valid value"""
        value = self.test_config['bot']["browser"]
        valid_values = ["firefox", "chrome", "iexplorer", "phantomjs"]
        self.assertIn(value, valid_values,
                      self.ERR_KEY_INVALID_VALUE.format('bot.mode', value))

    def test_003_bot_url_hub(self):
        """Test : Has key bot.url_hub and match regex"""
        self.assertRegexpMatches(
            self.test_config['bot']["url_hub"], self.REGEX_URL,
            self.ERR_KEY_REGEX.format('bot.url_hub', self.REGEX_URL)
        )

    @skipIf(
        True,
        """Test obsolete, maybe will use again
        this config key to manage server and nodes connected""")
    def test_004_bot_url_node(self):
        """Test : test_005_config_has_key_bot_url_node"""
        self.assertRegexpMatches(
            self.test_config['bot']["url_node"], self.REGEX_URL,
            self.ERR_KEY_REGEX.format('bot.url_node', self.REGEX_URL)
        )

    def test_005_bot_drivers_path(self):
        """Test : test_006_config_has_key_bot_drivers_path"""
        value = self.test_config['bot']["drivers_path"]
        msg = self.ERR_KEY_PATH_NOT_FOUND.format('bot.drivers_path', value)
        if not os.path.exists(value):
            self.log.warning(msg)

    def test_006_bot_drivers_names(self):
        """Test : test_007_config_has_key_bot_drivers_names"""
        values = self.test_config['bot']["drivers_names"]
        drivers_path = '../qadrivers/'
        path_not_found = self.ERR_KEY_PATH_NOT_FOUND.format(
            'bot.drivers_path', drivers_path)
        for driver_name in values:
            file_not_found = self.ERR_KEY_PATH_NOT_FOUND.format(
                'bot.drivers_path[driver_name]', driver_name)
            if not os.path.exists(drivers_path):
                self.log.warning(path_not_found)
            else:
                file_path = path_format(drivers_path, driver_name)
                if not os.path.exists(file_path):
                    self.log.warning(file_not_found)

    def test_007_bot_log_name(self):
        """Test : test_008_config_has_key_bot_log_name"""
        value = self.test_config['bot']["log_name"]
        self.assertNotEqual(value, "", self.ERR_KEY_EMPTY.format(
            'bot.log_name', value))

    def test_008_bot_log_output_file(self):
        """Test : test_009_config_has_key_bot_log_output_file"""
        value = self.test_config['bot']["log_output_file"]
        self.assertNotEqual(value, "", self.ERR_KEY_EMPTY.format(
            'bot.log_output_file', value))

    def test_009_testlink_url_api(self):
        """
        Test : test_010_config_has_key_testlink_url

        Just an optional key configuration
        """
        value = self.test_config['testlink']["url_api"]
        msg = self.ERR_KEY_REGEX.format('testlink.url_api', self.REGEX_URL)
        if len(value) <= 0:
            self.log.warning(msg)
        else:
            self.assertRegexpMatches(value, self.REGEX_URL, msg)

    def test_010_testlink_devkey(self):
        """
        Test : test_011_config_has_key_testlink_devkey

        Just an optional key configuration
        """
        value = self.test_config['testlink']["dev_key"]
        msg = self.ERR_KEY_EMPTY.format('testlink.testlink', value)
        if len(value) <= 0:
            self.log.warning(msg)
        else:
            self.assertNotEqual(value, "", msg)

    def test_011_key_url(self):
        """Test : test_012_config_has_key_test_unitaries_url"""
        self.assertRegexpMatches(
            self.test_config['tests']['unitaries']['url'],
            self.REGEX_URL,
            self.ERR_KEY_REGEX.format('tests.unitaries.url', self.REGEX_URL)
        )

    @skipIf(True, MSG_OBSOLETE)
    def test_012_key_url_login(self):
        """Test : test_013_config_has_key_test_functionals_url_login"""
        self.assertRegexpMatches(
            self.test_config['tests']['functionals']['url_login'],
            self.REGEX_URL,
            self.ERR_KEY_REGEX.format(
                'tests.functionals.url_login', self.REGEX_URL)
        )

    @skipIf(True, MSG_OBSOLETE)
    def test_013_key_url_logout(self):
        """Test : test_014_config_has_key_test_functionals_url_logout"""
        self.assertRegexpMatches(
            self.test_config['tests']['functionals']['url_logout'],
            self.REGEX_URL,
            self.ERR_KEY_REGEX.format(
                'tests.functionals.url_logout', self.REGEX_URL)
        )

    @skipIf(True, MSG_OBSOLETE)
    def test_014_key_url_logged(self):
        """Test : test_015_config_has_key_test_functionals_url_logged"""
        self.assertRegexpMatches(
            self.test_config['tests']['functionals']['url_logged'],
            self.REGEX_URL,
            self.ERR_KEY_REGEX.format(
                'tests.functionals.url_logged', self.REGEX_URL)
        )

    @skipIf(True, MSG_OBSOLETE)
    def test_015_key_url_404(self):
        """Test : test_016_config_has_key_test_functionals_url_404"""
        self.assertRegexpMatches(
            self.test_config['tests']['functionals']['url_404'],
            self.REGEX_URL,
            self.ERR_KEY_REGEX.format(
                'tests.functionals.url_404', self.REGEX_URL)
        )

    @skipIf(True, MSG_OBSOLETE)
    def test_016_key_selectors_login(self):
        """Test : test_017_config_has_key_test_functionals_selectors_login"""
        values = self.test_config['tests']['functionals']['selectors_login']
        self.assertEqual(len(values), 3, self.ERR_KEY_EMPTY.format(
            'tests.functionals.selectors_login', values))
        for value in values:
            self.assertNotEqual(value, "", self.ERR_KEY_EMPTY.format(
                'tests.functionals.selectors_login', value))

    @skipIf(True, MSG_OBSOLETE)
    def test_017_key_creed_user(self):
        """Test : test_018_config_has_key_test_functionals_creed_user"""
        value = self.test_config['tests']['functionals']['creed_user']
        self.assertNotEqual(value, "", self.ERR_KEY_EMPTY.format(
            'tests.functionals.creed_user', value))

    @skipIf(True, MSG_OBSOLETE)
    def test_018_key_creed_pass(self):
        """Test : test_019_config_has_key_test_functionals_creed_pass"""
        value = self.test_config['tests']['functionals']['creed_pass']
        self.assertNotEqual(value, "", self.ERR_KEY_EMPTY.format(
            'tests.functionals.creed_pass', value))

    def test_019_key_skip_drivers_local(self):
        """Test : test_022_key_skip_drivers_local"""
        value = self.test_config['tests']['skip']['drivers_local']
        msg = self.ERR_KEY_INVALID_VALUE.format(
            'tests.skip.drivers_local', value)
        self.assertIn(value, (True, False), msg)

    def test_020_key_skip_drivers_remote(self):
        """Test : test_023_key_skip_drivers_remote"""
        value = self.test_config['tests']['skip']['drivers_remote']
        msg = self.ERR_KEY_INVALID_VALUE.format(
            'tests.skip.drivers_remote', value)
        self.assertIn(value, (True, False), msg)

    def test_021_key_skip_web_controls(self):
        """Test : test_024_key_skip_web_controls"""
        value = self.test_config['tests']['skip']['web_controls']
        msg = self.ERR_KEY_INVALID_VALUE.format(
            'tests.skip.web_controls', value)
        self.assertIn(value, (True, False), msg)

    def test_022_key_skip_web_pages(self):
        """Test : test_025_key_skip_web_pages"""
        value = self.test_config['tests']['skip']['web_pages']
        msg = self.ERR_KEY_INVALID_VALUE.format(
            'tests.skip.web_pages', value)
        self.assertIn(value, (True, False), msg)
