# -*- coding: utf-8 -*-
"""TODO"""


class BrowserConfig(object):
    """TODO: doc class"""

    def __init__(self, **kwargs):
        """TODO: doc method"""
        self._config = kwargs

    @property
    def browser(self):
        return self._config.get("browser")

    @property
    def mode(self):
        return self._config.get("mode")

    @property
    def options(self):
        return self._config.get("options")

    @property
    def driver_path(self):
        return self._config.get("driver_path")

    @property
    def driver_name(self):
        return self._config.get("driver_name")
