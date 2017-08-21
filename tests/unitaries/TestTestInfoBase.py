import unittest, logging
from testconfig import config as cfg
from qacode.core.testing.TestInfoBase import TestInfoBase

class TestTestInfoBase(TestInfoBase):

    def __init__(self, method_name="TestTestInfoBase"):
        super(TestTestInfoBase, self).__init__(method_name)
    

    def setup(self):
        super().setup(self)

    def tearDown(self):
        super().tearDown(self)
