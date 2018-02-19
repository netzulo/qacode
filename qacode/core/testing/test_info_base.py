# -*- coding: utf-8 -*-
"""Base module for inherit new Test Suites"""


import time
import unittest

from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.utils import settings


LOGGER_MANAGER = None


class TestInfoBase(unittest.TestCase):
    """Base class for inherit new Test classes"""

    logger_manager = None
    log = None
    test_config = None

    def __init__(self, method_name="TestInfoBase", logger_manager=None,
                 test_config=None):
        """Instance test info base with default config load+loggermanager"""
        super(TestInfoBase, self).__init__(method_name)
        if test_config is None:
            self.test_config = settings()
        else:
            self.test_config = test_config
        if logger_manager is None:
            self.logger_manager = LOGGER_MANAGER
        else:
            self.logger_manager = logger_manager
        self.log = self.logger_manager.logger

    @classmethod
    def setUpClass(cls):
        """Just starting testcase instance dependencies"""
        global LOGGER_MANAGER
        LOGGER_MANAGER = LoggerManager()
        print("TestInfoBase.setup@classmethod: code mark")

    def setUp(self):
        """Just starting testcase instance dependencies by testlink instance"""
        self.log.debug("TestInfoBase.setup: starting testsuite...")
        # TODO: integrate TestlinkBase class and load testlink data at instance

    def tearDown(self):
        """Just stoping testcase instance dependencies"""
        self.log.debug("TestInfoBase.tearDown: finishing testsuite...")

    @classmethod
    def tearDownClass(cls):
        """Just stoping testcase class dependencies"""
        print("TestInfoBase.tearDownClass@classmethod: finishing testsuite...")

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
        msg_each = "Sleeping {} seconds, remaining {} seconds".format(
            print_each, wait)
        if (print_each % 1) != 0:
            raise Exception(msg_err)
        while wait > 0:
            self.log.debug(msg_each)
            self.sleep(print_each)
            wait -= print_each
        self.log.info("Test 'timer' terminated...")

    def sleep(self, wait=0):
        """Just call to native python time.sleep method

        Keyword Arguments:
            wait {int} -- Wait time on Runtime execution before execute
                next lane of code (default: {0})
        """
        if wait > 0:
            time.sleep(wait)
        self.log.info("Test 'sleep' terminated...")

    def assert_equals_url(self, actual, expected, msg='', wait=0):
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
        msg_err = "Wrong URL, not equals: msg={}, actual={}, expected={}"
        self.sleep(wait)
        if not actual == expected:
            raise AssertionError(
                actual, expected, msg_err.format(msg, actual, expected))

    def assert_not_equals_url(self, actual, expected, msg='', wait=0):
        """Allow to compare 2 urls to check if 1st isn't equals to 2nd url"""
        msg_err = "Wrong URL, is equals: msg={} actual={}, expected={}"
        self.sleep(wait)
        if actual == expected:
            raise AssertionError(
                actual, expected, msg_err.format(msg, actual, expected))

    def assert_contains_url(self, current, contains, msg='', wait=0):
        """Allow to compare 2 urls and check if 1st contains 2nd url"""
        msg_err = ("Wrong URL, current doesn't contains"
                   "expected: msg={}, current={}, contains={}")
        self.sleep(wait)
        if current not in contains:
            raise AssertionError(
                current, contains, msg_err.format(msg, current, contains))

    def assert_is_instance(self, obj, cls, msg=''):
        """Allow to encapsulate method assertIsInstance(obj, cls, msg='')"""
        self.assertIsInstance(obj, cls, msg=msg)

    def assert_raises(self, expected_exception, function_ref, *args, **kwargs):
        """Allow to encapsulate method TODO: last time used failed,
            need to confirm bug assertRaises
            ( expected_exception, function_ref, args, kwargs )
        """
        self.assertRaises(expected_exception, function_ref, args, kwargs)

    def assert_greater(self, int_a, int_b, msg=''):
        """Allow to encapsulate method assertGreater(a, b, msg=msg)"""
        self.assertGreater(int_a, int_b, msg=msg)
