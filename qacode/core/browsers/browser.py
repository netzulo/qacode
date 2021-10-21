# -*- coding: utf-8 -*-
"""TODO"""


import os
import sys
from qacode.core.browsers.browser_config import BrowserConfig
from qacode.core.browsers.modules.commons import ModuleCommons
from qacode.core.browsers.modules.elements import ModuleElements
from qacode.core.browsers.modules.js import ModuleJs
from qacode.core.browsers.modules.screenshots import ModuleScreenshots
from qacode.core.browsers.modules.waits import ModuleWaits
from qacode.core.exceptions.browser_error import BrowserError
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver import (Chrome, Edge, Firefox, Ie)
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser(object):
    """TODO: doc class"""

    def __init__(self, log, **kwargs):
        """TODO: doc method"""
        self._log = log
        self._config = BrowserConfig(**kwargs)
        self._capabilities = self.__capabilities__()
        self._options = self.__options__()
        self._driver_abs_path = self.__driver_abs_path__()
        self._driver = None

    def __capabilities__(self):
        """TODO: doc method"""
        capabilities = None
        try:
            capabilities = {
                "chrome": DesiredCapabilities.CHROME.copy(),
                "firefox": DesiredCapabilities.FIREFOX.copy(),
                "iexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
                "edge": DesiredCapabilities.EDGE.copy(),
            }[self._config.browser]
        except KeyError:
            raise BrowserError('Bad browser selected at load options', self)
        return capabilities

    def __driver_abs_path__(self):
        """TODO: doc method"""
        driver_path = "{}/{}".format(
            self._config.driver_path, self._config.driver_name)
        abs_path = os.path.abspath(driver_path)
        sys.path.append(abs_path)
        return abs_path

    def __options__(self):
        """TODO: doc method"""
        is_headless = self._config.options.get("headless")
        try:
            options = {
                "chrome": ChromeOptions(),
                "firefox": FirefoxOptions(),
            }[self._config.browser]
            if is_headless:
                options.add_argument("--headless")
            return options
        except KeyError:
            # this browser hasn't options
            return None

    def __driver_local__(self):
        """TODO: doc method"""
        driver = None
        try:
            driver = {
                "chrome": Chrome,
                "firefox": Firefox,
                "iexplorer": Ie,
                "edge": Edge
            }[self._config.browser]
        except KeyError:
            msg = ("Just browser names allowed: "
                   "chrome, firefox, iexplorer, edge")
            raise Exception(msg)
        return driver

    def __driver_remote__(self):
        """TODO: doc method"""
        return RemoteWebDriver

    def __open_local__(self):
        """TODO: doc method"""
        driver_class = self.__driver_local__()
        try:
            driver = driver_class(
                executable_path=self.driver_abs_path,
                capabilities=self.capabilities,
                options=self.options)
            return driver
        except (AttributeError) as err:
            raise Exception(str(err))

    def __open_remote__(self):
        """TODO: doc method"""
        driver_class = self.__driver_remote__()
        try:
            driver = driver_class(
                command_executor=self._config.hub_url,
                desired_capabilities=self.capabilities,
                options=self.options)
            return driver
        except (AttributeError, SessionNotCreatedException) as err:
            if err.args[0] == "'NoneType' object has no attribute 'execute'":
                raise Exception(
                    "Check if hub it's running at: {}".format(
                        self._config.hub_url))
            raise Exception(str(err))

    def __drivers_selenium__(self):
        """TODO: doc method"""
        self._driver_wait = WebDriverWait(self._driver, 10)
        self._driver_actions = ActionChains(self._driver)
        self._driver_touch = TouchActions(self._driver)

    def open(self):
        """TODO: doc method"""
        if self._config.mode == "local":
            self._driver = self.__open_local__()
        elif self._config.mode == "remote":
            self._driver = self.__open_remote__()
        else:
            raise BrowserError("Just allowed modes: local, remote", self)
        self.__drivers_selenium__()
        # modules
        self.commons = ModuleCommons(self._driver)
        self.elements = ModuleElements(self._driver)
        self.waits = ModuleWaits(self.driver, self._driver_wait)
        self.screenshots = ModuleScreenshots(self._driver)
        self.js = ModuleJs(self.driver)

    def close(self):
        """TODO: doc method"""
        self.driver.quit()
        self._driver = None
        self._driver_wait = None
        self._driver_actions = None
        self._driver_touch = None
        self.commons = None
        self.elements = None
        self.waits = None
        self.screenshots = None
        self.js = None

    @property
    def config(self):
        """TODO: doc method"""
        return self._config

    @property
    def capabilities(self):
        """TODO: doc method"""
        return self.__capabilities__()

    @property
    def options(self):
        """TODO: doc method"""
        return self.__options__()

    @property
    def driver_abs_path(self):
        """TODO: doc method"""
        return self.__driver_abs_path__()

    @property
    def driver(self):
        """TODO: doc method"""
        return self._driver

    @property
    def session_id(self):
        """TODO: doc method"""
        return self._driver.session_id

    @property
    def log(self):
        """TODO: doc method"""
        return self._log