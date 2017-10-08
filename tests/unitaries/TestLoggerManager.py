# -*- coding: utf-8 -*-
"""Test Suite module for loggers"""


from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.loggers.LoggerManager import LoggerManager


LOGGER_MANAGER = LoggerManager()


class TestLoggerManager(TestInfoBase):
    """Testcases for class LoggerManager"""

    def __init__(self, method_name="TestLoggerManager"):
        super(TestLoggerManager, self).__init__(
            method_name, logger_manager=LOGGER_MANAGER
        )

    def test_001_logger_debug(self):
        """Test: test_001_logger_debug"""
        self.log.debug("Unitary test, checking level type DEBUG")

    def test_002_logger_info(self):
        """Test: test_002_logger_info"""
        self.log.info("Unitary test, checking level type INFO")

    def test_003_logger_warn(self):
        """Test: test_003_logger_warn"""
        self.log.warning("Unitary test, checking level type WARNING")

    def test_004_logger_error(self):
        """Test: test_004_logger_error"""
        self.log.error("Unitary test, checking level type ERROR")

    def test_005_logger_critical(self):
        """Test: test_005_logger_critical"""
        self.log.critical("Unitary test, checking level type CRITICAL")
