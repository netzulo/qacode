# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_base"""


from collections import defaultdict
from qacode.core.bots.bot_base import BotBase
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.exceptions.core_exception import CoreException

from selenium.webdriver.common.by import By


class ControlBase(object):
    """Requirements: #35, #70"""

    # Log messages
    CB_SETTINGS_LOADING = "control | load_settings_keys: loading keys..."
    CB_SETTINGS_LOADED = "control | load_settings_keys: loaded keys"
    CB_SEARCH_DISABLED = "control | _load_search: Disabled element search"
    CB_SEARCH_LOADING = "control | _load_search: searching element..."
    CB_SEARCH_WAITING = "control | _load_search: waiting for element..."
    CB_SEARCH_FOUND = "control | _load_search: element found!"
    CB_PROP_DISABLED = ("control | _load_properties: "
                        "disabled loading for properties")
    CB_PROP_LOADING = "control | _load_properties: loading properties..."
    CB_PROP_LOADED = "control | _load_properties: loaded properties"
    CB_FINDCHILD_LOADING = "control | find_child: searching for selector='{}'"
    CB_FINDCHILD_LOADED = "control | find_child: child element found"
    CB_GETTAG_LOADING = "control | get_tag: searching for tag"
    CB_GETTAG_LOADED = "control | get_tag: found same tag='{}'"
    CB_TYPETEXT_LOADING = "control | type_text: typing text={}"
    CB_CLEAR_LOADING = "control | clear: clearing text..."
    CB_CLEAR_LOADED = "control | clear: cleared text"
    CB_CLICK_LOADING = "control | click: clicking element..."
    CB_CLICK_LOADED = "control | click: clicked!"
    CB_GETTEXT_LOADING = "control | get_text: obtaining text..."
    CB_GETTEXT_FAILED = "control | get_text: failed at obtain text"
    CB_GETTEXT_LOADED = "control | get_text: text obtained, text='{}'"
    CB_GETATTRS_LOADING = "control | get_attrs: obtaining attrs..."
    CB_GETATTRVALUE_LOADING = ("control | get_attr_value: obtaining value "
                               "for attr_name='{}'")
    CB_GETATTRVALUE_LOADED = ("control | get_attr_value: obtained"
                              "attr_name='{}', value='{}'")
    CB_GETATTRVALUE_FAILED = "control | get_attr_value: fail at obtain value"
    CB_SETCSSRULE_LOADING = ("control | set_css_value: setting new CSS rule,"
                             " prop_name={}, prop_value={}")
    CB_SETCSSRULE_FAILED = "control | set_css_value: failed at set CSS rule"
    CB_GETCSSRULE_LOADING = "control | get_css_value: obtaining css_value..."
    CB_GETCSSRULE_LOADED = "control | get_css_value: css_value='{}'"
    CB_RELOAD_LOADING = "control | reload: reloading control..."
    CB_RELOAD_LOADED = "control | reload: reloaded control"
    # Instance properties
    bot = None
    settings = None
    # Settings properties
    name = None
    locator = None
    selector = None
    on_instance_search = None
    on_instance_load = None
    auto_reload = None
    instance = None
    # Element properties
    element = None
    tag = None
    text = None
    is_displayed = None
    is_enabled = None
    is_selected = None
    attr_id = None
    attr_class = None
    # Reload configuration
    RELOAD_CONFIG = {
        "on_instance_search": True,
        "on_instance_load": True,
    }

    def __init__(self, bot, **kwargs):
        """Wrapper for Selenium class named 'WebElement' using
            wrapper of WebDriver named qacode.core.bots.BotBase

        Arguments:
            bot {BotBase} -- BotBase instance
        """
        if not bot or not isinstance(bot, BotBase):
            raise ControlException(message="Bad param 'bot'")
        self.bot = bot
        # load settings before try to instance
        self.load(**kwargs)

    def load(self, **kwargs):
        """Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        # needed for self._load_* functions
        self.load_settings_keys(kwargs.copy(), update=True)
        # instance logic
        self._load_search(enabled=self.on_instance_search)
        self._load_properties(enabled=self.on_instance_load)

    def load_settings_keys(self, settings, update=False, default_keys=None):
        """Load default setting for ControlBase instance"""
        self.bot.log.debug(self.CB_SETTINGS_LOADING)
        # generate default dict
        if default_keys is None:
            default_keys = [
                ("selector", None),  # required
                ("name", "UNNAMED"),
                ("locator", By.CSS_SELECTOR),
                ("on_instance_search", False),
                ("on_instance_load", False),
                ("auto_reload", True),
                ("instance", 'ControlBase')
            ]
        default_settings = defaultdict(list, default_keys)
        updated_settings = {}
        # Parse param settings, key is each one of default_keys
        for key in default_settings.keys():
            # value from params dict
            value = settings.get(key)
            # required keys checks
            if value is None and key == 'selector':
                msg = "Bad settings: key={}, value={}".format(
                    key, value)
                raise ControlException(message=msg)
            # optional keys, update with default value
            if value is None:
                value = default_settings.get(key)
            # update object property value and prepare
            # settings to be updated
            updated_settings.update({key: value})
            setattr(self, key, updated_settings.get(key))
        if update:
            self.settings = updated_settings
        self.bot.log.debug(self.CB_SETTINGS_LOADED)

    def _load_search(self, enabled=False, selector_multiple_pos=0):
        if not enabled or enabled is None:
            self.bot.log.debug(self.CB_SEARCH_DISABLED)
            return False
        self.bot.log.debug(self.CB_SEARCH_LOADING)
        try:
            self.element = self.bot.navigation.find_element(
                self.selector, locator=self.locator)
        except CoreException:
            self.bot.log.warning(self.CB_SEARCH_WAITING)
            self.element = self.bot.navigation.find_element_wait(
                self.selector, locator=self.locator)
        if self.element:
            self.bot.log.debug(self.CB_SEARCH_FOUND)
        return True

    def _load_properties(self, enabled=False):
        """Load default properties for base element

        Keyword Arguments:
            enabled {bool} -- load at enabled (default: {False})

        Raises:
            ControlException -- if enabled and settings
                haven't key on_instance_search
        """
        if enabled and not self.settings.get('on_instance_search'):
            msg = ("Can't call to load_properties "
                   "wihout call first to load_search")
            self.bot.log.error(msg)
            raise ControlException(message=msg)
        if not enabled or enabled is None:
            self.bot.log.debug(self.CB_PROP_DISABLED)
            return False
        self.bot.log.debug(self.CB_PROP_LOADING)
        self.tag = self.get_tag()
        self.text = self.get_text()
        self.is_displayed = self.bot.navigation.ele_is_displayed(self.element)
        self.is_enabled = self.bot.navigation.ele_is_enabled(self.element)
        self.is_selected = self.bot.navigation.ele_is_selected(self.element)
        self.attr_id = self.get_attr_value('id')
        self.attr_class = self.get_attr_value('class').split()
        self.bot.log.debug(self.CB_PROP_LOADED)
        return True

    def find_child(self, selector, locator=By.CSS_SELECTOR):
        """Find child element using bot with default By.CSS_SELECTOR strategy
            for internal element trought selenium WebElement

        Arguments:
            selector {str} -- string search for locator type

        Keyword Arguments:
            locator {[selenium.webdriver.common.by.By]} -- string type to
                use on this selenium search request
                (default: {By.CSS_SELECTOR})

        Returns:
            ControlBase -- instanced base element using qacode library object
        """
        self.bot.log.debug(self.CB_FINDCHILD_LOADING.format(selector))
        settings = {"locator": locator, "selector": selector}
        ctl = ControlBase(self.bot, **settings)
        if ctl:
            self.bot.log.debug(self.CB_FINDCHILD_LOADED)
        return ctl

    def get_tag(self):
        """Returns tag_name from Webelement"""
        self.bot.log.debug(self.CB_GETTAG_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        tag_name = self.bot.navigation.ele_tag(self.element)
        if tag_name:
            self.bot.log.debug(self.CB_GETTAG_LOADED.format(tag_name))
        return tag_name

    def type_text(self, text, clear=False):
        """Type text on input element

        Arguments:
            text {str} -- string to be typed on web element

        Keyword Arguments:
            clear {bool} -- clear text element at enable key (default: {False})
        """
        self.bot.log.debug(self.CB_TYPETEXT_LOADING.format(text))
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        if clear:
            self.clear()
        self.bot.navigation.ele_write(self.element, text)
        self.text = text

    def clear(self):
        """Clear input element text value"""
        self.bot.log.debug(self.CB_CLEAR_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        self.bot.navigation.ele_clear(self.element)
        self.bot.log.debug(self.CB_CLEAR_LOADED)

    def click(self):
        """Click on element"""
        self.bot.log.debug(self.CB_CLICK_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        self.bot.navigation.ele_click(element=self.element)
        self.bot.log.debug(self.CB_CLICK_LOADED)

    def get_text(self, on_screen=True):
        """Get element content text.
            If the isDisplayed() method can sometimes trip over when
            the element is not really hidden but outside the viewport
            get_text() returns an empty string for such an element.

        Keyword Arguments:
            on_screen {bool} -- allow to obtain text if element
                it not displayed to this element before
                read text (default: {True})

        Returns:
            str -- Return element content text (innerText property)
        """
        self.bot.log.debug(self.CB_GETTEXT_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        text = None
        try:
            text = self.bot.navigation.ele_text(
                self.element, on_screen=on_screen)
        except CoreException as err:
            self.bot.log.error(self.CB_GETTEXT_FAILED)
            raise ControlException(err, message=err.message)
        if text:
            self.text = text
            self.bot.log.debug(self.CB_GETTEXT_LOADED.format(text))
        return text

    def get_attrs(self, attr_names):
        """Find a list of attributes on WebElement
        and returns a dict list of {name, value}

        Arguments:
            attr_names {list of str} -- list of attr_name to search
                for each one name and value on self.element

        Returns:
            dict -- a dict list of {name, value}
        """
        self.bot.log.debug(self.CB_GETATTRS_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        attrs = list()
        for attr_name in attr_names:
            attrs.append({
                "name": attr_name,
                "value": self.get_attr_value(attr_name)
            })
        return attrs

    def get_attr_value(self, attr_name):
        """Search and attribute name over self.element and get value,
        if attr_value is obtained, then compare and raise if not

        Arguments:
            attr_name {str} -- find an attribute on WebElement
                with this name

        Returns:
            str -- value of html attr_name
        """
        self.bot.log.debug(self.CB_GETATTRVALUE_LOADING.format(attr_name))
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        try:
            value = self.bot.navigation.ele_attribute(
                self.element, attr_name)
            self.bot.log.debug(
                self.CB_GETATTRVALUE_LOADED.format(attr_name, value))
            return value
        except CoreException as err:
            self.bot.log.error(self.CB_GETATTRVALUE_FAILED)
            raise ControlException(err, message=err.message)

    def get_css_value(self, prop_name):
        """Allows to obtain CSS value based on CSS property name

        Arguments:
            prop_name {str} -- CSS property name

        Returns:
            str -- Value of CSS property searched
        """
        self.bot.log.debug(self.CB_GETCSSRULE_LOADING)
        if not self.element and self.auto_reload:
            self.reload(**self.settings)
        css_value = self.bot.navigation.ele_css(self.element, prop_name)
        self.bot.log.debug(self.CB_GETCSSRULE_LOADED.format(css_value))
        return css_value

    def set_css_value(self, prop_name, prop_value, css_important=True):
        """Set new value for given CSS property name
            on ControlBase selector

        Arguments:
            prop_name {str} -- CSS property name
            prop_value {str} -- CSS property value

        Keyword Arguments:
            css_important {bool} -- Allow to include '!important' to rule for
                overrite others values applied (default: {True})
        """
        self.bot.log.debug(
            self.CB_SETCSSRULE_LOADING.format(prop_name, prop_value))
        if not self.element and self.auto_reload:
            self.reload(**self.s)
        self.bot.navigation.set_css_rule(
            self.selector, prop_name, prop_value,
            css_important=css_important)
        if self.selector is None:
            self.bot.log.error(self.CB_SETCSSRULE_FAILED)
            raise ControlException(message="Couldn't reload element")
        self.reload(**self.settings)

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        self.bot.log.debug(self.CB_RELOAD_LOADING)
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
            enabled=self.settings.get('on_instance_search'))
        self._load_properties(
            enabled=self.settings.get('on_instance_load'))
        self.bot.log.debug(self.CB_RELOAD_LOADED)

    def __repr__(self):
        """Show basic properties for this object"""
        return ("{}: name={}, "
                "bot.browser={}, bot.mode={} \n"
                "settings={} \n"
                "tag={}, is_displayed={}, "
                "is_enabled={}, is_selected={}").format(
            self.__class__.__name__,
            self.name,
            self.bot.settings.get('browser'),
            self.bot.settings.get('mode'),
            self.settings,
            self.tag,
            self.is_displayed,
            self.is_enabled,
            self.is_selected)
