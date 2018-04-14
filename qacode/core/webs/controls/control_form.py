# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import StrictRule
from qacode.core.webs.strict_rules import StrictSeverity
from qacode.core.webs.strict_rules import StrictType


class ControlForm(ControlBase):
    """Requirements: #63"""

    # Settings properties
    on_instance_strict = None
    strict_rules = None
    # Strict properties
    strict_tags = None
    strict_attrs = None
    strict_css_props = None

    # TODO: follow instructions on #63
    def __init__(self, bot, **kwargs):
        """Instance of ControlForm"""
        super(ControlForm, self).__init__(bot, **kwargs)
        self._load(**kwargs)

    def _load(self, **kwargs):
        """Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        self.settings = {
            "selector": kwargs.get('selector'),
            "name": kwargs.get('name'),
            "locator": kwargs.get('locator'),
            "on_instance_search": kwargs.get('on_instance_search'),
            "on_instance_load": kwargs.get('on_instance_load'),
            "on_instance_strict": kwargs.get('on_instance_strict'),
            "strict_rules": kwargs.get('strict_rules')
        }
        # needed for self._load_* functions
        self.load_settings_keys(self.settings)
        # instance logic
        self._load_search(enabled=self.on_instance_search)
        self._load_properties(enabled=self.on_instance_load)
        self._load_strict(enabled=self.on_instance_strict)

    def load_settings_keys(self, settings):
        """Load default setting for ControlForm instance"""
        self.bot.log.debug(
            "control_form | load_settings_keys: loading keys...")
        for key in self.settings.keys():
            value = self.settings.get(key)
            if not value:
                # Optional params
                if key == 'on_instance_strict':
                    value = False
                elif key == 'strict_rules':
                    value = list()
                else:
                    raise ControlException(
                        message=("Bad settings: "
                                 "key={}, value={}").format(
                                     key, value))
            setattr(self, key, value)
        self.bot.log.debug("control_form | load_settings_keys: loaded keys!")

    def _load_strict(self, enabled=False):
        if not enabled:
            self.bot.log.debug(
                ("control | _load_strict: "
                 "!Disabled loading StrictRules!"))
            return False
        typed_rules = list()
        for strict_rule_config in self.settings.get('strict_rules'):
            strict_tag = HtmlTag(strict_rule_config.get('tag'))
            strict_type = StrictType(strict_rule_config.get('type'))
            strict_severity = StrictSeverity(
                strict_rule_config.get('severity', d=100))
            rule = StrictRule(strict_tag, strict_type, strict_severity)
            typed_rules.append(rule)
        self.strict_rules = typed_rules
        self.strict_tags = []
        self.strict_attrs = []
        self.strict_css_props = []
        self._add_rules(self.strict_rules)
        if not self.is_strict_tags() and self.strict_mode:
            raise ControlException(
                message=("Tag obtained for this element html tag not in "
                         "strict_tags list"))
        if not self.is_strict_attrs() and self.strict_mode:
            raise ControlException(
                message=("Html attribute obtained for this element not in "
                         "strict_attrs list"))
        if not self.is_strict_css_props() and self.strict_mode:
            raise ControlException(
                message=("Css property obtained for this element not in "
                         "strict_css_props list"))
        return True

    def _add_rules(self, strict_rules):
        """Validate strict rules for each type

        Arguments:
            strict_rules {StrictRule} -- strict_rule
            strict_mode {bool} -- if enabled, load values for future checks
        """
        # validate rules and add object to respective lists
        for strict_rule in strict_rules:
            if strict_rule.strict_type == StrictType.TAG:
                self.strict_tags.append(strict_rule.enum_type)
            elif strict_rule.strict_type == StrictType.HTML_ATTR:
                self.strict_attrs.append(strict_rule.enum_type)
            elif strict_rule.strict_type == StrictType.CSS_PROP:
                self.strict_css_props.append(strict_rule.enum_type)
            elif strict_rule.strict_type == StrictType.JS_EVENT:
                raise NotImplementedError(
                    "Open an issue on github if raise here")
            elif strict_rule.strict_type == StrictType.BEHAVIOUR:
                raise NotImplementedError(
                    "Open an issue on github if raise here")
            elif strict_rule.strict_type == StrictType.USABILITY:
                raise NotImplementedError(
                    "Open an issue on github if raise here")
            elif strict_rule.strict_type == StrictType.SEO:
                raise NotImplementedError(
                    "Open an issue on github if raise here")
            else:
                raise ControlException(
                    message="bad param 'strict_type', invalid value")

    def is_strict_tags(self, strict_tags=None):
        """Validate if element.tag is in list of strict_tags

        Keyword Arguments:
            strict_tags {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        if strict_tags is None:
            strict_tags = self.strict_tags
        # empty list doesn't to be checked
        if len(strict_tags) == 0:
            return True
        for strict_tag in strict_tags:
            if self.tag == strict_tag.name:
                return True
        return False

    def is_strict_attrs(self, strict_attrs=None):
        """Validate if element.attrs is in list of strict_attrs

        Keyword Arguments:
            strict_attrs {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        attrs_search = []
        attrs_found = []
        if strict_attrs is None:
            strict_attrs = self.strict_attrs
        # empty list doesn't to be checked
        if len(strict_attrs) == 0:
            return True
        for strict_attr in strict_attrs:
            try:
                attr_name = self.get_attr_value(strict_attr.value)
            except ControlException:
                if self.strict_mode:
                    return False
            attrs_search.append(attr_name)
            if attr_name:
                attrs_found.append(attr_name)
        return bool(set(attrs_search).intersection(attrs_found))

    def is_strict_css_props(self, strict_css_props=None):
        """Validate if element.attrs is in list of strict_attrs

        Keyword Arguments:
            strict_attrs {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        css_search = []
        css_found = []
        if strict_css_props is None:
            strict_css_props = self.strict_css_props
        # empty list doesn't to be checked
        if len(strict_css_props) == 0:
            return True
        for strict_css_prop in strict_css_props:
            css_prop = self.get_css_value(strict_css_prop.value)
            css_search.append(css_prop)
            if css_prop:
                css_found.append(css_prop)
        return len(css_search) == len(css_found)
