# -*- coding: utf-8 -*-
"""TODO"""


import os
import sys
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers.logger_manager import LoggerManager
from qacode.core.utils import settings
from selenium import webdriver as WebDriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait


class BotBase(object):
    """Class Base for handle selenium functionality throught this wrapper

        curr_caps -- Capabilities class

        curr_driver -- WebDriver class

        curr_driver_path -- WebDriver browser executable path

        curr_driver_wait -- Wait for expected conditions

        curr_driver_actions -- Performs actions on elements

        curr_driver_touch -- Perform touch actions on elements

        navigation -- Bot methods to brigde selenium functions

        bot_config -- Bot configuration object

        logger_manager -- logger manager class loaded from
            LoggerManager object

        log -- log class to write messages
    """

    settings = None

    curr_caps = None
    curr_driver = None
    curr_driver_path = None
    # Browser options
    curr_options = None
    # Wait for expected conditions
    curr_driver_wait = None
    # Performs actions on elements
    curr_driver_actions = None
    # Perform touch actions on elements
    curr_driver_touch = None
    navigation = None
    logger_manager = None
    log = None
    IS_64BITS = sys.maxsize > 2**32
    IS_WIN = os.name == 'nt'

    def __init__(self, **kwargs):
        """Create new Bot browser based on options object what can be
            (help for each option can be found on settings.json)

        Arguments:
            settings {dict} -- configuracion obtained from JSON
                file to dict instance

        Raises:
            CoreException -- Fail at instance LoggerManager class
            CoreException -- settings is None
            CoreException -- settings.get('mode') is not in [local, remote]
        """
        self.settings = kwargs.get("bot")
        # default read from qacode.configs, file named 'settings.json'
        if not self.settings:
            self.settings = settings().get('bot')
        self._load()

    def _load(self):
        self.logger_manager = LoggerManager(
            log_path=self.settings.get('log_output_file'),
            log_name=self.settings.get('log_name'),
            log_level=self.settings.get('log_level')
        )
        self.log = self.logger_manager.logger
        required_keys = [
            'mode',
            'browser',
            'options',
            'url_hub',
            'drivers_path',
            'drivers_names',
            'log_name',
            'log_output_file',
            'log_level',
        ]
        for setting in self.settings.keys():
            if setting not in required_keys:
                raise CoreException(
                    message=("Key for config isn't "
                             "valid for key='{}'").format(setting))
        # Configure browser settings
        browser_name = self.settings.get('browser')
        headless_enabled = self.settings.get('options').get('headless')
        self.curr_caps = self.get_capabilities(
            browser_name=browser_name)
        self.curr_options = self.get_options(
            browser_name=browser_name,
            headless_enabled=headless_enabled)
        if self.settings.get('mode') == 'local':
            self.mode_local(browser_name=browser_name)
        elif self.settings.get('mode') == 'remote':
            self.mode_remote(browser_name=browser_name)
        else:
            raise CoreException(
                message=("Bad mode selected, mode={}"
                         "").format(self.settings.get('mode')))
        self.curr_driver_wait = WebDriverWait(self.curr_driver, 10)
        self.curr_driver_actions = ActionChains(self.curr_driver)
        self.curr_driver_touch = TouchActions(self.curr_driver)
        self.navigation = NavBase(
            self.curr_driver,
            self.log,
            driver_wait=self.curr_driver_wait,
            driver_actions=self.curr_driver_actions,
            driver_touch=self.curr_driver_touch,
        )

    def get_capabilities(self, browser_name='chrome'):
        browser_name = self.settings.get('browser')
        capabilities = None
        if browser_name == 'chrome':
            capabilities = DesiredCapabilities.CHROME.copy()
        elif browser_name == 'firefox':
            capabilities = DesiredCapabilities.FIREFOX.copy()
        elif browser_name == 'iexplorer':
            capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
        elif browser_name == 'edge':
            capabilities = DesiredCapabilities.EDGE.copy()
        elif browser_name == 'opera':
            capabilities = DesiredCapabilities.OPERA.copy()
        else:
            raise CoreException(
                message='Bad browser selected at load options')
        return capabilities

    def get_options(self, browser_name='chrome', headless_enabled=False):
        options = None
        if browser_name == 'firefox':
            options = FirefoxOptions()
        elif browser_name == 'chrome':
            options = ChromeOptions()
        elif browser_name == 'iexplorer':
            raise NotImplementedError("Open an issue at github")
        elif browser_name == 'edge':
            raise NotImplementedError("Open an issue at github")
        elif browser_name == 'opera':
            options = OperaOptions()
        else:
            raise CoreException(message='Bad browser selected')
        if headless_enabled:
            options.add_argument("--headless")
        return options

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
        for name in self.settings.get('drivers_names'):
            if name.endswith(driver_name_format):
                return driver_name_format
        raise CoreException(
            message='Driver name not found {}'.format(
                driver_name_format))

    def mode_local(self, browser_name='chrome'):
        """Open new brower on local mode

        Raises:
            CoreException -- driver_name on config JSON
                file is not valid value
        """
        driver_name = self.driver_name_filter(driver_name=browser_name)
        # TODO: Need it ? maybe a test for this ?
        self.curr_driver_path = os.path.abspath("{}/{}".format(
            self.settings.get('drivers_path'),
            driver_name))
         
        sys.path.append(self.curr_driver_path)
        self.log.debug('Starting browser with mode : LOCAL ...')
        if browser_name == "chrome":
            self.curr_driver = WebDriver.Chrome(
                executable_path=self.curr_driver_path,
                desired_capabilities=self.curr_caps,
                chrome_options=self.curr_options
            )
        elif browser_name == "firefox":
            self.curr_driver = WebDriver.Firefox(
                executable_path=self.curr_driver_path,
                capabilities=self.curr_caps,
                firefox_options=self.curr_options)
        elif browser_name == "iexplorer":
            self.curr_driver = WebDriver.Ie(
                executable_path=self.curr_driver_path,
                capabilities=self.curr_caps)
        elif browser_name == "edge":
            self.curr_driver = WebDriver.Edge(
                executable_path=self.curr_driver_path,
                capabilities=self.curr_caps)
        elif browser_name == "opera":
            self.curr_driver = WebDriver.Opera(
                executable_path=self.curr_driver_path,
                desired_capabilities=self.curr_caps,
                options=self.curr_options)
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
        browser_name = self.settings.get('browser')
        url_hub = self.settings.get('url_hub')
        options = None
        self.log.debug('Starting browser with mode : REMOTE ...')
        self.curr_driver = RemoteWebDriver(
            command_executor=url_hub,
            desired_capabilities=self.curr_caps,
            options=self.curr_options
        )
        self.log.info('Started browser with mode : REMOTE OK')

    def close(self):
        """Close curr_driver browser"""
        self.log.debug('Closing browser...')
        self.curr_driver.quit()
        self.log.info('Closed browser')

    def __repr__(self):
        """Show basic properties for this object"""
        _settings = None
        if self.settings.get("mode") == "remote":
            hidden = {
                "drivers_names": [
                    "Hidden at '__repr__' for remote drivers..."]}
            _settings = self.settings.copy()
            _settings.update(hidden)
        return ("BotBase: IS_WIN={}, IS_64BITS={}\n"
                "  navigation={} \n"
                "  settings={}").format(
            self.IS_WIN,
            self.IS_64BITS,
            repr(self.navigation),
            self.settings)
