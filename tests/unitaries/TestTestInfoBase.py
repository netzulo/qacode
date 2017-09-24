import unittest, logging
from testconfig import config as cfg
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.loggers.LoggerManager import LoggerManager

logger_manager = LoggerManager(log_path=cfg["BOT"]["log_output_file"],log_level=logging.DEBUG)

class TestTestInfoBase(TestInfoBase):
    """Test Suite for TestInfoBase class"""

    def __init__(self, method_name="TestTestInfoBase"):
        super(TestTestInfoBase, self).__init__(method_name, logger_manager=logger_manager)

    def test_001_inheritance(self):
        """Test: test_001_inheritance"""
        self.assertIsInstance(self,unittest.TestCase)
        self.log.info("assertIsInstance : unittest.TestCase class inheritance it's working")
        self.assertIsInstance(self,TestInfoBase)
        self.log.info("assertIsInstance : TestInfoBase class inheritance it's working")

    def test_002_nosetests_methods(self):
        """Test: test_002_nosetests_methods"""
        self.log.info("dummy test to check setup and teardown methods")
