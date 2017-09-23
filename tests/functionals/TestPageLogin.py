import unittest, logging, time
from testconfig import config as cfg # just works when nose command it's launched
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.pages.PageLogin import PageLogin


class TestPageLogin(TestInfoBase):
    """description of class"""


    def __init__(self, method_name="TestPageBase"):
        super(TestPageLogin, self).__init__(method_name, logger_manager=None)

    def test_001_page_login_instance(self):
        try:
            self.bot = BotBase(BotConfig(nose_config=cfg))
            page = PageLogin(self.bot,cfg['TEST_FUNCTIONALS']['url'])
            assert cfg['TEST_FUNCTIONALS']['url'] in self.bot.curr_driver.current_url
        except Exception as err:
            raise Exception(err)
        finally:
            self.bot.close()