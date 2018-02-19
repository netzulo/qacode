# -*- coding: utf-8 -*-
"""Package testing.testlink"""


from unittest import skipIf
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_base import TestInfoBase
from qacode.core.utils import settings


SETTINGS = settings()
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestTlBase(TestInfoBase):
    """Test Suite for class TlBase"""

    def __init__(self, method_name="suite_TestTlBase"):
        """Test what probes TlBase class and methods

        Keyword Arguments:
            method_name {str} -- name for test testlink base
                (default: {"suite_TestTlBase"})
        """
        super(TestTlBase, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )

    @skipIf(True, "Functionality it's not working yet")
    def test_000_instance(self):
        """Test: test_000_instance"""
        raise NotImplementedError("Functionality it's not working yet")
