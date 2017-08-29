import unittest, logging
from testconfig import config as cfg
from qacode.core.testing.TestInfoBase import TestInfoBase

class TestTestInfoBase(TestInfoBase):

    def __init__(self, method_name="TestTestInfoBase"):
        super(TestTestInfoBase, self).__init__(method_name, logger_manager=None)       

    def test_inheritance(self):
        self.assertIsInstance(self,unittest.TestCase)
        self.log.info("assertIsInstance : unittest.TestCase class inheritance it's working")
        self.assertIsInstance(self,TestInfoBase)
        self.log.info("assertIsInstance : TestInfoBase class inheritance it's working")
