# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_group"""


from qacode.core.webs.controls.control_base import By
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_base import CoreException


class ControlGroup(ControlBase):
    """Requirements: #164"""

    # Log messages
    CG_SETTINGS_LOADING = "control_group | load_settings_keys: loading keys..."
    CG_SETTINGS_LOADED = "control_group | load_settings_keys: loaded keys!"
    CG_GROUP_DISABLED = ("control | _load_group: "
                         "!Disabled searching group of elements!")
    CG_GROUP_LOADING = ("control | _load_group: "
                        "searching group of elements...")
    CG_GROUP_WAITING = "control | _load_group: waiting for elements..."
    CG_GROUP_LOADED = "control | _load_group: elements found!"
    # Settings properties
    on_instance_group = None
    group = None
    # Element properties
    elements = None

    def __init__(self, bot, **kwargs):
        """Instance of ControlGroup"""
        super(ControlGroup, self).__init__(bot, **kwargs)
        self.load(**kwargs)
        # TODO: make sense

    def load(self, **kwargs):
        """Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        self.elements = []
        self.group = []
        # needed for self._load_* functions
        self.load_settings_keys(kwargs.copy(), update=True)
        # instance logic
        if not self.on_instance_group:
            self._load_search(enabled=self.on_instance_search)
            self._load_properties(enabled=self.on_instance_load)
        else:
            self._load_group(enabled=self.on_instance_group)
            self._load_properties(enabled=self.on_instance_load)

    def load_settings_keys(self, settings, update=False):
        """Load default setting for ControlGroup instance"""
        self.bot.log.debug(self.CG_SETTINGS_LOADING)
        super(ControlGroup, self).load_settings_keys(
            settings,
            update=update,
            default_keys=[
                ("selector", None),  # required
                ("name", "UNNAMED"),
                ("locator", By.CSS_SELECTOR),
                ("on_instance_search", False),
                ("on_instance_load", False),
                ("auto_reload", True),
                ("instance", 'ControlGroup'),
                ("on_instance_group", False),
                ("group", []),
            ]
        )
        self.bot.log.debug(self.CG_SETTINGS_LOADED)

    def _load_group(self, enabled=False, ):
        """Load default properties for each element at group dict

        Keyword Arguments:
            enabled {bool} -- load at enabled (default: {False})
        """
        if not enabled or enabled is None:
            self.bot.log.debug(self.CG_GROUP_DISABLED)
            return False
        self.bot.log.debug(self.CG_GROUP_LOADING)
        try:
            self.elements = self.bot.navigation.find_elements(
                self.selector, locator=self.locator)
        except CoreException:
            self.bot.log.warning(self.CG_GROUP_WAITING)
            self.elements = self.bot.navigation.find_elements_wait(
                self.selector, locator=self.locator)
        self.bot.log.debug(self.CG_GROUP_LOADED)
        return True
