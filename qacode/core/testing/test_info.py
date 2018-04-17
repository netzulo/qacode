# -*- coding: utf-8 -*-
"""Base module for inherit new Test Suites"""


import os
import re
import time
import pytest
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.bots.bot_base import BotBase
from qacode.core.loggers.logger_manager import LoggerManager


ASSERT_MSG_DEFAULT = "Fails at '{}': actual={}, expected={}"
ASSERT_REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501


class TestInfoBase(object):
    """Base class for inherit new Test classes"""

    is_loaded = False
    log = None
    config = None

    @classmethod
    def load(cls, config):
        """Load default config dict"""            
        if config is None and not cls.is_loaded:
            raise CoreException(message="Bad param 'config' provided")
        cls.add_property('config', value=config)
        if cls.log is None:
            config_bot = cls.config.get('bot')
            log_path = "{}/".format(
                config_bot.get('log_output_file'))
            lgm = LoggerManager(
                log_path=log_path,
                log_name=config_bot.get('log_name'),
                log_level=config_bot.get('log_level')
            )
            cls.add_property('log', lgm.logger)
        cls.is_loaded = True

    @classmethod
    def bot_open(cls, config):
        """Open browser using BotBase instance

        Returns:
            BotBase -- wrapper browser handler for selenium
        """
        return BotBase(**config)

    @classmethod
    def bot_close(cls, bot):
        """TODO: doc method"""
        return bot.close()

    @classmethod
    def settings_apps(cls):
        """TODO: doc method"""
        if cls.config is None:
            raise CoreException(message="Call to cls.load() first")
        return cls.config.get('tests').get('apps')

    @classmethod
    def settings_app(cls, app_name):
        """TODO: doc method"""
        for app in cls.settings_apps():
            if app.get('name') == app_name:
                return app
        raise Exception(
            "Not found for: app_name={}".format(
                app_name))

    @classmethod
    def settings_page(cls, page_name, app_name=None):
        """TODO: doc method"""
        page_selected = None
        apps = cls.settings_apps()
        if isinstance(app_name, str):
            apps = [cls.settings_app(app_name)]
        for app in apps:
            for page in app.get('pages'):
                if page.get('name') == page_name:
                    page_selected = page
        return page_selected

    @classmethod
    def settings_control(cls, control_name, page_name=None, app_name=None):
        """TODO: doc method"""
        page_selected = None
        if isinstance(page_name, str):
            page_selected = cls.settings_page(
                page_name, app_name=app_name)
        if page_selected:
            for control in page_selected.get('controls'):
                if control.get('name') == control_name:
                    return control
        else:
            apps = cls.settings_apps()
            for app in apps:
                for page in app.get('pages'):
                    for control in page.get('controls'):
                        if control.get('name') == control_name:
                            return control

    @classmethod
    def settings_filter(cls, key_type, key_name):
        """TODO: doc method"""
        apps = cls.settings_apps()
        if key_type == 'app':
            cls.settings_app(key_name)
        elif key_type == 'page':
            cls.settings_page(key_name)
            raise Exception(
                "Not found for: key_type={}, key_name={}".format(
                    key_type, key_name))
        elif key_type == 'control':
            for app in apps:
                for page in app.get('pages'):
                    for control in app.get('controls'):
                        if control.get('name') == key_name:
                            return control
        else:
            raise Exception("key_type not found")

    def setup_method(self, test_method, **kwargs):
        """Configure self.attribute"""
        self.load(kwargs.get('config'))
        self.log.info("Started testcase named='{}'".format(
            test_method.__name__))

    def teardown_method(self, test_method):
        """Unload self.attribute"""
        self.log.info("Finished testcase named='{}'".format(
            test_method.__name__))

    @classmethod
    def add_property(cls, name, value=None):
        """TODO: doc method"""
        setattr(cls, name, value)

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

    def assert_raises(self, expected_exception, function, *args, **kwargs):
        """Allow to encapsulate pytest.raises method(
            *args=(
                expected_exception,
                function,
            ),
            **kwargs={
                msg: ASSERT_MSG_DEFAULT
            }
        )
        """
        msg = kwargs.get('msg')
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_raises",
                "TODO:not implemented value",
                expected_exception)
        pytest.raises(expected_exception, function, *args, **kwargs)

    def assert_greater(self, actual, greater, msg=None):
        """Allow to encapsulate method assertGreater(a, b, msg=msg)"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_greater", actual, greater)
        if actual < greater:
            raise AssertionError(actual, greater, msg)

    def assert_lower(self, actual, lower, msg=None):
        """Allow to encapsulate method assertLower(a, b, msg=msg)"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_greater", actual, lower)
        if actual > lower:
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
                self.bot_close(self.bot)
            else:
                self.log.debug(
                    "Not closing bot by optional param 'close'")
        except Exception as err:
            self.log.error(
                "Fails at try to close bot: {}".format(
                    err))

    def setup_method(self, test_method, **kwargs):
        """Configure self.attribute.
        If skipIf mark applied and True as first param for args tuple
            then not open bot
        """
        super(TestInfoBot, self).setup_method(test_method, **kwargs)
        if 'skipIf' in dir(test_method) and test_method.skipIf.args[0]:
            pytest.skip(test_method.skipIf.args[1])
            return
        if not isinstance(self.bot, BotBase):
            self.add_property('bot', value=self.bot_open(self.config))


class TestInfoBotUnique(TestInfoBot):
    """Inherit class what implements bot on each testcase"""

    @classmethod
    def setup_class(cls, **kwargs):
        """If name start with 'test_' and have decorator skipIf
            with value True, then not open bot
        """
        tests_methods = []
        skip_methods = []
        skip_force = kwargs.get('skip_force')
        for method_name in dir(cls):
            if method_name.startswith("test_"):
                method = getattr(cls, method_name)
                tests_methods.append(method)
                if 'skipIf' in dir(method) and method.skipIf.args[0]:
                    skip_methods.append(method)
        if tests_methods == skip_methods or skip_force:
            pytest.skip("Testsuite skipped")
        else:
            if not isinstance(cls.bot, BotBase):
                cls.load(kwargs.get('config'))
                cls.add_property(
                    'bot', value=cls.bot_open(cls.config))

    @classmethod
    def teardown_class(cls):
        """TODO: doc method"""
        if cls.bot:
            cls.bot_close(cls.bot)

    def teardown_method(self, test_method, close=False):
        """Unload self.attribute"""
        super(TestInfoBotUnique, self).teardown_method(
            test_method, close=close)
