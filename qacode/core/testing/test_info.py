# -*- coding: utf-8 -*-
"""Base module for inherit new Test Suites"""


import os
import re
import time
import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.utils import settings


ASSERT_MSG_DEFAULT = "Fails at '{}': actual={}, expected={}"
ASSERT_REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501
SETTINGS = settings()
SETTINGS_BOT = SETTINGS.get('bot')
LOGGER_MANAGER = LoggerManager(
    log_path="{}/".format(
        SETTINGS_BOT.get('log_output_file')),
    log_name=SETTINGS_BOT.get('log_name'),
    log_level=SETTINGS_BOT.get('log_level')
)


class TestInfoBase(object):
    """Base class for inherit new Test classes"""

    log = None

    @classmethod
    def bot_open(cls):
        """Open browser using BotBase instance

        Returns:
            BotBase -- wrapper browser handler for selenium
        """
        return BotBase(**SETTINGS)

    @classmethod
    def bot_close(cls, bot):
        """TODO: doc method"""
        return bot.close()

    @classmethod
    def app_config(cls, app_name):
        """TODO: doc method"""
        app_configs = SETTINGS['tests']['apps']
        for app_config in app_configs:
            if app_config.get('name') == app_name:
                return app_config
        raise Exception("App name not found")

    @classmethod
    def app_page(cls, page_name):
        """TODO: doc method"""
        app_configs = SETTINGS['tests']['apps']
        for app_config in app_configs:
            for page_config in app_config.get('pages'):
                if page_config.get('name') == page_name:
                    return page_config
        raise Exception("App name not found")

    def setup_method(self, test_method):
        """Configure self.attribute"""
        self.add_property('log', value=LOGGER_MANAGER.logger)
        self.log.info("Started testcase named='{}'".format(
            test_method.__name__))

    def teardown_method(self, test_method):
        """Unload self.attribute"""
        self.log.info("Finished testcase named='{}'".format(
            test_method.__name__))

    def add_property(self, name, value=None):
        """TODO: doc method"""
        setattr(self, name, value)

    def timer(self, wait=5, print_each=5):
        """Timer to sleep browser on testcases

        Keyword Arguments:
            wait {int} -- seconds to wait (default: {5})
            print_each {int} -- print message each seconds, must be divisible
                by 5, negatives are accepted (default: {5})

        Raises:
            Exception -- [description]
        """
        msg_err = "Timer can't works if print_each param isn't divisible by 1"
        if (print_each % 1) != 0:
            raise Exception(msg_err)
        while wait > 0:
            self.sleep(print_each)
            wait -= print_each

    def sleep(self, wait=0):
        """Just call to native python time.sleep method

        Keyword Arguments:
            wait {int} -- Wait time on Runtime execution before execute
                next lane of code (default: {0})
        """
        if wait > 0:
            time.sleep(wait)

    def assert_equals(self, actual, expected, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_equals", actual, expected)
        if actual != expected:
            raise AssertionError(actual, expected, msg)

    def assert_not_equals(self, actual, expected, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_equals", actual, expected)
        if actual == expected:
            raise AssertionError(actual, expected, msg)

    def assert_equals_url(self, actual, expected, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st it's equals to 2nd url

        Arguments:
            actual {type} -- actual value
            expected {type} -- expected value

        Keyword Arguments:
            wait {int} -- Wait time on Runtime execution before execute
                next lane of code (default: {0})

        Raises:
            AssertionError -- [description]
        """
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_equals_url", actual, expected)
        self.sleep(wait)
        if actual != expected:
            raise AssertionError(actual, expected, msg)

    def assert_not_equals_url(self, actual, expected, msg=None, wait=0):
        """Allow to compare 2 urls to check if 1st isn't equals to 2nd url"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_equals_url", actual, expected)
        self.sleep(wait)
        if actual == expected:
            raise AssertionError(actual, expected, msg)

    def assert_contains_url(self, actual, contains, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st contains 2nd url"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_contains_url", actual, contains)
        self.sleep(wait)
        if actual not in contains:
            raise AssertionError(actual, contains, msg)

    def assert_not_contains_url(self, actual, contains, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st not contains 2nd url"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_contains_url", actual, contains)
        self.sleep(wait)
        if actual in contains:
            raise AssertionError(actual, contains, msg)

    def assert_is_instance(self, instance, class_type, msg=None):
        """Allow to encapsulate method assertIsInstance(obj, cls, msg='')"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_is_instance", instance, class_type)
        if not isinstance(class_type, type):
            class_type = type(class_type)
        if not isinstance(instance, class_type):
            raise AssertionError(instance, class_type, msg)
        return True

    def assert_raises(self, actual_exception, expected_exception, msg=None):
        """Allow to encapsulate method TODO: last time used failed,
            need to confirm bug assertRaises
            ( expected_exception, function_ref, args, kwargs )
        """
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_raises",
                actual_exception,
                expected_exception)
        if not isinstance(actual_exception, expected_exception):
            raise AssertionError(
                actual_exception, expected_exception, msg)

    def assert_greater(self, actual, greater, msg=None):
        """Allow to encapsulate method assertGreater(a, b, msg=msg)"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_greater", actual, greater)
        if actual > greater:
            raise AssertionError(actual, greater, msg)

    def assert_lower(self, actual, lower, msg=None):
        """Allow to encapsulate method assertLower(a, b, msg=msg)"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_greater", actual, lower)
        if actual < lower:
            raise AssertionError(actual, lower, msg)

    def assert_in(self, actual, valid_values, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_in", actual, valid_values)
        if actual not in valid_values:
            raise AssertionError(actual, valid_values, msg)

    def assert_not_in(self, actual, invalid_values, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_in", actual, invalid_values)
        if actual in invalid_values:
            raise AssertionError(actual, invalid_values, msg)

    def assert_regex(self, actual, pattern, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_regex", actual, pattern)
        is_match = re.match(pattern, actual)
        if not is_match:
            raise AssertionError(actual, pattern, msg)

    def assert_not_regex(self, actual, pattern, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_regex", actual, pattern)
        is_match = re.match(pattern, actual)
        if is_match:
            raise AssertionError(actual, pattern, msg)

    def assert_regex_url(self, actual, pattern=None, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_regex_url", actual, pattern)
        if not pattern:
            pattern = ASSERT_REGEX_URL
        self.assert_regex(actual, pattern, msg=msg)

    def assert_path_exist(self, actual, is_dir=True, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_path_exist",
                actual,
                "is_dir={}".format(is_dir))
        if not os.path.exists(actual):
            raise AssertionError(actual, "NEED_PATH_FOUND", msg)
        _is_dir = os.path.isdir(actual)
        if is_dir:
            if not _is_dir:
                raise AssertionError(actual, "NEED_PATH_IS_DIR", msg)
        else:
            if _is_dir:
                raise AssertionError(actual, "NEED_PATH_NOT_DIR", msg)

    def assert_path_not_exist(self, actual, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_path_not_exist", actual, "")
        if os.path.exists(actual):
            raise AssertionError(actual, "NEED_PATH_NOT_FOUND", msg)

    def assert_true(self, actual, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_true", actual, "")
        self.assert_is_instance(actual, bool)
        self.assert_equals(actual, True, msg=msg)

    def assert_false(self, actual, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_false", actual, "")
        self.assert_is_instance(actual, bool)
        self.assert_equals(actual, False, msg=msg)

    def assert_none(self, actual, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_false", actual, "")
        self.assert_equals(actual, None, msg=msg)

    def assert_not_none(self, actual, msg=None):
        """TODO: doc method"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_false", actual, "")
        self.assert_not_equals(actual, None, msg=msg)


class TestInfoBot(TestInfoBase):
    """Inherit class what implements bot on each testcase"""

    bot = None

    def teardown_method(self, test_method, close=True):
        """Unload self.attribute"""
        super(TestInfoBot, self).teardown_method(test_method)
        try:
            if close:
                self.log.debug(
                    "Not closing bot by optional param 'close'")
                self.bot_close(self.bot)
        except Exception as err:
            self.log.error(
                "Fails at try to close bot: {}".format(
                    err))

    def setup_method(self, test_method):
        """Configure self.attribute.
        If skipIf mark applied and True as first param for args tuple
            then not open bot
        """
        super(TestInfoBot, self).setup_method(test_method)
        if 'skipIf' in dir(test_method) and test_method.skipIf.args[0]:
            pytest.skip(test_method.skipIf.args[1])
            return
        if not isinstance(self.bot, BotBase):
            self.add_property('bot', value=self.bot_open())


class TestInfoBotUnique(TestInfoBot):
    """Inherit class what implements bot on each testcase"""

    @classmethod
    def setup_class(cls):
        """If name start with 'test_' and have decorator skipIf
            with value True, then not open bot
        """
        for method_name in dir(cls):
            if method_name.startswith("test_"):
                method = getattr(cls, method_name)
                if 'skipIf' in dir(method) and method.skipIf.args[0]:
                    return
        cls.add_property(cls, 'bot', cls.bot_open())

    @classmethod
    def teardown_class(cls):
        """TODO: doc method"""
        if cls.bot:
            cls.bot_close(cls.bot)

    def teardown_method(self, test_method, close=False):
        """Unload self.attribute"""
        super(TestInfoBotUnique, self).teardown_method(
            test_method, close=close)
