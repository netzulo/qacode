# -*- coding: utf-8 -*-
"""TODO"""


class BotConfig(object):
    """TODO: doc class"""

    def __init__(self, **kwargs):
        """TODO: doc method
            Note1: musn't check win/lin 32/64, use must now
        """
        self._log = kwargs.get("log")
        self._bot = kwargs.get("bot")
        # self._testlink = kwargs.get("testlink")

    @property
    def log_name(self):
        """TODO: doc method"""
        return self._log.get("name")

    @property
    def log_path(self):
        """TODO: doc method"""
        return self._log.get("path")

    @property
    def log_level(self):
        """TODO: doc method"""
        return self._log.get("level")

    @property
    def drivers_path(self):
        """TODO: doc method"""
        return self._bot.get("drivers_path")

    @property
    def drivers_names(self):
        """TODO: doc method"""
        return self._bot.get("drivers_names")

    @property
    def browsers(self):
        """TODO: doc method"""
        return self._bot.get("browsers")

    @property
    def pages(self):
        """TODO: doc method"""
        return self._bot.get("pages")

    @property
    def controls(self):
        """TODO: doc method"""
        return self._bot.get("controls")

    @property
    def hub_url(self):
        """TODO: doc method"""
        return self._bot.get("hub_url")
