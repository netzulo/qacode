# -*- coding: utf-8 -*-
"""TODO"""


from selenium.webdriver.common.by import By


class ControlConfig(object):
    """TODO: doc class"""

    def __init__(self, **kwargs):
        """TODO: doc method"""
        self._config = kwargs

    @property
    def name(self):
        """TODO: doc method"""
        return self._config.get("name")

    @property
    def selector(self):
        """TODO: doc method"""
        return self._config.get("selector")

    @property
    def locator(self):
        """TODO: doc method"""
        return self._config.get("locator") or By.CSS_SELECTOR

    @property
    def search(self):
        """TODO: doc method"""
        return self._config.get("search") or False

    @property
    def pages(self):
        """TODO: doc method"""
        return self._config.get("pages") or []
