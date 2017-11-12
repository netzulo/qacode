# -*- coding: utf-8 -*-
"""TODO"""

import os
import sys
from selenium import webdriver as WebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from qacode.core.bots.modules.NavBase import NavBase
from qacode.core.exceptions.CoreException import CoreException


class BotBase(object):
    '''
    Class Base for handle selenium functionality
    Properties
      curr_caps : Capabilities class
      curr_driver : WebDriver class
      curr_driver_path : WebDriver browser executable path
      navigation : Bot methods to brigde selenium functions
      bot_config : Bot configuration object
      logger_manager : logger manager class loaded from BotConfig object
      log : log class to write messages
    '''
    curr_caps = None
    curr_driver = None
    curr_driver_path = None
    navigation = None
    bot_config = None
    logger_manager = None
    log = None
    IS_64BITS = sys.maxsize > 2**32
    IS_WIN = os.name == 'nt'

    def __init__(self, bot_config):
        """
        Create new Bot browser based on options object what can be:
        (help for each option can be found on settings.json)
        """
        if bot_config is None:
            raise CoreException(
                message=("BotBase configuration can't be none: bad "
                         "bot_config provided")
            )
        else:
            try:
                self.bot_config = bot_config
                self.logger_manager = bot_config.logger_manager
                self.log = self.bot_config.log
            except Exception as err:
                raise CoreException(
                    err,
                    message="Error at create LoggerManager for BotBase class"
                )
            if self.bot_config.config['mode'] == 'local':
                self.curr_driver_path = self.driver_name_filter(
                    driver_name=self.bot_config.config['browser'])
                self.mode_local()
            elif self.bot_config.config['mode'] == 'remote':
                self.mode_remote()
            else:
                raise CoreException(
                    message=("Unkown word for bot mode config value: {}"
                             .format(self.bot_config.bot_mode))
                )

            self.navigation = NavBase(self.curr_driver)
            self.curr_driver_wait = WebDriverWait(self.curr_driver, 10)

    def driver_name_filter(self, driver_name=None):
        """
        driver_name_format = {driver_name}{arch}{os}
        examples:
          chromedriver_32.exe
          firefox_64
        """
        driver_name_format = '{}{}{}'
        if driver_name is None:
            raise CoreException(message='driver_name received it\'s None')
        driver_name_format = driver_name_format.format(
            driver_name, '{}', '{}'
        )
        if self.IS_WIN:
            driver_name_format = driver_name_format.format('{}', '.exe')
        else:
            driver_name_format = driver_name_format.format('{}', '')
        if self.IS_64BITS:
            driver_name_format = driver_name_format.format('driver_64')
        else:
            driver_name_format = driver_name_format.format('driver_32')

        for name in self.bot_config.config['drivers_names']:
            if name.endswith(driver_name_format):
                return driver_name_format
        raise CoreException(
            message='Driver name not found {}'.format(
                driver_name_format))

    def mode_local(self):
        """Open new brower on local mode"""
        browser_name = self.bot_config.config['browser']
        if browser_name == "chrome":
            self.curr_caps = DesiredCapabilities.CHROME.copy()
            self.curr_driver = WebDriver.Chrome(
                executable_path=self.curr_driver_path,
                desired_capabilities=self.curr_caps
            )
        elif browser_name == "firefox":
            self.curr_caps = DesiredCapabilities.FIREFOX.copy()
            self.curr_driver = WebDriver.Firefox(
                executable_path=self.curr_driver_path,
                capabilities=self.curr_caps
            )
        elif browser_name == "iexplorer":
            self.curr_caps = DesiredCapabilities.INTERNETEXPLORER.copy()
            self.curr_driver = WebDriver.Ie(
                executable_path=self.curr_driver_path,
                capabilities=self.curr_caps
            )
        elif browser_name == "edge":
            self.curr_caps = DesiredCapabilities.EDGE.copy()
            self.curr_driver = WebDriver.Edge(
                executable_path=self.curr_driver_path,
                capabilities=self.curr_caps
            )
        elif browser_name == "phantomjs":
            self.curr_caps = DesiredCapabilities.PHANTOMJS.copy()
            self.curr_driver = WebDriver.PhantomJS(
                executable_path=self.curr_driver_path,
                desired_capabilities=self.curr_caps
            )
        else:
            raise CoreException(
                message=("config file error, SECTION=bot, KEY=browser isn't "
                         "valid value: {}".format(browser_name)),
                log=self.log
            )

    def mode_remote(self):
        """
        Open new brower on remote mode
        """
        browser_name = self.bot_config.config['browser']
        url_hub = self.bot_config.config['url_hub']
        self.log.info('Starting browser with mode : REMOTE')
        if browser_name == 'firefox':
            self.curr_caps = DesiredCapabilities.FIREFOX.copy()

        elif browser_name == 'chrome':
            self.curr_caps = DesiredCapabilities.CHROME.copy()

        elif browser_name == 'iexplorer':
            self.curr_caps = DesiredCapabilities.INTERNETEXPLORER.copy()

        elif browser_name == 'phantomjs':
            self.curr_caps = DesiredCapabilities.PHANTOMJS.copy()

        elif browser_name == 'edge':
            self.curr_caps = DesiredCapabilities.EDGE.copy()
        else:
            raise CoreException(message='Bad browser selected')

        self.curr_driver = RemoteWebDriver(
            command_executor=url_hub,
            desired_capabilities=self.curr_caps)
        self.log.info('Started browser with mode : REMOTE OK')

    def close(self):
        """
        Close curr_driver browser
        """
        self.log.info('Closing browser')
        self.curr_driver.quit()
        self.log.info('Closed browser OK')
