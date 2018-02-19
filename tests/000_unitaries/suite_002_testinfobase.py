# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import unittest
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_base import TestInfoBase
from qacode.core.utils import settings


SETTINGS = settings()
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestTestInfoBase(TestInfoBase):
    """Testcases for class TestInfoBase"""

    def __init__(self, method_name="TestTestInfoBase"):
        """Constructor

        Keyword Arguments:
            method_name {str} -- name for test info base testsuite
                (default: {"TestTestInfoBase"})
        """
        super(TestTestInfoBase, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER
        )

    def test_001_inheritance(self):
        """Test: test_001_inheritance"""
        self.assertIsInstance(self, unittest.TestCase)
        self.log.info("assertIsInstance : unittest.TestCase class inheritance "
                      "it's working")
        self.assertIsInstance(self, TestInfoBase)
        self.log.info("assertIsInstance : TestInfoBase class inheritance it's "
                      "working")

    def test_002_nosetests_methods(self):
        """Test: test_002_nosetests_methods"""
        self.log.info("dummy test to check setup and teardown methods")
