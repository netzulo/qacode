# -*- coding: utf-8 -*-
"""Testsuite for package bots"""


import pytest
from qacode.core.bots.bot_base import BotBase
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.testing.test_info import TestInfoBase
from qautils.files import settings


SETTINGS = settings(file_path="qacode/configs/")
SKIP = SETTINGS['tests']['skip']['benchmarks']
SKIP_MSG = 'benchmarks DISABLED by config file'
# TODO: must be setteable from config JSON
LOGGER_MANAGER = LoggerManager(log_level=SETTINGS['bot']['log_level'])
ITERATIONS = 2
ROUNDS = 2


class TestBotBase(TestInfoBase):
    """Testcases for class BotBase"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestBotBase, self).setup_method(
            test_method,
            config=settings(file_path="qacode/configs/"),
            skip_force=SKIP)

    def bot_benchmark(self, browser_name, driver_mode, is_headless):
        """Allow to open and close any browser_name with
            any driver_mode configuration

        Arguments:
            browser_name {str} -- browser name
            driver_mode {str} -- driver mode (local, remote)
        """
        settings = SETTINGS.copy()
        settings.get('bot').update({
            'browser': str(browser_name),
            'mode': str(driver_mode),
            'options': {'headless': is_headless}
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

    @pytest.mark.benchmark(group='BROWSERS')
    @pytest.mark.parametrize("browser_name", [
        "chrome",
        "firefox",
        "iexplorer",
        "edge",
        "opera"
    ])
    @pytest.mark.parametrize("driver_mode", ["local", "remote"])
    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    def test_benchmark_browsers(self, benchmark, browser_name, driver_mode):
        """Testcase: test_benchmark_local_chrome"""
        if SKIP:
            pytest.skip(SKIP_MSG)
        cfg_local = {
            'browser_name': browser_name,
            'driver_mode': driver_mode,
            'is_headless': False
        }
        benchmark.pedantic(
            self.bot_benchmark,
            kwargs=cfg_local,
            iterations=ITERATIONS,
            rounds=ROUNDS)

    @pytest.mark.benchmark(group='BROWSERS_HEADLESS')
    @pytest.mark.parametrize("browser_name", [
        "chrome", "firefox", "opera"
    ])
    @pytest.mark.parametrize("driver_mode", ["local", "remote"])
    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    def test_benchmark_browsers_headless(self, benchmark,
                                         browser_name, driver_mode):
        """Testcase: test_benchmark_local_chrome"""
        if SKIP:
            pytest.skip(SKIP_MSG)
        cfg_local = {
            'browser_name': browser_name,
            'driver_mode': driver_mode,
            'is_headless': True
        }
        benchmark.pedantic(
            self.bot_benchmark,
            kwargs=cfg_local,
            iterations=ITERATIONS,
            rounds=ROUNDS)
