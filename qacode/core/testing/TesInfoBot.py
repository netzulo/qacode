from testconfig import config as cfg # just works when nose command it's launched>
from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase 


class TestInfoBot(TestInfoBase):
    """Inherit class what implements"""

    is_multiple_bot = None
    bot_config = BotConfig
    bot = BotBase

    def __init__(self, method_name="TESTSUITE_NAME", logger_manager=None, is_multiple_bot=True):
        super(TestInfoBot, self).__init__(method_name,logger_manager)
        if is_multiple_bot is None:
            raise Exception("Param is_multiple_bot (bool) can't be None")
        self.is_multiple_bot = is_multiple_bot

    def setUp(self):   
        super(TestInfoBot,self).setUp()
        self.bot_config = BotConfig(nose_config=cfg, logger_manager=self.logger_manager)
        self.bot = BotBase(self.bot_config)

    def tearDown(self):
        super(TestInfoBot,self).tearDown()
        self.bot.close()