import unittest, logging
from testconfig import config as cfg
from qacode.core.testing. TesInfoBot import TestInfoBot
from qacode.core.bots.BotBase import BotBase

class TestTestInfoBot(TestInfoBot):

    def __init__(self, method_name="TestTestInfoBot"):
        super(TestTestInfoBot, self).__init__(method_name, logger_manager=None)

    def test_001_inheritance(self):
        self.assertIsInstance(self,unittest.TestCase)
        self.log.info("assertIsInstance : unittest.TestCase class inheritance it's working")
        self.assertIsInstance(self,TestInfoBot)
        self.log.info("assertIsInstance : TestInfoBase class inheritance it's working")

    def test_002_bots_methods(self):
        self.log.info("dummy test to check setup and teardown methods")
        self.assertIsInstance(self.bot,BotBase)
