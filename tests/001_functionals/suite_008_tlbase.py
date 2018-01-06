# -*- coding: utf-8 -*-
"""Package testing.testlink"""


from qacode.core.utils import settings
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info_base import TestInfoBase


SETTINGS = settings()
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestTlBase(TestInfoBase):
    """TODO"""

    # properties

    def __init__(self, method_name="TestTlBase"):
        """TODO"""
        super(TestTlBase, self).__init__(
            method_name,
            logger_manager=LOGGER_MANAGER,
            test_config=SETTINGS
        )

    def test_000_instance(self):
        """TODO"""
        # TODO: need to wait for qatestlink module be completed
        pass
