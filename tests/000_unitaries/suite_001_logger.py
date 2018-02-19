# -*- coding: utf-8 -*-
"""Test Suite module for loggers"""


from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_base import TestInfoBase
from qacode.core.utils import settings


SETTINGS = settings()
LOGGER_MANAGER = LoggerManager()


class TestLoggerManager(TestInfoBase):
    """Testcases for class LoggerManager"""

    def __init__(self, method_name="TestLoggerManager"):
        """Constructor

        Keyword Arguments:
            method_name {str} -- name for logger testsuite
                (default: {"TestLoggerManager"})
        """
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

    def test_006_logger_loglevelbyconfig(self):
        """Test: test_006_logger_loglevelbyconfig"""
        self.logger_manager_test = LoggerManager(
            log_level=SETTINGS['bot']['log_level'])
        self.log = self.logger_manager_test.logger
        self.log.warning("Unitary test, checking level type by JSON key")

    def test_007_raises_nonelogpath(self):
        """Test: test_007_raises_nonelogpath"""
        self.assertRaises(
            Exception,
            LoggerManager,
            log_path=None)

    def test_008_raises_nonelogname(self):
        """Test: test_008_raises_nonelogname"""
        self.assertRaises(
            Exception,
            LoggerManager,
            log_name=None)

    def test_009_raises_noneoutputs(self):
        """Test: test_008_raises_nonelogname"""
        self.assertRaises(
            Exception,
            LoggerManager,
            is_output_console=None,
            is_output_file=None)
