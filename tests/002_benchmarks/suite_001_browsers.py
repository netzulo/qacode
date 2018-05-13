# -*- coding: utf-8 -*-
"""Testsuite for package bots"""


import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info import TestInfoBase
from qacode.core.utils import settings


SETTINGS = settings()
SKIP_LOCALS = SETTINGS['tests']['skip']['benchmarks']
SKIP_LOCALS_MSG = 'benchmarks DISABLED by config file'
# TODO: must be setteable from config JSON
WAIT_TO_CLOSE = int(3)
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])


class TestBotBase(TestInfoBase):
    """Testcases for class BotBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestBotBase, self).setup_method(
            test_method, config=settings())

    def bot_benchmark(self, browser_name, driver_mode):
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
        try:
            if self.bot:
                self.bot.close()
        except Exception:
            print(
                "Fail at try to close bot, maybe never opened")

    @pytest.mark.benchmark(group='CHROME_QACODE')
    @pytest.mark.parametrize("browser_name", [
        "chrome",
        "firefox",
        "phantomjs",
        "iexplorer",
        "edge",
        "opera"
    ])
    @pytest.mark.parametrize("driver_mode", ["local", "remote"])
    def test_benchmark_browsers(self, benchmark, browser_name, driver_mode):
        """Testcase: test_benchmark_local_chrome"""
        if SKIP_LOCALS:
            pytest.skip(SKIP_LOCALS_MSG)
        cfg_local = {'browser_name': browser_name, 'driver_mode': driver_mode}
        benchmark.pedantic(
            self.bot_benchmark, kwargs=cfg_local, iterations=1, rounds=1)