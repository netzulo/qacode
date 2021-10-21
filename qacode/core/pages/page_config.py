# -*- coding: utf-8 -*-
"""TODO"""


class PageConfig(object):
    """TODO: doc class"""

    def __init__(self, **kwargs):
        """TODO: doc method"""
        self._config = kwargs

    @property
    def name(self):
        """TODO: doc method"""
        return self._config.get("name")

    @property
    def url(self):
        """TODO: doc method"""
        return self._config.get("url")
