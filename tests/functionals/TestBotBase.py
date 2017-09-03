import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase


class TestBotBase(TestInfoBase):     

    def __init__(self, method_name="TestBotBase"):
        super(TestBotBase, self).__init__(method_name, logger_manager=None)
   
    def test_001_bot_local_chrome(self):
        self.log.debug("TestBotBase: LOCAL started for CHROME")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "chrome"
        bot_config.bot_mode = "local"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for CHROME")
    
    def test_002_bot_local_firefox(self):
        self.log.debug("TestBotBase: LOCAL started for FIREFOX")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "firefox"
        bot_config.bot_mode = "local"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for FIREFOX")

    def test_003_bot_local_phantomjs(self):
        self.log.debug("TestBotBase: LOCAL started for PHANTOMJS")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "phantomjs"
        bot_config.bot_mode = "local"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for PHANTOMJS")

    def test_004_bot_local_iexplorer(self):
        self.log.debug("TestBotBase: LOCAL started for IEXPLORER")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "iexplorer"
        bot_config.bot_mode = "local"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for IEXPLORER")

    def test_005_bot_local_edge(self):
        self.log.debug("TestBotBase: LOCAL started for EDGE")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "edge"
        bot_config.bot_mode = "local"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: LOCAL terminated for EDGE")

    def test_006_bot_remote_chrome(self):
        self.log.debug("TestBotBase: REMOTE started for CHROME")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "chrome"
        bot_config.bot_mode = "remote"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for CHROME")

    def test_007_bot_remote_firefox(self):
        self.log.debug("TestBotBase: REMOTE started for FIREFOX")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "firefox"
        bot_config.bot_mode = "remote"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for FIREFOX")

    def test_008_bot_remote_phantomjs(self):
        self.log.debug("TestBotBase: REMOTE started for PHANTOMJS")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "phantomjs"
        bot_config.bot_mode = "remote"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for PHANTOMJS")

    def test_009_bot_remote_iexplorer(self):
        self.log.debug("TestBotBase: REMOTE started for IEXPLORER")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "iexplorer"
        bot_config.bot_mode = "remote"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for IEXPLORER")

    def test_010_bot_remote_edge(self):
        self.log.debug("TestBotBase: REMOTE started for EDGE")
        bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        bot_config.bot_browser = "edge"
        bot_config.bot_mode = "remote"
        self.bot = BotBase(bot_config)
        time.sleep(10)
        self.bot.close()
        self.log.debug("TestBotBase: REMOTE terminated for EDGE")