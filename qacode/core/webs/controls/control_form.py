# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers import logger_messages
from qacode.core.webs.controls.control_base import By
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import StrictRule
from qacode.core.webs.strict_rules import StrictSeverity
from qacode.core.webs.strict_rules import StrictType
from selenium.webdriver.support.ui import Select


MSG = logger_messages


class ControlForm(ControlBase):
    """Requirements: #63"""

    # Strict properties
    strict_tag = None
    # tag=select
    dropdown = None

    def __init__(self, bot, **kwargs):
        """Instance of ControlForm"""
        super(ControlForm, self).__init__(bot, **kwargs)
        self.__load__(**kwargs)

    def __load__(self, **kwargs):
        """Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        # needed for self._load_* functions
        self.load_settings_keys(kwargs.copy(), update=True)
        # instance logic
        self._load_search(
            enabled=self.on_instance_search,
            element=self.settings.get("element"))
        self._load_properties(enabled=self.on_instance_load)
        # at least 1 rule to enable this feature
        self.__load__rules__(enabled=len(self.strict_rules))

    def load_settings_keys(self, settings, update=False):
        """Load default setting for ControlForm instance"""
        super(ControlForm, self).load_settings_keys(
            settings,
            update=update,
            default_keys=[
                ("selector", None),  # required
                ("name", "UNNAMED"),
                ("locator", By.CSS_SELECTOR),
                ("on_instance_search", False),
                ("on_instance_load", False),
                ("auto_reload", True),
                ("instance", 'ControlForm'),
                ("strict_rules", []),
            ]
        )

    def __load__rules__(self, enabled=False):
        """Validate strict rules for each type of StricRule"""
        self.bot.log.debug(MSG.CF_PARSERULES_LOADING)
        if not enabled:
            self.warning(MSG.CF_STRICT_DISABLED)
            return False
        typed_rules = list()
        # parsing rules > to enums > to instance
        for strict_cfg in self.strict_rules:
            cfg = {
                "tag": strict_cfg.get('tag'),
                "type": strict_cfg.get('type'),
                "severity": strict_cfg.get('severity')
            }
            if cfg.get('severity') is None:
                cfg.update({"severity": "low"})
            typed_rules.append(
                StrictRule(
                    HtmlTag(cfg.get('tag')),
                    StrictType(cfg.get('type')),
                    StrictSeverity(cfg.get('severity'))))
        # parsed rules at this point
        self.bot.log.debug(MSG.CF_PARSERULES_LOADED)
        # not implemented list
        not_implemented_types = [
            StrictType.HTML_ATTR,
            StrictType.CSS_PROP,
            StrictType.JS_EVENT,
            StrictType.BEHAVIOUR,
            StrictType.USABILITY,
            StrictType.SEO
        ]
        # validate rules and apply it
        for strict_rule in typed_rules:
            if strict_rule.strict_type in not_implemented_types:
                raise NotImplementedError(MSG.CF_NOT_IMPLEMENTED_TYPES)
            if strict_rule.strict_type == StrictType.TAG:
                self.__load_strict_tag__(strict_rule.enum_type)
            else:
                raise ControlException(
                    message="bad param 'strict_type', invalid value")

    def __load_strict_tag__(self, strict_tag):
        """Validate if element.tag is in list of strict_tags and
            instance ControlForm specific properties
        """
        self.strict_tag = strict_tag
        valid_tags = ['select']
        self.bot.log.debug(MSG.CF_STRICTTAG_LOADING)
        if self.strict_tag.value not in valid_tags:
            raise ControlException(
                msg="This tag can be loaded as strict_rule")
        if self.tag == valid_tags[0]:
            self.dropdown = Select(self.element)
            self.bot.log.debug(MSG.CF_DROPDOWN_LOADED)
        self.bot.log.debug(MSG.CF_STRICTTAG_LOADED)
        return True

    def __check_reload__form__(self):
        """Allow to check before methods calls to ensure
            if it's neccessary reload element properties
        """
        if (not self.element or not self.dropdown) and self.auto_reload:
            self.reload(**self.settings)

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        # load settings again
        if kwargs:
            config = kwargs.copy()
        else:
            config = self.settings.copy()
        config.update(self.RELOAD_CONFIG)
        # needed for self._load_* functions
        self.load_settings_keys(config, update=True)
        # instance logic
        self._load_search(
            enabled=self.on_instance_search,
            element=self.element)
        self._load_properties(enabled=self.on_instance_load)
        # at least 1 rule to enable this feature
        self.__load__rules__(enabled=len(kwargs.get("strict_rules")))
        self.bot.log.debug(MSG.CF_RELOAD_LOADED)

    def dropdown_select(self, text, by_value=False, by_index=False):
        """The Select class only works with tags which have select tags.
            Using the Index of Dropdown (int)
            Using the Value of Dropdown (str)
            Using the Text of Dropdown (str)

        Arguments:
            text {str|int} -- Probably the easiest way of doing it. You
                have to match the text which is displayed in the drop down.

        Keyword Arguments:
            by_value {bool} -- We can use to select an option using the
                value attribute. (default: {False})
            by_index {bool} -- We can use to select an option using the
                index attribute. (default: {False})

        Raises:
            ControlException -- if tag is not 'select'
            ControlException -- if all flags are 'True'
        """
        self.bot.log.debug(MSG.CF_DROPDOWNSELECT_LOADING)
        self.__check_reload__form__()
        if self.dropdown is None:
            raise ControlException(
                msg="Element must be dropdown, tag={})".format(self.tag))
        if by_value and by_index:
            raise ControlException(
                msg="Can't use this function with all flags with True values")
        if by_value:
            self.dropdown.select_by_value(text)
        elif by_index:
            if not isinstance(text, int):
                raise ControlException(msg="index must be an int value")
            self.dropdown.select_by_index(int(text))
        else:
            self.dropdown.select_by_visible_text(text)
        self.bot.log.debug(MSG.CF_DROPDOWNSELECT_LOADED)

    def dropdown_deselect(self, text, by_value=False, by_index=False):
        """The Select class only works with tags which have select tags.
            Using the Index of Dropdown (int)
            Using the Value of Dropdown (str)
            Using the Text of Dropdown (str)

        Arguments:
            text {str|int} -- Probably the easiest way of doing it. You
                have to match the text which is displayed in the drop down.

        Keyword Arguments:
            by_value {bool} -- We can use to select an option using the
                value attribute. (default: {False})
            by_index {bool} -- We can use to select an option using the
                index attribute. (default: {False})

        Raises:
            ControlException -- if tag is not 'select'
            ControlException -- if all flags are 'True'
        """
        self.bot.log.debug(MSG.CF_DROPDOWNDESELECT_LOADING)
        self.__check_reload__form__()
        if self.dropdown is None:
            raise ControlException(
                msg="Element must be dropdown, tag={}".format(self.tag))
        if by_value and by_index:
            raise ControlException(
                msg="Can't use this function with all flags with True values")
        if by_value:
            self.dropdown.deselect_by_value(text)
        elif by_index:
            if not isinstance(text, int):
                raise ControlException(msg="index must be an int value")
            self.dropdown.deselect_by_index(int(text))
        else:
            self.dropdown.deselect_by_visible_text(text)
        self.bot.log.debug(MSG.CF_DROPDOWNDESELECT_LOADED)

    def dropdown_deselect_all(self):
        """The Select class only works with tags which have select
            tags with multiple="multiple" attribute.

        Raises:
            ControlException -- if tag is not 'select'
        """
        self.bot.log.debug(MSG.CF_DROPDOWNDESELECTALL_LOADING)
        self.__check_reload__form__()
        if self.dropdown is None:
            msg = "Element must be dropdown"" (tag={})".format(self.tag)
            raise ControlException(msg=msg)
        self.dropdown.deselect_all()
        self.bot.log.debug(MSG.CF_DROPDOWNDESELECTALL_LOADED)

    def __repr__(self):
        """Show basic properties for this object"""
        return super(ControlForm, self).__repr__()
