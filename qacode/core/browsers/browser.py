# -*- coding: utf-8 -*-
"""TODO"""


import os
import sys
from qacode.core.browsers.browser_config import BrowserConfig
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers.log import Log
from selenium.webdriver import DesiredCapabilities


class Browser(object):
    """TODO: doc class"""

    def __init__(self, log, **kwargs):
        """TODO: doc method"""
        self._log = log
        self._config = self.__config__(kwargs)
        self._driver = None
        self._capabilities = self.__capabilities__()
        self._driver_abs_path = self.__driver_abs_path__()

    def __config__(self, config):
        """TODO: doc method"""
        _config = None
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

    def open(self):
        """TODO: doc method"""
        # based on mode use or not drivers path
        # get capabilities
        # bassed on browser get options or not
        # others webdrivers ?
        raise NotImplementedError("WIP code")

    def close(self):
        """TODO: doc method"""
        # try to call selenium driver.quit
        # try to call selenium driver.close
        raise NotImplementedError("WIP code")

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
    def driver_abs_path(self):
        """TODO: doc method"""
        return self.__driver_abs_path__()

    @property
    def session_id(self):
        """TODO: doc method"""
        return self._driver.session_id
