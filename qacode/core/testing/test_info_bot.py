# -*- coding: utf-8 -*-
"""Package qacode.core.testing"""


from qacode.core.bots.bot_base import BotBase
from qacode.core.bots.bot_config import BotConfig
from qacode.core.testing.test_info_base import TestInfoBase


class TestInfoBot(TestInfoBase):
    """Inherit class what implements bot on each testcase"""

    bot_config = None
    bot = None
    is_bot_instance = False

    def __init__(self, method_name="TestInfoBot", logger_manager=None,
                 test_config=None,
                 bot=None):
        """
        Allows to execute tests what open and close
         BotBase on each test method
        :args:
            bot: if contain instance of BotBase, then load bot
             config and logger_manager for self as properties
        """
        super(TestInfoBot, self).__init__(method_name=method_name,
                                          logger_manager=logger_manager,
                                          test_config=test_config)
        if bot is not None and isinstance(bot, BotBase):
            self.is_bot_instance = True
            self.bot = bot
            self.test_config = bot.bot_config
            self.logger_manager = bot.logger_manager

    def setUp(self):
        """Each testcase instance BotBase class"""
        super(TestInfoBot, self).setUp()
        if self.bot is None and not self.is_bot_instance:
            self.bot = TestInfoBot.bot_open(
                self.test_config, self.logger_manager)

    def tearDown(self):
        """Each testcase shutdown BotBase instance"""
        super(TestInfoBot, self).tearDown()
        if not self.is_bot_instance:
            self.bot_close(self.bot)

    @classmethod
    def bot_close(cls, bot):
        """Close bot and return close return result"""
        bot.close()

    @classmethod
    def bot_open(cls, test_config, logger_manager):
        """Open bot and return it"""
        bot_config = BotConfig(
            test_config,
            logger_manager)
        return BotBase(bot_config)
