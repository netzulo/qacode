import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.bots.BotBase import BotBase
from qacode.core.bots.BotOptions import  BotOptions
from qacode.core.exceptions.CoreException import CoreException
from qacode.core.testing.TestInfoBase import TestInfoBase


class TestBotBase(TestInfoBase): 
    def __init__(self, methodName="TEST_BOTS"):
        super(TestBotBase, self).__init__(methodName)          

    @unittest.skip("BOT local for firefox it's failing")
    def test_001_bot_local_firefox(self):
        cfg.get("BOT")['browser'] = 'firefox'
        self.bot = BotBase(BotOptions(iniNoseFile=cfg))
        self.bot.log.info('BOT STARTED')
        time.sleep(5)
        self.bot.close()

    def test_002_bot_local_chrome(self):
        cfg.get("BOT")['browser'] = 'chrome'
        self.bot = BotBase(BotOptions(iniNoseFile=cfg))
        self.bot.log.info('BOT STARTED')
        time.sleep(5)
        self.bot.close()
if __name__ == '__main__':
    unittest.main()
