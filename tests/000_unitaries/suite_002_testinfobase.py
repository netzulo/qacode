# -*- coding: utf-8 -*-
"""Test Suite module for testing package"""


import logging
import pytest
from qacode.core.testing.test_info import TestInfoBase


class TestTestInfoBase(TestInfoBase):
    """Testcases for class TestInfoBase"""

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestTestInfoBase, self).setup_method(test_method)

    def test_001_inheritance(self):
        """Test: test_001_inheritance"""
        self.assert_is_instance(self, object)
        self.assert_is_instance(self, TestInfoBase)
        self.assert_is_instance(self.log, logging.Logger)

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
