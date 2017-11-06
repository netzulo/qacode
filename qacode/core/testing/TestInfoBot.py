# -*- coding: utf-8 -*-
"""Package testing"""


from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.exceptions.CoreException import CoreException


class TestInfoBot(TestInfoBase):
    """Inherit class what implements bot on each testcase"""

    bot_config = None
    bot = None
    is_bot_instance = False

    def __init__(self, method_name="TestInfoBot", logger_manager=None,
                 test_config=None,
                 bot=None):
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
            config=test_config,
            logger_manager=logger_manager)
        return BotBase(bot_config)
         