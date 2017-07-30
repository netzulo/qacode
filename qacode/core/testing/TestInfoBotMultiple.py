import time, unittest
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.exceptions.TestAssertionError import TestAssertionError

class TestInfoBotMultiple(TestInfoBase):

    def __init__(self, method_name="NO_TESTCASE_NAME"):
        super(TestInfoBotMultiple, self).__init__(method_name)

    def setUp(self, config=cfg):
        """
        Just starting testcase instance dependencies
        Dependencies:
          TODO: Teslink, Instance testlink dependencies
        Notes:
          Initialize bot by testcase method
          IMPORTANT: inherits must call super(classInheritName, self).setup()
        """        
        self.bot = BotBase(BotConfig(nose_config=config))

    def tearDown(self):
        '''
        Close bot by testcase method
        '''
        self.bot.close()

    def sleep(self, wait=0):
        """        
        Just call to native python time.sleep() method
        Notes:
          Just wait time on Runtime execution before execute next lane of code           
        """
        super(TestInfoBotMultiple,self).sleep(wait)

if __name__ == '__main__':
    unittest.main()    
