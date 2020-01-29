# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.loggers.logger_manager import Log
from qacode.core.testing.test_info import TestInfoBase
from qacode.utils import settings
from qatestlink.core.testlink_manager import TLManager


class TestTestInfoBase(TestInfoBase):
    """Testcases for class TestInfoBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestTestInfoBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    def test_log_inheritance(self):
        """Test: test_001_inheritance"""
        self.assert_is_instance(self, object)
        self.assert_is_instance(self, TestInfoBase)
        self.assert_is_instance(self.log._logger, logging.Logger)
        self.assert_is_instance(self.config, dict)
        if self.config.get('testlink'):
            self.assert_is_instance(self.tlm, TLManager)

    @pytest.mark.parametrize("log_level", [
        "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
    ])
    def test_log_levels(self, log_level):
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

    def test_log_notparams(self):
        """Testcase: test_log_notlogname"""
        log = Log(**{})
        self.assert_equals(log._name, "qacode")
        self.assert_equals(log._name_file, "qacode.log")
        self.assert_equals(log._path, "./logs/")
