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

    def test_003_bot_local_phantomjs(self):
        self.log.debug("TestBotBase: started for PHANTOMJS")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "phantomjs"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: terminated for PHANTOMJS")

    def test_004_bot_local_iexplorer(self):
        self.log.debug("TestBotBase: started for IEXPLORER")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "iexplorer"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: terminated for IEXPLORER")

    def test_005_bot_local_edge(self):
        self.log.debug("TestBotBase: started for EDGE")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "edge"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: terminated for EDGE")