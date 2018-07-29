# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.testing.test_info import TestInfoBase
from qatestlink.core.testlink_manager import TLManager
from qautils.files import settings


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
        """TODO: doc method"""
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
