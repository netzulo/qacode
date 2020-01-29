# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers import logger_messages as MSG
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import (
    StrictRule, StrictSeverity, StrictType)


class ControlForm(ControlBase):
    """This class allow to reference remote NodeElement (JS) or Html Tag to
        use checks , obtain information or handle actions using this instance.
        Wrapper for Selenium class named 'WebElement' using wrapper of
        WebDriver named qacode.core.bots.BotBase
        This class inherit of ControlBase and add functionality to ensure
        tag names, html attributes, css properties values and element behaviour
        at instance based on configuration

    Arguments:
        object {ControlBase} -- qacode wrapper for WebElement from Selenium
    """

    def __init__(self, bot, **kwargs):
        """Initialize an instance of ControlForm

        Arguments:
            bot {BotBase} -- BotBase instance
        """
        super(ControlForm, self).__init__(bot, **kwargs)
        # instance minimal data
        self._rules = kwargs.get("rules") or []

    def __load__(self, **kwargs):
        """Allow to instance settings obtaining from super
            and applying self instance behaviour
        """
        super(ControlForm, self).__load__(**kwargs)
        if self._on_instance_search:
            self.bot.log.debug(MSG.CF_RULES_LOADING)
            self.__rules_apply__(rules=self._rules)

    def __settings_parse__(self, **kwargs):
        """Allow to parse settings obtaining from super
            and applying self instance behaviour
        """
        settings = super(ControlForm, self).__settings_parse__(**kwargs)
        _rules = kwargs.get("rules") or []
        # at least 1 rule to enable this feature
        if not isinstance(_rules, list) or not bool(_rules):
            _rules = list()
        self._rules = self.__rules_parse__(rules=_rules)
        settings.update({"rules": self._rules})
        return settings

    def __rules_parse__(self, rules=[]):
        """Validate rules for each type of StricRule"""
        self.bot.log.debug(MSG.CF_RULES_PARSING)
        if not bool(rules):
            self.bot.log.debug(MSG.CF_RULES_DISABLED)
            return []
        typed_rules = list()
        # parsing rules > to enums > to instance
        for _rule in rules:
            self.bot.log.debug(MSG.CF_RULES_PARSING)
            rule = None
            if isinstance(_rule, StrictRule):
                rule = _rule
            else:
                _tag = HtmlTag(_rule.get('tag'))
                _type = StrictType(_rule.get('type'))
                _severity = _rule.get('severity')
                if _severity is None:
                    _severity = StrictSeverity("low")
                else:
                    _severity = StrictSeverity(_severity)
                rule = StrictRule(_tag, _type, _severity)
            typed_rules.append(rule)
            self.bot.log.debug(MSG.CF_RULES_PARSED)
        # parsed rules at this point
        self.bot.log.debug(MSG.CF_RULES_PARSED)
        return typed_rules

    def __rules_apply__(self, rules=[]):
        """Allow to apply rules using self WebElement"""
        self.bot.log.debug(MSG.CF_RULES_APPLYING)
        if not bool(rules):
            self.bot.log.debug(MSG.CF_RULES_DISABLED)
            return False
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
        for rule in rules:
            if rule.strict_type in not_implemented_types:
                raise NotImplementedError(MSG.NOT_IMPLEMENTED)
            if rule.strict_type == StrictType.TAG:
                self.__rules_apply_tag__(rule)
            else:
                msg = MSG.BAD_PARAM.format("strict_type")
                self.bot.log.debug(msg)
                raise ControlException(msg, info_bot=self._info_bot)
        self.bot.log.debug(MSG.CF_RULES_APPLIED)

    def __rules_apply_tag__(self, rule):
        """Apply Tag based on StictType.TAG enum"""
        self.bot.log.debug(MSG.CF_RULES_APPLYING_TAG)
        valid_tags = [HtmlTag.TAG_SELECT.value, HtmlTag.TAG_TABLE.value]
        if not isinstance(rule.enum_type, HtmlTag):
            msg = MSG.BAD_PARAM.format("tag")
            self.bot.log.debug(msg)
            raise ControlException(msg, info_bot=self._info_bot)
        # element must exist to get working this instance
        _tag = HtmlTag(self._tag)
        if rule.enum_type.value not in valid_tags:
            raise ControlException(MSG.CF_BADTAG, info_bot=self._info_bot)
        # Validate at instance
        if _tag != rule.enum_type:
            raise ControlException(
                "ctl | Tag validation Error", info_bot=self._info_bot)
        self.bot.log.debug(MSG.CF_RULES_APPLIED_TAG)

    def __check_reload__(self):
        """Allow to check before methods calls to ensure
            if it's neccessary reload element properties
        """
        super(ControlForm, self).__check_reload__()

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        super(ControlForm, self).reload(**kwargs)

    def __repr__(self):
        """Show basic properties for this object"""
        return super(ControlForm, self).__repr__()

    @property
    def rules(self):
        """GET for rules attribute"""
        return self._rules
