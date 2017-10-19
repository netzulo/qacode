# -*- coding: utf-8 -*-
"""Package testing"""


from qacode.core.testing.TestInfoBase import TestInfoBase
from qacode.core.bots.BotConfig import BotConfig
from qacode.core.bots.BotBase import BotBase
from qacode.core.exceptions.CoreException import CoreException


class TestInfoBot(TestInfoBase):
    """Inherit class what implements bot on each testcase"""

    is_multiple_bot = None
    bot_config = None
    bot = None

    def __init__(self, method_name="TestInfoBot", logger_manager=None,
                 test_config=None,
                 is_multiple_bot=True):
        super(TestInfoBot, self).__init__(method_name=method_name,
                                          logger_manager=logger_manager,
                                          test_config=test_config)
        if is_multiple_bot is None:
            raise CoreException(
                message='Param is_multiple_bot (bool) can\'t be None'
            )
        self.is_multiple_bot = is_multiple_bot

    def setUp(self):
        """Each testcase instance BotBase class"""
        super(TestInfoBot, self).setUp()
        if not self.is_multiple_bot:
            raise CoreException(
                message='Unique bot for testSuite not implemented'
            )
        self.bot_config = BotConfig(
            config=self.test_config,
            logger_manager=self.logger_manager
        )
        self.bot = BotBase(self.bot_config)

    def tearDown(self):
        """Each testcase shutdown BotBase instance"""
        super(TestInfoBot, self).tearDown()
        self.bot.close()
