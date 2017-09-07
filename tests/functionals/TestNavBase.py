import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase

class TestNavBase(TestInfoBase):
    
    def __init__(self, method_name="TestNavBase"):
        super(TestNavBase, self).__init__(method_name, logger_manager=None)

    def test_001_page_base_go_url_without_wait_param(self):
        try:
            self.bot = BotBase(BotConfig(nose_config=cfg))
            self.bot.navigation.get_url(cfg['TEST_UNITARIES']['url'])
        except Exception as err:
            raise Exception(err)
        finally:
            self.bot.close()

    def test_001_page_base_go_url_with_wait_param(self):
        try:
            self.bot = BotBase(BotConfig(nose_config=cfg))
            self.bot.navigation.get_url(cfg['TEST_UNITARIES']['url'], wait_for_load=0)
        except Exception as err:
            raise Exception(err)
        finally:
            self.bot.close()    


if __name__ == '__main__':
    unittest.main()
