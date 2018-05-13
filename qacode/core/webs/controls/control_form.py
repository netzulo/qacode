# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import StrictRule
from qacode.core.webs.strict_rules import StrictSeverity
from qacode.core.webs.strict_rules import StrictType
from selenium.webdriver.support.ui import Select


class ControlForm(ControlBase):
    """Requirements: #63"""

    # Settings properties
    on_instance_strict = None
    strict_rules = None
    strict_rules_typed = None
    # Strict properties
    strict_tags = None
    strict_attrs = None
    strict_css_props = None
    # Tags: select
    dropdown = None

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
            "auto_reload": kwargs.get('auto_reload'),
            "on_instance_strict": kwargs.get('on_instance_strict'),
            "strict_rules": kwargs.get('strict_rules')
        }
        # needed for self._load_* functions
        self.load_settings_keys(self.settings)
        # needed for self._load_strict function
        self.strict_rules_typed = []
        self.strict_tags = []
        self.strict_attrs = []
        self.strict_css_props = []
        # instance logic
        self._load_search(enabled=self.on_instance_search)
        self._load_properties(enabled=self.on_instance_load)
        self._load_strict(enabled=self.on_instance_strict)

    def load_settings_keys(self, settings, update=False):
        """Load default setting for ControlForm instance"""
        self.bot.log.debug(
            "control_form | load_settings_keys: loading keys...")
        # Update instance settings
        if update:
            self.settings = settings
        for key in settings.keys():
            value = settings.get(key)
            if not value:
                # Optional params
                if key == 'name':
                    value = "UNNAMED"
                elif key == 'locator':
                    value = 'css selector'
                elif key == 'on_instance_search':
                    value = False
                elif key == 'on_instance_load':
                    value = False
                elif key == 'auto_reload':
                    value = True
                elif key == 'on_instance_strict':
                    value = False
                elif key == 'strict_rules':
                    value = []
                else:
                    raise ControlException(
                        message=("Bad settings: "
                                 "key={}, value={}").format(
                                     key, value))
            setattr(self, key, value)
        self.bot.log.debug("control_form | load_settings_keys: loaded keys!")

    def _load_strict(self, enabled=False):
        """Load default setting for ControlForm instance"""
        self.bot.log.debug(
            "control_form | _load_strict: loading strict_rules...")
        if not enabled:
            self.bot.log.debug(
                ("control_form | _load_strict: "
                 "!Disabled loading StrictRules!"))
            return False
        # Parse to enums
        typed_rules = self.parse_rules(self.strict_rules)
        self.add_rules(typed_rules, typed=True)
        # Logic for strict_rules here
        self.is_strict_tags = self.load_strict_tags()
        self.is_strict_attrs = self.load_strict_attrs()
        self.is_strict_css_props = self.load_strict_css_props()
        self.bot.log.debug(
            "control_form | _load_strict: loaded strict_rules!")

    def add_rules(self, strict_rules, typed=False):
        """Validate strict rules for each type

        Arguments:
            strict_rules {StrictRule} -- strict_rule
            on_instance_strict {bool} -- if enabled, load values for
                future checks
        """
        if not typed:
            self.bot.log.debug(
                ("control_form | add_rules: "
                 "adding base list of strict_rules..."))
            self.strict_rules.append(strict_rules)
            self.bot.log.debug(
                "control_form | add_rules: added base list of strict_rules!")
            return
        else:
            self.bot.log.debug(
                ("control_form | add_rules: "
                 "adding typed list of strict_rules..."))
            self.strict_rules_typed.extend(strict_rules)
            # validate rules and add object to respective lists
            for strict_rule in self.strict_rules_typed:
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
            self.bot.log.debug(
                "control_form | add_rules: added typed list of strict_rules!")

    def load_strict_tags(self, strict_tags=None):
        """Validate if element.tag is in list of strict_tags and
            instance ControlForm specific properties

            tag=select, instance down 'dropdown' property

        Keyword Arguments:
            strict_tags {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        self.bot.log.debug(
            "control_form | load_strict_tags: loading strict_tags...")
        if strict_tags is None:
            strict_tags = self.strict_tags
        # empty list doesn't to be checked
        if len(strict_tags) == 0:
            return True
        for strict_tag in strict_tags:
            if self.tag == strict_tag.value:
                # specific elements logic
                if self.tag == 'select':
                    self.dropdown = Select(self.element)
                self.bot.log.debug(
                    ("control_form | load_strict_tags: "
                     "loaded strict_tags!"))
                return True
        if self.on_instance_strict:
            self.bot.log.error(
                ("control_form | load_strict_tags: "
                 "not loaded strict_tags with enabled strict_mode!"))
            raise ControlException(
                message=("Validation raises for strict_tags for this element:"
                         "control={}, strict_tags=[{}]").format(
                             self, strict_tags))
        self.bot.log.warning(
            ("control_form | load_strict_tags: "
             "not loaded strict_tags!"))
        return False

    def load_strict_attrs(self, strict_attrs=None):
        """Validate if element.attrs is in list of strict_attrs

        Keyword Arguments:
            strict_attrs {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        self.bot.log.debug(
            "control_form | load_strict_attrs: loading strict_attrs...")
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
                if not self.on_instance_strict:
                    self.bot.log.warning(
                        ("control_form | load_strict_attrs: "
                         "not loaded strict_attrs!"))
                    return False
                self.bot.log.error(
                    ("control_form | load_strict_attrs: "
                     "not loaded strict_attrs with enabled strict_mode!"))
                raise ControlException(
                    message=("Validation raises for strict_attrs "
                             "for this element:"
                             "control={}, strict_attrs=[{}]").format(
                                 self, strict_attrs))
            attrs_search.append(attr_name)
            if attr_name:
                attrs_found.append(attr_name)
        is_attrs = bool(set(attrs_search).intersection(attrs_found))
        if not is_attrs and self.on_instance_strict:
            self.bot.log.error(
                ("control_form | load_strict_attrs: "
                 "not loaded strict_attrs with enabled strict_mode!"))
            raise ControlException(
                message=("Validation raises for strict_attrs "
                         "for this element:"
                         "control={}, strict_attrs=[{}]").format(
                             self, strict_attrs))
        self.bot.log.debug(
            "control_form | load_strict_attrs: loaded strict_attrs!")
        return is_attrs

    def load_strict_css_props(self, strict_css_props=None):
        """Validate if element.attrs is in list of strict_attrs

        Keyword Arguments:
            strict_css_props {[type]} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """
        self.bot.log.debug(
            "control_form | load_strict_css_props: loading strict_attrs...")
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
        is_css = len(css_search) == len(css_found)
        if not is_css and self.on_instance_strict:
            raise ControlException(
                message=("Validation raises for strict_css_props "
                         "for this element:"
                         "control={}, strict_css_props=[{}]").format(
                             self, strict_css_props))
        self.bot.log.debug(
            "control_form | load_strict_css_props: loaded strict_attrs!")
        return is_css

    def parse_rules(self, strict_rules=None):
        """Parse array of configurations dicts of strict_rules to
            instances list of StrictRule
        """
        self.bot.log.debug(
            "control_form | parse_rules: parsing strict_rules...")
        typed_rules = list()
        if strict_rules is None:
            strict_rules = self.settings.get('strict_rules')
        # parsing rules > to enums > to instance
        for strict_rule_config in strict_rules:
            strict_config = {
                "tag": strict_rule_config.get('tag'),
                "type": strict_rule_config.get('type'),
                "severity": strict_rule_config.get('severity')
            }
            if strict_config.get('severity') is None:
                strict_config.update({"severity": "low"})
            strict_tag = HtmlTag(strict_config.get('tag'))
            strict_type = StrictType(strict_config.get('type'))
            strict_severity = StrictSeverity(strict_config.get('severity'))
            rule = StrictRule(strict_tag, strict_type, strict_severity)
            typed_rules.append(rule)
        # parsed rules at this point
        self.bot.log.debug(
            "control_form | parse_rules: parsed strict_rules!")
        return typed_rules

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        self.bot.log.debug(
            "control_form | reload: reloading control...")
        # load settings again
        config = kwargs.copy()
        # needed for self._load_* functions
        self.load_settings_keys(config, update=True)
        # instance logic
        self._load_search(
            enabled=config.get('on_instance_search'))
        self._load_properties(
            enabled=config.get('on_instance_load'))
        self._load_strict(
            enabled=config.get('on_instance_strict'))
        self.bot.log.debug(
            "control_form | reload: reloaded control!")
