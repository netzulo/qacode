import unittest, logging
from testconfig import config as cfg
from qacode.core.testing.TestInfoBase import TestInfoBase

class TestTestInfoBase(TestInfoBase):

    def __init__(self, method_name="TestTestInfoBase"):
        super(TestTestInfoBase, self).__init__(method_name, logger_manager=None)
    
    def setup(self):
        super(TestTestInfoBase, self).setup()

    def tearDown(self):
        super(TestTestInfoBase, self).tearDown()

    def test_instance(self):
        self.log.info("message enter setup and tearDown from super TestInfoBase Class")
