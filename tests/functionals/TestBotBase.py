import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase


class TestBotBase(TestInfoBase):     

    def __init__(self, method_name="TestBotBase"):
        super(TestBotBase, self).__init__(method_name, logger_manager=None)
   
    def test_001_bot_local_chrome(self):
        self.log.debug("TestBotBase: started for CHROME")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "chrome"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: terminated for CHROME")
    
    def test_002_bot_local_firefox(self):
        self.log.debug("TestBotBase: started for FIREFOX")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "firefox"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: terminated for FIREFOX")
