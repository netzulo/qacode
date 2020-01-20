# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info import TestInfoBase
from qatestlink.core.testlink_manager import TLManager
from qacode.utils import settings


class TestTestInfoBase(TestInfoBase):
    """Testcases for class TestInfoBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestTestInfoBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    def test_001_inheritance(self):
        """Test: test_001_inheritance"""
        self.assert_is_instance(self, object)
        self.assert_is_instance(self, TestInfoBase)
        self.assert_is_instance(self.log, logging.Logger)
        self.assert_is_instance(self.config, dict)
        if self.config.get('testlink'):
            self.assert_is_instance(self.tlm, TLManager)

    @pytest.mark.parametrize("log_level", [
        "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
    ])
    def test_002_log_levels(self, log_level):
        """Testcase: test_002_log_levels"""
        msg = "Unitary test, checking level type'{}'".format(
            log_level)
        if log_level == 'DEBUG':
            self.log.debug(msg)
        if log_level == 'INFO':
            self.log.info(msg)
        if log_level == 'WARNING':
            self.log.warning(msg)
        if log_level == 'ERROR':
            self.log.error(msg)
        if log_level == 'CRITICAL':
            self.log.critical(msg)

    def test_loggermanager_notlogpath(self):
        """Testcase: test_loggermanager_notlogpath"""
        with pytest.raises(Exception):
            LoggerManager(log_path=None)

    def test_loggermanager_notlogname(self):
        """Testcase: test_loggermanager_notlogname"""
        with pytest.raises(Exception):
            LoggerManager(log_name=None)

    def test_loggermanager_allflagsfalse(self):
        """Testcase: test_loggermanager_allflagsfalse"""
        with pytest.raises(Exception):
            LoggerManager(is_output_console=False, is_output_file=False)
