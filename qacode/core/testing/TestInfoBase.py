# -*- coding: utf-8 -*-
"""Base module for inherit new Test Suites"""


import time
import unittest

from qacode.core.loggers.LoggerManager import LoggerManager
from qacode.core.utils.Utils import settings


class TestInfoBase(unittest.TestCase):
    """Base class for inherit new Test classes"""

    logger_manager = None
    log = None
    test_config = None

    def __init__(self, method_name="TestInfoBase", logger_manager=None,
                 test_config=None):
        super(TestInfoBase, self).__init__(method_name)
        if test_config is None:
            self.test_config = settings()
        else:
            self.test_config = test_config
        if logger_manager is None:
            self.logger_manager = LoggerManager()
        else:
            self.logger_manager = logger_manager
        self.log = self.logger_manager.get_log()

    @classmethod
    def setUpClass(cls):
        """
        Just starting testcase instance dependencies
        """
        print("TestInfoBase.setup@classmethod: code mark")

    def setUp(self):
        """
        Just starting testcase instance dependencies
        Dependencies:
          [core] Instance testlink dependencies
        """
        self.log.debug("TestInfoBase.setup: starting testsuite...")
        # TODO: integrate TestlinkBase class and load testlink data at instance

    def tearDown(self):
        """
        Just stoping testcase instance dependencies
        """
        self.log.debug("TestInfoBase.tearDown: finishing testsuite...")

    @classmethod
    def tearDownClass(cls):
        """
        Just stoping testcase class dependencies
        """
        print("TestInfoBase.tearDownClass@classmethod: finishing testsuite...")

    def timer(self, wait=5, print_each=5, log=None):
        """
        Notes:
          logger:
          wait: default value it's 5
          print_each: default value it's 5, must be divisible by 5, negatives
              are accepted
        """
        if log is None:
            raise Exception("Can't execute timer without log")
        if (print_each % 5) != 0:
            raise Exception(
                "Can't print timer if print_each is not divisible by 5"
            )

        while wait > 0:
            log("Sleeping {} seconds, remaining {} seconds"
                .format(print_each, wait))
            self.sleep(print_each)
            wait -= print_each
        log("Timer terminated...")

    def sleep(self, wait=0):
        """
        Just call to native python time.sleep() method
        Notes:
          Wait time on Runtime execution before execute next lane of code
        """
        if wait > 0:
            time.sleep(wait)

    def assert_equals_url(self, actual, expected, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st it's equals to 2nd url
        """
        self.sleep(wait)
        if not actual == expected:
            raise AssertionError(
                actual, expected,
                ('Wrong URL, not equals: actual={}, expected={}'
                 .format(actual, expected)),
                msg
            )

    def assert_not_equals_url(self, actual, expected, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st it isn't equals to 2nd url
        """
        self.sleep(wait)
        if actual == expected:
            raise AssertionError(
                actual, expected,
                ('Wrong URL, is equals: actual={}, expected={}'
                 .format(actual, expected)),
                msg
            )

    def assert_contains_url(self, current, contains, msg='', wait=0):
        """
        Allow to compare 2 urls and check if 1st contains 2nd url
        """
        self.sleep(wait)
        if current not in contains:
            raise AssertionError(
                current, contains,
                ("Wrong URL, current doesn't contains expected: current={}, "
                 "contains={}".format(current, contains)),
                msg
            )

    def assert_is_instance(self, obj, cls, msg=''):
        """
        Allow to encapsulate method
            assertIsInstance(obj, cls, msg='')
        """
        self.assertIsInstance(obj, cls, msg=msg)

    def assert_raises(self, expected_exception, *args, **kwargs):
        """
        Allow to encapsulate method
            assertRaises(expected_exception, args, kwargs)
        """
        self.assertRaises(expected_exception, args, kwargs)

    def assert_greater(self, int_a, int_b, msg=''):
        """
        Allow to encapsulate method
            assertGreater(a, b, msg=msg)
        """
        self.assertGreater(int_a, int_b, msg=msg)