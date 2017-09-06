import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.pages.PageBase import PageBase

class TestNavBase(TestInfoBase):
    
    def __init__(self, method_name="TestNavBase"):
        super(TestNavBase, self).__init__(method_name, logger_manager=None)

    def test_001_page_base_go_url_param(self):
        # TODO: open web page throught bot on nav Class
        self.bot = BotBase(BotConfig(nose_config=cfg))
        self.bot.navigation.get_url("http://demoqa.com", wait_for_load=10)
        self.bot.close()


if __name__ == '__main__':
    unittest.main()
