import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase


class TestBotBase(TestInfoBase):     

    def __init__(self, method_name="TestTestInfoBase"):
        super(TestBotBase, self).__init__(method_name, logger_manager=None)
   
    def test_001_bot_local_chrome(self):
        self.log.debug("TestBotBase: started")
        self.bot = BotBase(BotConfig(nose_config=cfg, logger_manager=self.logger_manager))
        self.log.debug("TestBotBase: terminated")
        
