# -*- coding: utf-8 -*-
"""Base module for asserts on Test Suites"""


import os
import re


ASSERT_MSG_DEFAULT = "Fails at '{}': actual={}, expected={}"
ASSERT_REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501


class Assert(object):
    """Base class for inherit new Test classes"""

    @classmethod
    def message(cls, assert_name, actual, expected, msg=None):
        """Generate assert message for method that calls for it

        Arguments:
            assert_name {str} -- Assert method name that call
            actual {any} -- Actual value to compare
            expected {any} -- Expected value to compare

        Keyword Arguments:
            msg {[type]} -- [description] (default: {None})

        Returns:
            str -- Message to be use on Assert method
        """
        if msg is not None:
            return msg
        return ASSERT_MSG_DEFAULT.format(
            assert_name,
            actual,
            expected)

    def equals(self, actual, expected, msg=None):
        """Allow to compare 2 values and check if 1st it's equals to
            2nd value
        """
        _msg = self.message("assert_equals", actual, expected, msg=msg)
        if actual != expected:
            raise AssertionError(actual, expected, _msg)
        return True

    def not_equals(self, actual, expected, msg=None):
        """Allow to compare 2 value to check if 1st isn't equals to
            2nd value
        """
        _msg = self.message(
            "assert_not_equals", actual, expected, msg=msg)
        if actual == expected:
            raise AssertionError(actual, expected, _msg)
        return True

    def equals_url(self, actual, expected, msg=None, wait=0):
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
        _msg = self.message(
            "assert_equals_url", actual, expected, msg=msg)
        self.sleep(wait)
        if actual != expected:
            raise AssertionError(actual, expected, _msg)
        return True

    def not_equals_url(self, actual, expected, msg=None, wait=0):
        """Allow to compare 2 urls to check if 1st isn't equals to 2nd url"""
        _msg = self.message(
            "assert_not_equals_url", actual, expected, msg=msg)
        self.sleep(wait)
        if actual == expected:
            raise AssertionError(actual, expected, _msg)
        return True

    def contains_url(self, actual, contains, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st contains 2nd url"""
        _msg = self.message(
            "assert_contains_url", actual, contains, msg=msg)
        self.sleep(wait)
        if actual not in contains:
            raise AssertionError(actual, contains, _msg)
        return True

    def not_contains_url(self, actual, contains, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st not contains 2nd url"""
        _msg = self.message(
            "assert_not_contains_url", actual, contains, msg=msg)
        self.sleep(wait)
        if actual in contains:
            raise AssertionError(actual, contains, _msg)
        return True

    def is_instance(self, instance, class_type, msg=None):
        """Allow to encapsulate method assertIsInstance(obj, cls, msg='')"""
        _msg = self.message(
            "assert_is_instance", instance, class_type, msg=msg)
        if not isinstance(class_type, type):
            class_type = type(class_type)
        if not isinstance(instance, class_type):
            raise AssertionError(instance, class_type, _msg)
        return True

    def greater(self, actual, greater, msg=None):
        """Allow to encapsulate method assertGreater(a, b, msg=msg)"""
        _msg = self.message(
            "assert_greater", actual, greater, msg=msg)
        if actual < greater:
            raise AssertionError(actual, greater, _msg)
        return True

    def lower(self, actual, lower, msg=None):
        """Allow to encapsulate method assertLower(a, b, msg=msg)"""
        _msg = self.message(
            "assert_lower", actual, lower, msg=msg)
        if actual > lower:
            raise AssertionError(actual, lower, _msg)
        return True

    def in_list(self, actual, valid_values, msg=None):
        """Allow to compare if value it's in to 2nd list of values"""
        _msg = self.message(
            "assert_in_list", actual, valid_values, msg=msg)
        if actual not in valid_values:
            raise AssertionError(actual, valid_values, _msg)
        return True

    def not_in_list(self, actual, invalid_values, msg=None):
        """Allow to compare if value it's not in to 2nd list of values"""
        _msg = self.message(
            "assert_not_in_list", actual, invalid_values, msg=msg)
        if actual in invalid_values:
            raise AssertionError(actual, invalid_values, _msg)
        return True

    def regex(self, actual, pattern, msg=None):
        """Allow to compare if value match pattern"""
        _msg = self.message(
            "assert_regex", actual, pattern, msg=msg)
        is_match = re.match(pattern, actual)
        if not is_match:
            raise AssertionError(actual, pattern, _msg)
        return True

    def not_regex(self, actual, pattern, msg=None):
        """Allow to compare if value not match pattern"""
        _msg = self.message(
            "assert_not_regex", actual, pattern, msg=msg)
        is_match = re.match(pattern, actual)
        if is_match:
            raise AssertionError(actual, pattern, _msg)
        return True

    def regex_url(self, actual, pattern=None, msg=None):
        """Allow to compare if value match url pattern, can use
            custom pattern
        """
        if not pattern:
            pattern = ASSERT_REGEX_URL
        return self.assert_regex(actual, pattern, msg=msg)

    def path_exist(self, actual, is_dir=True, msg=None):
        """Allow to check if path exist, can check if is_dir also"""
        _msg = self.message(
            "assert_path_exist",
            actual,
            "is_dir={}".format(is_dir),
            msg=msg)
        if not os.path.exists(actual):
            raise AssertionError(actual, "PATH_NOT_EXIST", _msg)
        _is_dir = os.path.isdir(actual)
        if is_dir:
            if not _is_dir:
                raise AssertionError(actual, "PATH_NOT_DIR", _msg)
        else:
            if _is_dir:
                raise AssertionError(actual, "PATH_IS_DIR_AND_MUST_NOT", _msg)
        return True

    def path_not_exist(self, actual, msg=None):
        """Allow to check if path not exist, can check if is_dir also"""
        _msg = self.message(
            "assert_path_not_exist", actual, "", msg=msg)
        if os.path.exists(actual):
            raise AssertionError(actual, "PATH_EXIST_AND_MUST_NOT", _msg)
        return True

    def true(self, actual, msg=None):
        """Allow to compare and check if value it's equals to 'True'"""
        self.assert_is_instance(actual, bool)
        self.assert_equals(actual, True, msg=msg)
        return True

    def false(self, actual, msg=None):
        """Allow to compare and check if value it's equals to 'False'"""
        self.assert_is_instance(actual, bool)
        self.assert_equals(actual, False, msg=msg)
        return True

    def none(self, actual, msg=None):
        """Allow to compare and check if value it's equals to 'None'"""
        return self.assert_equals(actual, None, msg=msg)

    def not_none(self, actual, msg=None):
        """Allow to compare and check if value it's not equals to 'None'"""
        return self.assert_not_equals(actual, None, msg=msg)