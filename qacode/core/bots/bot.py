# -*- coding: utf-8 -*-
"""TODO"""


from qacode.core.bots.bot_config import BotConfig
from qacode.core.browsers.browser import Browser
from qacode.core.loggers.log import Log


class Bot(object):
    """Class Base for handle selenium functionality throught this wrapper"""

    def __init__(self, **kwargs):
        """TODO: doc method"""
        self._browsers = []
        self._pages = []
        self._controls = []
        self._config = self.__config__(kwargs)
        self._log = Log(**{
            "name": self._config.log_name,
            "path": self._config.log_path,
            "level": self._config.log_level})

    def __config__(self, config):
        """TODO: doc method"""
        _config = None
        if config is None:
            raise Exception("Can't create browser without configuration")
        if isinstance(config, BotConfig):
            return config
        elif isinstance(config, dict):
            return BotConfig(**config)
        else:
            raise Exception("Just accepted types: dict, BotConfig")

    def browser(self, session_id):
        """TODO: doc method"""
        for browser in self.browsers:
            if browser.session_id == session_id:
                return browser
        raise Exception("browser not found")

    def page(self, url):
        """TODO: doc method"""
        for page in self.pages:
            if page.url == url:
                return page
        raise Exception("page not found")

    def control(self, selector):
        """TODO: doc method"""
        for control in self.controls:
            if control.selector == selector:
                return control
        raise Exception("control not found")

    def browser_create(self, config):
        """TODO: doc method"""
        driver_name = self._config.drivers_names[config.get("browser")]
        driver_path = self._config.drivers_path
        _config = config.copy()
        _config.update({
            "driver_path": driver_path,
            "driver_name": driver_name,
            "hub_url": self._config.hub_url})
        browser = Browser(self.log, **_config)
        self._browsers.append(browser)
        return browser

    @property
    def config(self):
        """TODO: doc method"""
        return self._config

    @config.setter
    def config(self, value):
        """TODO: doc method"""
        self._config = self.__config__(value)


    @property
    def browsers(self):
        """TODO: doc method"""
        return self._browsers

    @browsers.setter
    def browsers(self, value):
        """TODO: doc method"""
        self._browsers = value
    
    @property
    def pages(self):
        """TODO: doc method"""
        return self._pages

    @pages.setter
    def pages(self, value):
        """TODO: doc method"""
        self._pages = value
    
    @property
    def controls(self):
        """TODO: doc method"""
        return self._controls

    @controls.setter
    def controls(self, value):
        """TODO: doc method"""
        self._controls = value

    @property
    def log(self):
        """TODO: doc method"""
        return self._log