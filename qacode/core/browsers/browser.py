# -*- coding: utf-8 -*-
"""TODO"""


import os
import sys
from qacode.core.browsers.browser_config import BrowserConfig
from qacode.core.exceptions.core_exception import CoreException
# from qacode.core.loggers.log import Log
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
        self._config = self.__config__(kwargs)
        self._capabilities = self.__capabilities__()
        self._options = self.__options__()
        self._driver_abs_path = self.__driver_abs_path__()
        self._driver = None

    def __config__(self, config):
        """TODO: doc method"""
        if config is None:
            raise Exception("Can't create browser without configuration")
        if isinstance(config, BrowserConfig):
            return config
        elif isinstance(config, dict):
            return BrowserConfig(**config)
        else:
            raise Exception("Just accepted types: dict, BrowserConfig")

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
            msg = 'Bad browser selected at load options'
            raise CoreException(msg, log=self._log)
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

    def __drivers_modules__(self):
        """TODO: doc method"""
        self._modules = {}

    def open(self):
        """TODO: doc method"""
        if self._config.mode == "local":
            self._driver = self.__open_local__()
        elif self._config.mode == "remote":
            self._driver = self.__open_remote__()
        else:
            raise Exception("Just allowed modes: local, remote")
        self.__drivers_selenium__()
        self.__drivers_modules__()

    def close(self):
        """TODO: doc method"""
        self.driver.quit()
        self._driver = None
        self._driver_wait = None
        self._driver_actions = None
        self._driver_touch = None
        self._modules = None

    @property
    def config(self):
        """TODO: doc method"""
        return self._config

    @config.setter
    def config(self, value):
        """TODO: doc method"""
        self._config = self.__config__(value)

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
    def modules(self):
        """TODO: doc method"""
        return self._modules

    @property
    def session_id(self):
        """TODO: doc method"""
        return self._driver.session_id
