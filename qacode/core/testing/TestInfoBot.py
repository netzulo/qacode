import time, unittest, logging
from testconfig import config as cfg # just works when nose command it's launched>
from qacode.loggers.LoggerManager import LoggerManager
from qacode.core.bots.BotOptions import BotOptions
from qacode.core.bots.BotBase import BotBase
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.exceptions.TestAssertionError import TestAssertionError

class TestInfoBot(TestInfoBase):
    '''
    Create LoggerManager and instance bot
    '''

    def __init__(self, methodName="NO_TESTCASE_NAME"):
        super(TestInfoBot, self).__init__(methodName)

    @classmethod
    def setUpClass(cls):
        """
        Just starting testcase instance dependencies
        Dependencies:
          [core] Base class, Instance testlink dependencies
        Notes:
          [core] Initialize bot as class property
        """
        cls.bot = BotBase(BotOptions(iniNoseFile=cfg))
        cls.log = cls.bot.log
        
    @classmethod
    def tearDownClass(cls):
        """
        Just stopping testcase instance
        Notes:
          [core] Close bot from class property
        """
        cls.bot.close()
        pass

    def sleep(self, wait=0):
        """        
        Just call to native python time.sleep() method
        Notes:
          Just wait time on Runtime execution before execute next lane of code           
        """
        super(TestInfoBot,self).sleep(wait)

if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(verbosity=1, failfast=True))
