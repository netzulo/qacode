# -*- coding: utf-8 -*-
"""Testsuite for package bots"""


import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers.logger_manager import Log
from qacode.core.testing.asserts import Assert
from qacode.core.testing.test_info import TestInfoBase
from qacode.utils import settings


ASSERT = Assert()
SETTINGS = settings(file_path="qacode/configs/")
SKIP = SETTINGS['tests']['skip']['browsers']
SKIP_MSG = 'browsers.{} DISABLED by config file'
# TODO: must be setteable from config JSON
WAIT_TO_CLOSE = int(3)
LOGGER_MANAGER = Log(log_level=SETTINGS['bot']['log_level'])


class TestBotBase(TestInfoBase):
    """Testcases for class BotBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestBotBase, self).setup_method(
            test_method, config=settings(file_path="qacode/configs/"))

    def teardown_method(self, method):
        """TODO: doc method"""
        if method.__name__ == 'test_botbase_drivernamefilter_ok':
            return True
        self.try_bot_close()

    def try_bot_close(self):
        """Utility method for tests"""
        try:
            if self.bot:
                self.bot.close()
        except Exception:
            print("ERROR: Failed at try to close bot")

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    @pytest.mark.parametrize("is_win", [True, False])
    @pytest.mark.parametrize("is_64bits", [True, False])
    @pytest.mark.parametrize("browser", ["chrome", "firefox"])
    def test_botbase_drivernamefilter_ok(self, browser, is_win, is_64bits):
        """Testcase: test_botbase_drivernamefilter_ok"""
        if 'bot' not in dir(self):
            settings = SETTINGS.copy()
            self.add_property('bot', BotBase(**settings))
        # end setup
        self.bot.IS_WIN = is_win
        self.bot.IS_64BITS = is_64bits
        name_formatted = self.bot.driver_name_filter(browser)
        if is_win and not is_64bits:
            ASSERT.equals(
                name_formatted, "{}driver_32.exe".format(browser))
        if is_win and is_64bits:
            ASSERT.equals(
                name_formatted, "{}driver_64.exe".format(browser))
        if not is_win and not is_64bits:
            ASSERT.equals(
                name_formatted, "{}driver_32".format(browser))
        if not is_win and is_64bits:
            ASSERT.equals(
                name_formatted, "{}driver_64".format(browser))
            self.try_bot_close()

    @pytest.mark.parametrize("browser_name", [
        "chrome", "firefox", "iexplorer", "edge"])
    @pytest.mark.parametrize("driver_mode", ["local", "remote"])
    def test_bot_modes_and_names(self, driver_mode, browser_name):
        """Testcase: test_001_bot_local_chrome"""
        if SKIP[browser_name][driver_mode]:
            pytest.skip(SKIP_MSG.format(browser_name))
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
        self.bot = BotBase(**settings)
        self.timer(wait=WAIT_TO_CLOSE)
        ASSERT.is_instance(self.bot, BotBase)
        ASSERT.equals(
            self.bot.settings.get('browser'),
            settings.get('bot').get('browser'))
        ASSERT.equals(self.bot.settings.get('mode'), driver_mode)
        ASSERT.equals(self.bot.curr_caps['browserName'], browser_name)

    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    @pytest.mark.parametrize("driver_mode", ["local", "remote"])
    def test_bot_modes_headless(self, driver_mode, browser_name):
        """Testcase: test_bot_modes_headless"""
        if SKIP[browser_name][driver_mode]:
            pytest.skip(SKIP_MSG.format(browser_name))
        settings = SETTINGS.copy()
        settings.get('bot').update({
            'browser': str(browser_name),
            'mode': str(driver_mode),
            'options': {"headless": True}
        })
        self.bot = BotBase(**settings)
        self.timer(wait=WAIT_TO_CLOSE)
        ASSERT.is_instance(self.bot, BotBase)
        ASSERT.equals(
            self.bot.settings.get('browser'),
            settings.get('bot').get('browser'))
        ASSERT.equals(self.bot.settings.get('mode'), driver_mode)
        ASSERT.equals(self.bot.curr_caps['browserName'], browser_name)

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    def test_botbase_invalidsettingskey(self):
        """Testcase: test_botbase_invalidsettingskey"""
        settings = SETTINGS.copy()
        settings.get('bot').update({"must_raises": "test"})
        with pytest.raises(CoreException):
            BotBase(**settings)

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    def test_botbase_invalidmode(self):
        """Testcase: test_botbase_invalidmode"""
        settings = SETTINGS.copy()
        settings.get('bot').update({"mode": "must_raises"})
        with pytest.raises(CoreException):
            self.bot = BotBase(**settings)

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    def test_botbase_invalidbrowser(self):
        """Testcase: test_botbase_invalidbrowser"""
        settings = SETTINGS.copy()
        settings.get('bot').update({"browser": "must_raises"})
        with pytest.raises(CoreException):
            self.bot = BotBase(**settings)
