# -*- coding: utf-8 -*-
"""TODO"""


import os
import sys
from qacode.core.bots.modules.nav_base import NavBase
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers.logger_manager import LoggerManager
from qautils.files import settings
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
    BROWSERS_WITHOUT_OPTIONS = ('iexplorer', 'edge')

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
            log_level=self.settings.get('log_level'))
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
                msg_setting = ("Key for config isn't valid for"
                               " key='{}'").format(setting)
                raise CoreException(
                    message=msg_setting,
                    log=self.log)
        # Configure browser settings
        browser_name = self.settings.get('browser')
        headless_enabled = self.settings.get(
            'options').get('headless')
        # Instance selenium settings classes
        self.curr_caps = self.get_capabilities(
            browser_name=browser_name)
        self.curr_options = self.get_options(
            browser_name=browser_name,
            headless_enabled=headless_enabled)
        # Open browser based on mode from settings.json
        if self.settings.get('mode') == 'local':
            self.mode_local(browser_name=browser_name)
        elif self.settings.get('mode') == 'remote':
            self.mode_remote(browser_name=browser_name)
        else:
            raise CoreException(
                message=("Bad mode selected, mode={}"
                         "").format(self.settings.get('mode')),
                log=self.log)
        # Instance all needed for BotBase instance
        self.curr_driver_wait = WebDriverWait(self.curr_driver, 10)
        self.curr_driver_actions = ActionChains(self.curr_driver)
        self.curr_driver_touch = TouchActions(self.curr_driver)
        self.navigation = NavBase(
            self.curr_driver,
            self.log,
            driver_wait=self.curr_driver_wait,
            driver_actions=self.curr_driver_actions,
            driver_touch=self.curr_driver_touch)

    def get_capabilities(self, browser_name='chrome'):
        """Instance DesiredCapabilities class from selenium and return it

        Keyword Arguments:
            browser_name {str} -- name of a valid browser name for selenium
                (default: {'chrome'})

        Raises:
            CoreException -- if name of browser isn't supported

        Returns:
            [DesiredCapabilities] -- DesiredCapabilities inherit
                class instanced for one browser
        """
        capabilities = None
        try:
            capabilities = {
                "chrome": DesiredCapabilities.CHROME.copy(),
                "firefox": DesiredCapabilities.FIREFOX.copy(),
                "iexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
                "edge": DesiredCapabilities.EDGE.copy(),
                "opera": DesiredCapabilities.OPERA.copy(),
            }[browser_name]
        except KeyError:
            raise CoreException(
                message='Bad browser selected at load options',
                log=self.log)
        return capabilities

    def get_options(self, browser_name='chrome', headless_enabled=False):
        """Instance Options class from selenium and return it

        Keyword Arguments:
            browser_name {str} -- name of a valid browser name for selenium
                (default: {'chrome'})
            headless_enabled {bool} -- allow to configure --headless param
                (default: {False})

        Raises:
            CoreException -- if name of browser isn't supported

        Returns:
            [Options] -- Options inherit
                class instanced for one browser
        """
        options = None
        msg_not_conf = ("get_options | : doesn't have configurations"
                        " for browser='{}'".format(browser_name))
        try:
            options = {
                "chrome": ChromeOptions(),
                "firefox": FirefoxOptions(),
                "opera": OperaOptions(),
            }[browser_name]
            if headless_enabled:
                options.add_argument("--headless")
        except KeyError:
            if browser_name in self.BROWSERS_WITHOUT_OPTIONS:
                self.log.debug(msg_not_conf)
            else:
                raise CoreException(
                    message="Bad browser selected",
                    log=self.log)
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
                driver_name_format),
            log=self.log)

    def get_driver_chrome(self, driver_path=None, capabilities=None,
                          options=None):
        """Open WebDriver selenium based on Chrome browser

        Keyword Arguments:
            driver_path {str} -- Path for driver binary path
                (default: {None})
            capabilities {DesiredCapabilities} -- Capabilities for browser
                (default: {None})
            options {Options} -- Options for browser (default: {None})

        Returns:
            [WebDriver.Chrome] -- WebDriver opened and ready to be used
        """
        if driver_path is None:
            driver_path = self.curr_driver_path
        if capabilities is None:
            capabilities = self.curr_caps
        if options is None:
            options = self.curr_options
        return WebDriver.Chrome(
            executable_path=driver_path,
            desired_capabilities=capabilities,
            chrome_options=options)

    def get_driver_firefox(self, driver_path=None, capabilities=None,
                           options=None):
        """Open WebDriver selenium based on Firefox browser

        Keyword Arguments:
            driver_path {str} -- Path for driver binary path
                (default: {None})
            capabilities {DesiredCapabilities} -- Capabilities for browser
                (default: {None})
            options {Options} -- Options for browser (default: {None})

        Returns:
            [WebDriver.Firefox] -- WebDriver opened and ready to be used
        """
        if driver_path is None:
            driver_path = self.curr_driver_path
        if capabilities is None:
            capabilities = self.curr_caps
        if options is None:
            options = self.curr_options
        return WebDriver.Firefox(
            executable_path=driver_path,
            capabilities=capabilities,
            firefox_options=options)

    def get_driver_iexplorer(self, driver_path=None, capabilities=None):
        """Open WebDriver selenium based on InternetExplorer browser

        Keyword Arguments:
            driver_path {str} -- Path for driver binary path
                (default: {None})
            capabilities {DesiredCapabilities} -- Capabilities for browser
                (default: {None})

        Returns:
            [WebDriver.Ie] -- WebDriver opened and ready to be used
        """
        if driver_path is None:
            driver_path = self.curr_driver_path
        if capabilities is None:
            capabilities = self.curr_caps
        return WebDriver.Ie(
            executable_path=driver_path,
            capabilities=capabilities)

    def get_driver_edge(self, driver_path=None, capabilities=None):
        """Open WebDriver selenium based on Edge browser

        Keyword Arguments:
            driver_path {str} -- Path for driver binary path
                (default: {None})
            capabilities {DesiredCapabilities} -- Capabilities for browser
                (default: {None})
            options {Options} -- Options for browser (default: {None})

        Returns:
            [WebDriver.Edge] -- WebDriver opened and ready to be used
        """
        if driver_path is None:
            driver_path = self.curr_driver_path
        if capabilities is None:
            capabilities = self.curr_caps
        return WebDriver.Edge(
            executable_path=driver_path,
            capabilities=capabilities)

    def get_driver_opera(self, driver_path=None, capabilities=None,
                         options=None):
        """Open WebDriver selenium based on Opera browser

        Keyword Arguments:
            driver_path {str} -- Path for driver binary path
                (default: {None})
            capabilities {DesiredCapabilities} -- Capabilities for browser
                (default: {None})
            options {Options} -- Options for browser (default: {None})

        Returns:
            [WebDriver.Opera] -- WebDriver opened and ready to be used
        """
        if driver_path is None:
            driver_path = self.curr_driver_path
        if capabilities is None:
            capabilities = self.curr_caps
        if options is None:
            options = self.curr_options
        return WebDriver.Opera(
            executable_path=driver_path,
            capabilities=capabilities)

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
        try:
            self.curr_driver = {
                "chrome": self.get_driver_chrome(),
                "firefox": self.get_driver_firefox(),
                "iexplorer": self.get_driver_iexplorer(),
                "edge": self.get_driver_edge(),
                "opera": self.get_driver_opera(),
            }[browser_name]
        except KeyError:
            raise CoreException(
                message=("config file error, SECTION=bot, KEY=browser isn't "
                         "valid value: {}".format(browser_name)),
                log=self.log)
        self.log.info('Started browser with mode : REMOTE OK')

    def mode_remote(self, browser_name='chrome'):
        """Open new brower on remote mode

        Raises:
            CoreException -- browser name is not in valid values list
        """
        url_hub = self.settings.get('url_hub')
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
