# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.webs.controls.control_base import By
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.html_tags import HtmlTag
from qacode.core.webs.strict_rules import StrictRule
from qacode.core.webs.strict_rules import StrictSeverity
from qacode.core.webs.strict_rules import StrictType
from selenium.webdriver.support.ui import Select


class ControlForm(ControlBase):
    """Requirements: #63"""

    # Log messages
    CF_STRICT_LOADING = "control_form | _load_strict: loading strict_rules..."
    CF_STRICT_DISABLED = ("control_form | _load_strict: "
                          "disabled loading StrictRules")
    CF_STRICT_LOADED = "control_form | _load_strict: loaded strict_rules"
    CF_ADDRULES_BASE_ADDING = ("control_form | add_rules: "
                               "adding base list of strict_rules...")
    CF_ADDRULES_BASE_ADDED = ("control_form | add_rules: "
                              "added base list of strict_rules")
    CF_ADDRULES_TYPED_ADDING = ("control_form | add_rules: "
                                "adding typed list of strict_rules...")
    CF_ADDRULES_TYPED_ADDED = ("control_form | add_rules: "
                               "added typed list of strict_rules")
    CF_NOT_IMPLEMENTED_TYPES = "Open an issue on github if raise here"
    CF_STRICTTAGS_LOADING = ("control_form | load_strict_tags: "
                             "loading strict_tags...")
    CF_STRICTTAGS_NOTAGS = "control_form | load_strict_tags: 0 strict_tags"
    CF_STRICTTAGS_LOADED = "control_form | load_strict_tags: loaded"
    CF_STRICTTAGS_ENABLED_ERROR = ("control_form | load_strict_tags: not "
                                   "loaded with enabled strict_mode")
    CF_STRICTTAGS_NOT_LOADED = "control_form | load_strict_tags: not loaded"
    CF_STRICTATTRS_LOADING = ("control_form | load_strict_attrs: "
                              "loading strict_attrs...")
    CF_STRICTATTRS_NOT_LOADED = ("control_form | load_strict_attrs: not loaded"
                                 " strict_attrs")
    CF_STRICTATTRS_ERROR = ("control_form | load_strict_attrs: not loaded "
                            "strict_attrs with enabled strict_mode")
    CF_STRICTATTRS_LOADED = ("control_form | load_strict_attrs: "
                             "loaded strict_attrs")
    CF_STRICTCSS_LOADING = "control_form | load_strict_css_props: loading..."
    CF_STRICTCSS_LOADED = "control_form | load_strict_css_props: loaded"
    CF_STRICTCSS_NOT_LOADED = ("control_form | load_strict_css_props:"
                               " not loaded strict_attrs")
    CF_STRICTCSS_ERROR = ("control_form | load_strict_css_props: not loaded "
                          "strict_css_props with enabled strict_mode")
    CF_PARSERULES_LOADING = "control_form | parse_rules: parsing..."
    CF_PARSERULES_LOADED = "control_form | parse_rules: parsed"
    CF_RELOAD_LOADING = "control_form | reload: reloading control..."
    CF_RELOAD_LOADED = "control_form | reload: reloaded control"
    CF_DROPDOWNSELECT_LOADING = "control_form | dropdown_select: selecting..."
    CF_DROPDOWNSELECT_LOADED = "control_form | dropdown_select: selected"
    CF_DROPDOWNDESELECT_LOADING = ("control_form | dropdown_select:"
                                   " deselecting...")
    CF_DROPDOWNDESELECT_LOADED = "control_form | dropdown_select: deselected"
    CF_DROPDOWNDESELECTALL_LOADING = ("control_form | dropdown_select:"
                                      " deselecting all...")
    CF_DROPDOWNDESELECTALL_LOADED = ("control_form | dropdown_select:"
                                     " deselected all")
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
        # needed for self._load_* functions
        self.load_settings_keys(kwargs.copy())
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
                ("on_instance_strict", False),
                ("strict_rules", []),
            ]
        )

    def _load_strict(self, enabled=False):
        """Load default setting for ControlForm instance"""
        self.bot.log.debug(self.CF_STRICT_LOADING)
        if not enabled:
            self.bot.log.debug(self.CF_STRICT_DISABLED)
            return False
        # Parse to enums
        typed_rules = self.parse_rules(self.strict_rules)
        self.add_rules(typed_rules, typed=True)
        # Logic for strict_rules here
        self.is_strict_tags = self.load_strict_tags()
        self.is_strict_attrs = self.load_strict_attrs()
        self.is_strict_css_props = self.load_strict_css_props()
        self.bot.log.debug(self.CF_STRICT_LOADED)

    def add_rules(self, strict_rules, typed=False):
        """Validate strict rules for each type

        Arguments:
            strict_rules {StrictRule} -- strict_rule
            on_instance_strict {bool} -- if enabled, load values for
                future checks
        """
        if not typed:
            self.bot.log.debug(self.CF_ADDRULES_BASE_LOADING)
            self.strict_rules.append(strict_rules)
            self.bot.log.debug(self.CF_ADDRULES_BASE_ADDED)
            return
        else:
            self.bot.log.debug(self.CF_ADDRULES_TYPED_ADDING)
            self.strict_rules_typed.extend(strict_rules)
            # not implemented list
            not_implemented_types = [
                StrictType.JS_EVENT,
                StrictType.BEHAVIOUR,
                StrictType.USABILITY,
                StrictType.SEO
            ]
            # validate rules and add object to respective lists
            for strict_rule in self.strict_rules_typed:
                if strict_rule.strict_type == StrictType.TAG:
                    self.strict_tags.append(strict_rule.enum_type)
                elif strict_rule.strict_type == StrictType.HTML_ATTR:
                    self.strict_attrs.append(strict_rule.enum_type)
                elif strict_rule.strict_type == StrictType.CSS_PROP:
                    self.strict_css_props.append(strict_rule.enum_type)
                elif strict_rule.strict_type in not_implemented_types:
                    raise NotImplementedError(self.CF_NOT_IMPLEMENTED_TYPES)
                else:
                    raise ControlException(
                        message="bad param 'strict_type', invalid value")
            self.bot.log.debug(self.CF_ADDRULES_TYPED_ADDED)

    def load_strict_tags(self, strict_tags=None):
        """Validate if element.tag is in list of strict_tags and
            instance ControlForm specific properties

            tag=select, instance down 'dropdown' property

        Keyword Arguments:
            strict_tags {list} -- list of StrictRule.tag values
                (default: {None})

        Returns:
            bool -- if success execution of this method return True
        """
        self.bot.log.debug(self.CF_STRICTTAGS_LOADING)
        if strict_tags is None:
            strict_tags = self.strict_tags
        # empty list doesn't to be checked
        if len(strict_tags) == 0:
            self.bot.log.debug(self.CF_STRICTTAGS_NOTAGS)
            return True
        for strict_tag in strict_tags:
            if self.tag == strict_tag.value:
                # specific elements logic
                if self.tag == 'select':
                    self.dropdown = Select(self.element)
                self.bot.log.debug(self.CF_STRICTTAGS_LOADED)
                return True
        if self.on_instance_strict:
            self.bot.log.error(self.CF_STRICTTAGS_ENABLED_ERROR)
            raise ControlException(
                message=("Validation raises at strict_tags for this element:"
                         "control={}, strict_tags=[{}]").format(
                             self, strict_tags))
        self.bot.log.debug(self.CF_STRICTTAGS_NOT_LOADED)
        return False

    def load_strict_attrs(self, strict_attrs=None):
        """Validate if element.attrs is in list of strict_attrs

        Keyword Arguments:
            strict_attrs {[type]} -- [description] (default: {None})

        Returns:
            bool -- if success execution of this method return True
        """
        self.bot.log.debug(self.CF_STRICTATTRS_LOADING)
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
                    self.bot.log.debug(self.CF_STRICTATTRS_NOT_LOADED)
                    return False
                self.bot.log.error(self.CF_STRICTATTRS_ERROR)
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
            self.bot.log.error(self.CF_STRICTATTRS_ERROR)
            raise ControlException(
                message=("Validation raises for strict_attrs "
                         "for this element:"
                         "control={}, strict_attrs=[{}]").format(
                             self, strict_attrs))
        self.bot.log.debug(self.CF_STRICTATTRS_LOADED)
        return is_attrs

    def load_strict_css_props(self, strict_css_props=None):
        """Validate if element.attrs is in list of strict_attrs

        Keyword Arguments:
            strict_css_props {[type]} -- [description] (default: {None})

        Returns:
            bool -- if success execution of this method return True
        """
        self.bot.log.debug(self.CF_STRICTCSS_LOADING)
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
            self.bot.log.error(self.CF_STRICTCSS_ERROR)
            raise ControlException(
                message=("Validation raises for strict_css_props "
                         "for this element:"
                         "control={}, strict_css_props=[{}]").format(
                             self, strict_css_props))
        if not is_css:
            self.bot.log.debug(self.CF_STRICTCSS_NOT_LOADED)
        else:
            self.bot.log.debug(self.CF_STRICTCSS_LOADED)
        return is_css

    def parse_rules(self, strict_rules=None):
        """Parse array of configurations dicts of strict_rules to
            instances list of StrictRule
        """
        self.bot.log.debug(self.CF_PARSERULES_LOADING)
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
        self.bot.log.debug(self.CF_PARSERULES_LOADED)
        return typed_rules

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        self.bot.log.debug(self.CF_RELOAD_LOADING)
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
            enabled=config.get('on_instance_search'))
        self._load_properties(
            enabled=config.get('on_instance_load'))
        self._load_strict(
            enabled=config.get('on_instance_strict'))
        self.bot.log.debug(self.CF_RELOAD_LOADED)

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
        self.bot.log.debug(self.CF_DROPDOWNSELECT_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.RELOAD_CONFIG)
        if self.dropdown is None:
            raise ControlException(
                message=("Element must be dropdown"
                         " (tag={})").format(self.tag))
        if by_value and by_index:
            raise ControlException(
                message=("Can't use this function with"
                         " all flags with True values"))
        if by_value:
            self.dropdown.select_by_value(text)
        elif by_index:
            if not isinstance(text, int):
                raise ControlException(message="index must be an int value")
            self.dropdown.select_by_index(int(text))
        else:
            self.dropdown.select_by_visible_text(text)
        self.bot.log.debug(self.CF_DROPDOWNSELECT_LOADED)

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
        self.bot.log.debug(self.CF_DROPDOWNDESELECT_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        if self.dropdown is None:
            raise ControlException(
                message=("Element must be dropdown"
                         " (tag={})").format(self.tag))
        if by_value and by_index:
            raise ControlException(
                message=("Can't use this function with"
                         " all flags with True values"))
        if by_value:
            self.dropdown.deselect_by_value(text)
        elif by_index:
            if not isinstance(text, int):
                raise ControlException(message="index must be an int value")
            self.dropdown.deselect_by_index(int(text))
        else:
            self.dropdown.deselect_by_visible_text(text)
        self.bot.log.debug(self.CF_DROPDOWNDESELECT_LOADED)

    def dropdown_deselect_all(self):
        """The Select class only works with tags which have select
            tags with multiple="multiple" attribute.

        Raises:
            ControlException -- if tag is not 'select'
        """
        self.bot.log.debug(self.CF_DROPDOWNDESELECTALL_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        if self.dropdown is None:
            raise ControlException(
                message=("Element must be dropdown"
                         " (tag={})").format(self.tag))
        self.dropdown.deselect_all()
        self.bot.log.debug(self.CF_DROPDOWNDESELECTALL_LOADED)

    def __repr__(self):
        """Show basic properties for this object"""
        return super(ControlForm, self).__repr__()
