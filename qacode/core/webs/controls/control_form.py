# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers import logger_messages as MSG
from qacode.core.webs.controls.control_base import By
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import (
    StrictRule, StrictSeverity, StrictType)


class ControlForm(ControlBase):
    """Requirements: #63"""

    # Strict properties
    strict_tag = None
    # tag=select
    IS_DROPDOWN = None
    # tag=select
    IS_TABLE = None

    def __init__(self, bot, **kwargs):
        """Instance of ControlForm. Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        super(ControlForm, self).__init__(bot, **kwargs)
        # needed for self._load_* functions
        self.__load_settings_keys__(kwargs.copy(), update=True)
        # instance logic
        self.__load_search__(
            enabled=self.on_instance_search,
            element=self.settings.get("element"))
        if self.on_instance_search:
            # at least 1 rule to enable this feature
            self.__load__rules__(enabled=len(self.strict_rules))

    def __load_settings_keys__(self, settings, update=False):
        """Load default setting for ControlForm instance"""
        settings.update({"strict_rules": settings.get('strict_rules') or []})
        super(ControlForm, self).__load_settings_keys__(
            settings,
            update=update,
            default_keys=[
                ("selector", None),  # required
                ("name", "UNNAMED"),
                ("locator", By.CSS_SELECTOR),
                ("on_instance_search", False),
                ("auto_reload", True),
                ("instance", 'ControlForm'),
                ("strict_rules", []),
            ]
        )

    def __load__rules__(self, enabled=False):
        """Validate strict rules for each type of StricRule"""
        self.bot.log.debug(MSG.CF_PARSERULES_LOADING)
        if not enabled:
            self.bot.log.warning(MSG.CF_STRICT_DISABLED)
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
        self.IS_DROPDOWN = False
        self.IS_TABLE = False
        self.strict_tag = strict_tag
        valid_tags = ['select', 'table']
        self.bot.log.debug(MSG.CF_STRICTTAG_LOADING)
        if self.strict_tag.value not in valid_tags:
            raise ControlException(msg=MSG.CF_BADTAG)
        if self.tag == HtmlTag.TAG_SELECT.value:
            self.IS_DROPDOWN = True
        if self.tag == HtmlTag.TAG_TABLE.value:
            self.IS_TABLE = True
        self.bot.log.debug(MSG.CF_STRICTTAG_LOADED)
        return True

    def __check_reload__form__(self):
        """Allow to check before methods calls to ensure
            if it's neccessary reload element properties
        """
        reload_needed = not self.element and self.auto_reload
        if reload_needed:
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
        config.update({"on_instance_search": True})
        # needed for self._load_* functions
        self.__load_settings_keys__(config, update=True)
        # instance logic
        self.__load_search__(
            enabled=self.on_instance_search,
            element=self.element)
        if self.on_instance_search:
            # at least 1 rule to enable this feature
            self.__load__rules__(enabled=len(kwargs.get("strict_rules")))
        self.bot.log.debug(MSG.CF_RELOAD_LOADED)

    def __repr__(self):
        """Show basic properties for this object"""
        return super(ControlForm, self).__repr__()
