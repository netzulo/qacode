import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.pages.PageBase import PageBase

class TestPageBase(TestInfoBase):
    
    def __init__(self, method_name="TestPageBase"):
        super(TestPageBase, self).__init__(method_name, logger_manager=None)

    def test_001_page_base_instance(self):
        try:
            self.bot = BotBase(BotConfig(nose_config=cfg))
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'])
            assert cfg['TEST_UNITARIES']['url'] in self.bot.curr_driver.current_url
        except Exception as err:
            raise Exception(err)
        finally:
            self.bot.close()
            
    def test_002_page_base_instance_go_url_False(self):
        try:
            self.bot = BotBase(BotConfig(nose_config=cfg))
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'], go_url=False)
            assert cfg['TEST_UNITARIES']['url'] not in self.bot.curr_driver.current_url
        except Exception as err:
            raise Exception(err)
        finally:
            self.bot.close()
   
    def test_003_page_base_method_go_page_url(self):
        try:
            url_second_page = "https://www.netzulo.com"
            self.bot = BotBase(BotConfig(nose_config=cfg))
            page = PageBase(self.bot,cfg['TEST_UNITARIES']['url'])
            assert cfg['TEST_UNITARIES']['url'] in self.bot.curr_driver.current_url
            page.go_page_url(url_second_page )
            assert url_second_page in self.bot.curr_driver.current_url
        except Exception as err:
            raise Exception(err)
        finally:
            self.bot.close()

if __name__ == '__main__':
    unittest.main()
