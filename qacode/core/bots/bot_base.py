# -*- coding: utf-8 -*-
"""TODO"""


import os
import sys
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.exceptions.core_exception import CoreException
from selenium import webdriver as WebDriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait


class BotBase(object):
    """Class Base for handle selenium functionality throught this wrapper

        curr_caps -- Capabilities class

        curr_driver -- WebDriver class

        curr_driver_path -- WebDriver browser executable path

        navigation -- Bot methods to brigde selenium functions

        bot_config -- Bot configuration object

        logger_manager -- logger manager class loaded from BotConfig object

        log -- log class to write messages
    """

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
        """Create new Bot browser based on options object what can be
            (help for each option can be found on settings.json)

        Arguments:
            bot_config {BotConfig} -- object containing configuration
                for new bot instance

        Raises:
            CoreException -- Fail at instance LoggerManager class
            CoreException -- bot_config param is None
            CoreException -- bot_config.mode is not in [local, remote]
        """
        if bot_config is None:
            raise CoreException(
                message=("BotBase configuration can't be none: bad bot_config"
                         " provided"))
        self.bot_config = bot_config
        self.logger_manager = bot_config.logger_manager
        self.log = self.bot_config.log
        if self.bot_config.config['mode'] == 'local':
            self.mode_local()
        elif self.bot_config.config['mode'] == 'remote':
            self.mode_remote()
        # else: handled at BotConfig
        self.curr_driver_wait = WebDriverWait(self.curr_driver, 10)
        self.navigation = NavBase(
            self.curr_driver, self.log, driver_wait=self.curr_driver_wait)

    def driver_name_filter(self, driver_name=None):
        """Filter names of driver to search selected on config list

        Keyword Arguments:
            driver_name {str} -- driver_name_format is
                {driver_name}{arch}{os} (default: {None})

        Raises:
            CoreException -- driver_name param is None
            CoreException -- driver_name not in

        Returns:
            str -- name of driver
                (example: chromedriver_32.exe)
        """
        driver_name_format = '{}{}{}'
        if driver_name is None:
            raise CoreException(message='driver_name received it\'s None')
        driver_name_format = driver_name_format.format(
            driver_name, '{}', '{}')
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
        """Open new brower on local mode

        Raises:
            CoreException -- driver_name on config JSON
                file is not valid value
        """
        browser_name = self.bot_config.config['browser']
        driver_name = self.driver_name_filter(driver_name=browser_name)
        self.curr_driver_path = os.path.abspath("{}/{}".format(
            self.bot_config.config['drivers_path'],
            driver_name))
        # add to path before to open
        sys.path.append(self.curr_driver_path)
        self.log.debug('Starting browser with mode : LOCAL ...')
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
        elif browser_name == "opera":
            self.curr_caps = DesiredCapabilities.OPERA.copy()
            self.curr_driver = WebDriver.Opera(
                executable_path=self.curr_driver_path,
                desired_capabilities=self.curr_caps
            )
        else:
            raise CoreException(
                message=("config file error, SECTION=bot, KEY=browser isn't "
                         "valid value: {}".format(browser_name)),
                log=self.log
            )
        self.log.info('Started browser with mode : REMOTE OK')

    def mode_remote(self):
        """Open new brower on remote mode

        Raises:
            CoreException -- browser name is not in valid values list
        """
        browser_name = self.bot_config.config['browser']
        url_hub = self.bot_config.config['url_hub']
        self.log.debug('Starting browser with mode : REMOTE ...')
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

        elif browser_name == 'opera':
            self.curr_caps = DesiredCapabilities.OPERA.copy()
        else:
            raise CoreException(message='Bad browser selected')

        self.curr_driver = RemoteWebDriver(
            command_executor=url_hub,
            desired_capabilities=self.curr_caps)
        self.log.info('Started browser with mode : REMOTE OK')

    def close(self):
        """Close curr_driver browser"""
        self.log.debug('Closing browser...')
        self.curr_driver.quit()
        self.log.info('Closed browser')
