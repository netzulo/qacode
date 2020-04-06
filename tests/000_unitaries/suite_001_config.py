# -*- coding: utf-8 -*-
"""Test Suite module for configs"""


import pytest
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBase
from qacode.utils import settings


ASSERT = Assert()
SETTINGS = settings(file_path="qacode/configs/")
MSG_OBSOLETE = "Test obsolete, need new tests for key tests.functionals.pages"
SKIP_CONFIG = SETTINGS['tests']['skip']['test_configs']
SKIP_CONFIG_MSG = 'test_configs DISABLED by config file'


class TestConfig(TestInfoBase):
    """Testcases for class TestInfoBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestConfig, self).setup_method(
            test_method,
            config=settings(file_path="qacode/configs/"))

    # Error Messages
    ERR_KEY_NOT_FOUND = "Required key '{}', can't be None"
    ERR_KEY_INVALID_VALUE = "Required key '{}', just can be in '{}'"
    ERR_KEY_PATH_NOT_FOUND = "Required key '{}', not found for path '{}'"
    ERR_KEY_EMPTY = "Required key '{}', can't be empty, value='{}'"
    ERR_KEY_REGEX = "Optional key '{}', not provided or not matching regex: {}"
    # Test constants
    PATH_SETTINGS = "qacode/configs/"
    REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501

    def test_config_exist(self):
        """Test : test_000_config_exist"""
        ASSERT.path_exist(self.PATH_SETTINGS)

    @pytest.mark.parametrize("key_name", [
        "mode", "browser", "url_hub", "drivers_path",
        "drivers_names", "log_output_file", "log_name", "log_level"
    ])
    def test_config_bot_keys(self, key_name):
        """Testcase: test_config_bot_keys"""
        if SKIP_CONFIG:
            pytest.skip(msg=SKIP_CONFIG_MSG)
        key_value = self.config['bot'][key_name]
        if key_name == 'mode':
            valid_values = ["local", "remote"]
            ASSERT.in_list(key_value, valid_values)
        if key_name == 'browser':
            valid_values = [
                "firefox", "chrome",
                "iexplorer", "phantomjs",
                "edge", "iexplorer"]
            ASSERT.in_list(key_value, valid_values)
        if key_name == 'url_hub':
            ASSERT.regex_url(key_value)
        if key_name == 'drivers_path':
            ASSERT.path_exist(key_value)
        if key_name == 'log_name':
            ASSERT.not_equals(key_value, "")
        if key_name == 'log_output_file':
            ASSERT.not_equals(key_value, "")

    @pytest.mark.parametrize("key_name", [
        "skip", "apps"
    ])
    def test_config_tests_keys(self, key_name):
        """Testcase: test_config_tests_keys"""
        if SKIP_CONFIG:
            pytest.skip(msg=SKIP_CONFIG_MSG)
        key_value = self.config['tests'][key_name]
        if key_name == 'skip':
            ASSERT.is_instance(key_value, dict)
            ASSERT.is_instance(key_value.get('test_configs'), bool)
            ASSERT.is_instance(key_value.get('browsers'), dict)
            ASSERT.is_instance(key_value.get('bot_multiple'), bool)
            ASSERT.is_instance(key_value.get('bot_unique'), bool)
            ASSERT.is_instance(key_value.get('web_controls'), dict)
            ASSERT.is_instance(
                key_value.get('web_controls').get('control_base'), bool)
            ASSERT.is_instance(key_value.get('web_pages'), bool)
            ASSERT.is_instance(key_value.get('benchmarks'), bool)
        if key_name == 'apps':
            ASSERT.is_instance(key_value, list)
            for app_config in key_value:
                ASSERT.is_instance(app_config, dict)
                ASSERT.is_instance(app_config.get('name'), str)
                ASSERT.is_instance(app_config.get('pages'), list)
                for page_config in app_config.get('pages'):
                    ASSERT.is_instance(page_config.get('name'), str)
                    ASSERT.is_instance(page_config.get('url'), str)
                    ASSERT.is_instance(page_config.get('locator'), str)
                    ASSERT.is_instance(page_config.get('go_url'), bool)
                    ASSERT.is_instance(page_config.get('wait_url'), int)
                    ASSERT.is_instance(page_config.get('maximize'), bool)
                    ASSERT.is_instance(page_config.get('controls'), list)
                    # TODO: handle control list
                    ctl_configs = page_config.get('controls')
                    for control in ctl_configs:
                        ASSERT.is_instance(control.get('selector'), str)
