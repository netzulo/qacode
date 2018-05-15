# -*- coding: utf-8 -*-
"""Testsuite for package bots"""


import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info import TestInfoBase
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_LOCALS = SETTINGS['tests']['skip']['drivers_local']
SKIP_LOCALS_MSG = 'drivers_local DISABLED by config file'
SKIP_REMOTES = SETTINGS['tests']['skip']['drivers_remote']
SKIP_REMOTES_MSG = 'drivers_remote DISABLED by config file'
# TODO: must be setteable from config JSON
WAIT_TO_CLOSE = int(3)
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestBotBase(TestInfoBase):
    """Testcases for class BotBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestBotBase, self).setup_method(
            test_method, config=settings())

    def teardown_method(self, method):
        """TODO: doc method"""
        try:
            if self.bot:
                self.bot.close()
        except Exception:
            print(
                "Fail at try to close bot, maybe never opened")

    @pytest.mark.parametrize("browser_name", [
        "chrome",
        "firefox",
        "iexplorer",
        "edge",
        "opera"
    ])
    @pytest.mark.parametrize("driver_mode", ["local", "remote"])
    def test_bot_modes_and_names(self, driver_mode, browser_name):
        """Testcase: test_001_bot_local_chrome"""
        if SKIP_LOCALS and driver_mode == 'local':
            pytest.skip(SKIP_LOCALS_MSG)
        if SKIP_REMOTES and driver_mode == 'remote':
            pytest.skip(SKIP_REMOTES_MSG)
        settings = SETTINGS.copy()
        settings.get('bot').update({
            'browser': str(browser_name),
            'mode': str(driver_mode)
        })
        if browser_name == 'edge':
            browser_name = 'MicrosoftEdge'
            pytest.skip(msg="Browser not configured")
        if browser_name == 'iexplorer':
            browser_name = 'internet explorer'
        if browser_name == 'opera':
            pytest.skip(
                msg=("Issue opened on official opera"
                     " chromium github: "
                     "https://github.com/operasoftware"
                     "/operachromiumdriver/issues/9"))
        self.bot = BotBase(**settings)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assert_is_instance(self.bot, BotBase)
        self.assert_equals(
            self.bot.settings.get('browser'),
            settings.get('bot').get('browser'))
        self.assert_equals(self.bot.settings.get('mode'), driver_mode)
        self.assert_equals(self.bot.curr_caps['browserName'], browser_name)

    @pytest.mark.parametrize("browser_name", [
        "chrome", "firefox", "opera"
    ])
    @pytest.mark.parametrize("driver_mode", ["local", "remote"])
    def test_bot_modes_headless(self, driver_mode, browser_name):
        """Testcase: test_bot_modes_headless"""
        if SKIP_LOCALS and driver_mode == 'local':
            pytest.skip(SKIP_LOCALS_MSG)
        if SKIP_REMOTES and driver_mode == 'remote':
            pytest.skip(SKIP_REMOTES_MSG)
        settings = SETTINGS.copy()
        settings.get('bot').update({
            'browser': str(browser_name),
            'mode': str(driver_mode),
            'options': {"headless": True}
        })
        if browser_name == 'opera':
            pytest.skip(
                msg=("Issue opened on official opera"
                     " chromium github: "
                     "https://github.com/operasoftware"
                     "/operachromiumdriver/issues/9"))
        self.bot = BotBase(**settings)
        self.timer(wait=WAIT_TO_CLOSE)
        self.assert_is_instance(self.bot, BotBase)
        self.assert_equals(
            self.bot.settings.get('browser'),
            settings.get('bot').get('browser'))
        self.assert_equals(self.bot.settings.get('mode'), driver_mode)
        self.assert_equals(self.bot.curr_caps['browserName'], browser_name)
