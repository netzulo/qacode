# -*- coding: utf-8 -*-
"""Package qacode.core.testing.testlink"""


import pytest
from qacode.core.loggers.logger_manager import Log
from qacode.core.testing.test_info import TestInfoBase
from qacode.core.testing.testlink.reporter_testlink import ReporterTestlink
from qacode.utils import settings


SETTINGS = settings(file_path="qacode/configs/")


class TestReporterTestlink(TestInfoBase):
    """Test Suite for class ReporterTestlink"""

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestReporterTestlink, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    def test_reportertestlink_ok(self):
        """Test: test_reportertestlink_ok"""
        settings = SETTINGS.get("bot")
        log = Log(
            log_path=settings.get('log_output_file'),
            log_name=settings.get('log_name'),
            log_level=settings.get('log_level'))
        with pytest.raises(NotImplementedError):
            ReporterTestlink(log=log)
