# -*- coding: utf-8 -*-
"""Base module for inherit new Test Suites"""


import time


ASSERT_MSG_DEFAULT = "Fails at '{}': actual={}, expected={}"


class TestInfoBase(object):
    """Base class for inherit new Test classes"""

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
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_equals", actual, expected)
        if actual != expected:
            raise AssertionError(actual, expected, msg)

    def assert_not_equals(self, actual, expected, msg=None):
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
