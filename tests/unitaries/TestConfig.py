# -*- coding: utf-8 -*-
"""TODO"""


import os
import ast

from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.loggers.LoggerManager import LoggerManager

LOGGER_MANAGER = LoggerManager()
class TestConfig(TestInfoBase):
    '''
    TestSuite for settings keys and values
    '''

    # Error Messages
    ERR_KEY_NOT_FOUND = "Required key '{}', can't be None"
    ERR_KEY_INVALID_VALUE = "Required key '{}', just can be in '{}'"
    ERR_KEY_PATH_NOT_FOUND = "Required key '{}', not found for path '{}'"
    ERR_KEY_EMPTY = "Required key '{}', can't be empty, value='{}'",
    ERR_KEY_REGEX = "Optional key '{}', not provided or not matching regex: {} ",
    # Test constants
    PATH_SETTINGS = "qacode/configs/settings.json"
    # TODO: Replace this list with a dict and stop using numeric indexes
    msgs = [
        "Settings file doesn't found, copy from settings.example.ini",
        "Some missing section on settings.ini file",
        "BOT mode just can be : local,remote",
        "BOT browser just can be : firefox , chrome , iexplorer, phantomjs",
        "BOT url_hub just can be match with this regular expression : {}",
        "BOT url_node just can be match with this regular expression : {}",
        "BOT profile_path, optional key: file not found or not provided",
        "BOT drivers_path: path not found or not provided",
        "BOT drivers_names: path not found for driver_name={}",
        "BOT log_name can't be empty name",
        "BOT log_output_file can't be empty name",
        ("TESTLINK url, optional key, not provided or not matching regular "
         "expression: {} "),
        "TESTLINK devkey, optional key: file not found",
        ("TEST_UNITARIES url just can be match with this regular expression : "
         "{}"),
        ("TEST_FUNCTIONALS url_login just can be match with this regular "
         "expression : {}"),
        ("TEST_FUNCTIONALS url_logout just can be match with this regular "
         "expression : {}"),
        ("TEST_FUNCTIONALS url_logged_ok just can be match with this regular "
         "expression : {}"),
        ("TEST_FUNCTIONALS url_logged_ko just can be match with this regular "
         "expression : {}"),
        ("TEST_FUNCTIONALS selectors can't be empty array and can't contain "
         "empty selectors"),
        "TEST_FUNCTIONALS creed_user, can't be empty string",
        "TEST_FUNCTIONALS creed_pass, can't be empty string",
        "BUILD skip_travis_tests, can't be None, just bool values",
    ]
    regexs = [
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'  # noqa
    ]

    def __init__(self, method_name="TestConfig"):
        super(TestConfig, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER
        )

    def test_000_config_exist(self):
        """Test : test_000_config_exist"""
        self.assertEqual(True, os.path.exists(self.PATH_SETTINGS),
                         self.ERR_KEY_PATH_NOT_FOUND.format("Log file", self.PATH_SETTINGS))

    def test_001_config_loaded(self):
        """Test : test_001_config_nose_loaded"""
        sections = [
            self.test_config['bot'],
            self.test_config['testlink'],
            self.test_config['tests'],
            self.test_config['tests']['unitaries'],
            self.test_config['tests']['functionals'],
            self.test_config['build'],
        ]
        self.assertNotIn(None, sections, self.msgs[1])

    def test_002_botmode(self):
        """Test : Has key bot.mode with valid value"""
        value = self.test_config['bot']['mode']
        valid_values = ["local", "remote"]
        self.assertIn(value,valid_values,
                      self.ERR_KEY_INVALID_VALUE.format('bot.mode',value))

    def test_003_botbrowser(self):
        """Test : Has key bot.browser with valid value"""
        value = self.test_config['bot']["browser"]
        valid_values = ["firefox", "chrome", "iexplorer", "phantomjs"]
        self.assertIn(value, valid_values,
                      self.ERR_KEY_INVALID_VALUE.format('bot.mode',value))

    def test_004_config_has_key_bot_url_hub(self): # TODO: edit test
        """Test : test_004_config_has_key_bot_url_hub"""
        self.assertRegex(
            self.test_config['bot']["url_hub"], self.regexs[0],
            self.msgs[4].format(self.regexs[0])
        )

    def test_005_config_has_key_bot_url_node(self): # TODO: edit test
        """Test : test_005_config_has_key_bot_url_node"""
        self.assertRegex(
            self.test_config['bot']["url_node"], self.regexs[0],
            self.msgs[5].format(self.regexs[0])
        )

    def test_006_config_has_key_bot_drivers_path(self): # TODO: edit test
        """Test : test_006_config_has_key_bot_drivers_path"""
        value = self.test_config['bot']["drivers_path"]
        exist = os.path.exists(value)
        if not exist:
            self.log.warn(self.msgs[7])

    def test_007_config_has_key_bot_drivers_names(self): # TODO: edit test
        """Test : test_007_config_has_key_bot_drivers_names"""
        values = ast.literal_eval(self.test_config['bot']["drivers_names"])
        file_path = "{}{}{}".format(self.test_config['bot']["drivers_path"], "{}", "{}")
        if os.name == "nt":
            file_path = file_path.format("\\", "{}")
        else:
            file_path = file_path.format("/", "{}")
        for driver_name in values:
            file_path = file_path.format(driver_name)
            exist = os.path.exists(file_path)
            if not exist:
                self.log.warn(self.msgs[8].format(driver_name))

    def test_008_config_has_key_bot_log_name(self): # TODO: edit test
        """Test : test_008_config_has_key_bot_log_name"""
        value = self.test_config['bot']["log_name"]
        self.assertNotEqual(value, "", self.msgs[9])

    def test_009_config_has_key_bot_log_output_file(self): # TODO: edit test
        """Test : test_009_config_has_key_bot_log_output_file"""
        value = self.test_config['bot']["log_output_file"]
        self.assertNotEqual(value, "", self.msgs[10])

    def test_010_config_has_key_testlink_url(self): # TODO: edit test
        """Test : test_010_config_has_key_testlink_url"""
        value = self.test_config.get("TESTLINK")["url"]
        exist_length = len(value)
        if exist_length <= 0:
            self.log.warn(self.msgs[11].format(self.regexs[0]))
        else:
            self.assertRegexpMatches(value, self.regexs[0], self.msgs[11])

    def test_011_config_has_key_testlink_devkey(self): # TODO: edit test
        """Test : test_011_config_has_key_testlink_devkey"""
        value = self.test_config.get("TESTLINK")["devkey"]
        exist_length = len(value)
        if exist_length <= 0:
            self.log.warn(self.msgs[12])

    def test_012_config_has_key_test_unitaries_url(self): # TODO: edit test
        """Test : test_012_config_has_key_test_unitaries_url"""
        self.assertRegexpMatches(
            self.test_config.get("TEST_UNITARIES")["url"],
            self.regexs[0], self.msgs[13]
        )

    def test_013_config_has_key_test_functionals_url_login(self): # TODO: edit test
        """Test : test_013_config_has_key_test_functionals_url_login"""
        self.assertRegexpMatches(
            self.test_config.get("TEST_FUNCTIONALS")["url_login"],
            self.regexs[0], self.msgs[14]
        )

    def test_014_config_has_key_test_functionals_url_logout(self): # TODO: edit test
        """Test : test_014_config_has_key_test_functionals_url_logout"""
        self.assertRegexpMatches(
            self.test_config.get("TEST_FUNCTIONALS")["url_logout"],
            self.regexs[0], self.msgs[15]
        )

    def test_015_config_has_key_test_functionals_url_logged_ok(self): # TODO: edit test
        """Test : test_015_config_has_key_test_functionals_url_logged_ok"""
        self.assertRegexpMatches(
            self.test_config.get("TEST_FUNCTIONALS")["url_logged_ok"],
            self.regexs[0], self.msgs[16]
        )

    def test_016_config_has_key_test_functionals_url_logged_ko(self): # TODO: edit test
        """Test : test_016_config_has_key_test_functionals_url_logged_ko"""
        self.assertRegexpMatches(
            self.test_config.get("TEST_FUNCTIONALS")["url_logged_ko"],
            self.regexs[0], self.msgs[17]
        )

    def test_017_config_has_key_test_functionals_selectors_login(self): # TODO: edit test
        """Test : test_017_config_has_key_test_functionals_selectors_login"""
        values = ast.literal_eval(
            self.test_config.get("TEST_FUNCTIONALS")["selectors_login"]
        )
        self.assertEqual(len(values), 3, self.msgs[18])
        for value in values:
            self.assertNotEqual(value, "", self.msgs[18])

    def test_018_config_has_key_test_functionals_creed_user(self): # TODO: edit test
        """Test : test_018_config_has_key_test_functionals_creed_user"""
        value = self.test_config.get("TEST_FUNCTIONALS")["creed_user"]
        self.assertNotEqual(value, "", self.msgs[19])

    def test_019_config_has_key_test_functionals_creed_pass(self): # TODO: edit test
        """Test : test_019_config_has_key_test_functionals_creed_pass"""
        value = self.test_config.get("TEST_FUNCTIONALS")["creed_pass"]
        self.assertNotEqual(value, "", self.msgs[20])

    def test_020_config_has_key_build_skip_travis_tests(self): # TODO: edit test
        """Test : test_020_config_has_key_build_skip_travis_tests"""
        value = self.test_config.get("BUILD")["skip_travis_tests"]
        self.assertNotEqual(value, None, self.msgs[21])
        self.assertNotEqual(value, "", self.msgs[21])
