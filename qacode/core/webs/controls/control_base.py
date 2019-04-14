# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_base"""


from collections import defaultdict
from qacode.core.bots.bot_base import BotBase
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers import logger_messages as MSG
from selenium.common.exceptions import (
    ElementNotVisibleException, NoSuchElementException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ControlBase(object):
    """Requirements: #35, #70"""

    # Instance properties
    bot = None
    settings = None
    # Settings properties
    name = None
    locator = None
    selector = None
    on_instance_search = None
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

    def __init__(self, bot, **kwargs):
        """Wrapper for Selenium class named 'WebElement' using
            wrapper of WebDriver named qacode.core.bots.BotBase

        Arguments:
            bot {BotBase} -- BotBase instance
        """
        if not bot or not isinstance(bot, BotBase):
            raise ControlException(msg="Bad param 'bot'")
        self.bot = bot
        # load settings before try to instance
        # needed for self._load_* functions
        self.__load_settings_keys__(kwargs.copy(), update=True)
        # instance logic
        self.__load_search__(
            enabled=self.on_instance_search,
            element=self.settings.get("element"))

    def __load_settings_keys__(self, settings,
                               update=False, default_keys=None):
        """Load default setting for ControlBase instance"""
        self.bot.log.debug(MSG.CB_SETTINGS_LOADING)
        # generate default dict
        if default_keys is None:
            default_keys = [
                ("selector", None),  # required
                ("name", "UNNAMED"),
                ("locator", By.CSS_SELECTOR),
                ("on_instance_search", False),
                ("auto_reload", True),
                ("instance", 'ControlBase'),
                ("element", None)
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
                raise ControlException(msg=msg)
            # optional keys, update with default value
            if value is None:
                value = default_settings.get(key)
            # update object property value and prepare
            # settings to be updated
            updated_settings.update({key: value})
            setattr(self, key, updated_settings.get(key))
        if update:
            self.settings = updated_settings
        self.bot.log.debug(MSG.CB_SETTINGS_LOADED)

    def __load_search__(self, enabled=False, element=None):
        """Load element searching at selenium WebDriver"""
        if enabled is None or not enabled:
            self.bot.log.debug(MSG.CB_SEARCH_DISABLED)
            self.bot.log.debug(MSG.CB_PROP_DISABLED)
            return False
        self.bot.log.debug(MSG.CB_SEARCH_LOADING)
        try:
            if element is not None:
                if not isinstance(element, WebElement):
                    msg = "Child is not instance of WebElement"
                    raise ControlException(msg=msg)
                self.bot.log.debug(MSG.CB_SEARCH_FOUND_CHILD)
                self.element = element
            else:
                self.element = self.bot.navigation.find_element(
                    self.selector, locator=self.locator)
        except CoreException:
            self.bot.log.warning(MSG.CB_SEARCH_WAITING)
            self.element = self.bot.navigation.find_element_wait(
                self.selector, locator=self.locator)
        if self.element:
            self.bot.log.debug(MSG.CB_SEARCH_FOUND)
        self.bot.log.debug(MSG.CB_PROP_LOADING)
        self.tag = self.get_tag()
        self.text = self.get_text()
        self.is_displayed = self.bot.navigation.ele_is_displayed(self.element)
        self.is_enabled = self.bot.navigation.ele_is_enabled(self.element)
        self.is_selected = self.bot.navigation.ele_is_selected(self.element)
        self.attr_id = self.get_attr_value('id')
        self.attr_class = self.get_attr_value('class').split()
        self.bot.log.debug(MSG.CB_PROP_LOADED)
        return True

    def __check_reload__(self):
        """Allow to check before methods calls to ensure
            if it's neccessary reload element properties
        """
        if not self.element and self.auto_reload:
            self.reload(**self.settings)

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
        self.bot.log.debug(MSG.CB_FINDCHILD_LOADING.format(selector))
        self.__check_reload__()
        settings = {"locator": locator, "selector": selector}
        ele = self.bot.navigation.find_element_child(
            self.element, selector, locator=locator)
        settings.update({"element": ele})
        ctl = ControlBase(self.bot, **settings)
        if ctl:
            self.bot.log.debug(MSG.CB_FINDCHILD_LOADED)
        return ctl

    def find_children(self, selector, locator=By.CSS_SELECTOR):
        """Find children elements using bot with default By.CSS_SELECTOR
            strategy for internal element trought selenium WebElement

        Arguments:
            selector {str} -- string search for locator type

        Keyword Arguments:
            locator {[selenium.webdriver.common.by.By]} -- string type to
                use on this selenium search request
                (default: {By.CSS_SELECTOR})

        Returns:
            list(ControlBase) -- instanced list of base element using
                qacode library object
        """
        self.bot.log.debug(MSG.CB_FINDCHILD_LOADING.format(selector))
        self.__check_reload__()
        settings = {"locator": locator, "selector": selector}
        elements = self.bot.navigation.find_element_children(
            self.element, selector, locator=locator)
        ctls = list()
        for ele in elements:
            settings.update({"element": ele})
            ctls.append(ControlBase(self.bot, **settings))
        if bool(ctls):
            self.bot.log.debug(MSG.CB_FINDCHILD_LOADED)
        return ctls

    def get_tag(self):
        """Returns tag_name from Webelement"""
        self.bot.log.debug(MSG.CB_GETTAG_LOADING)
        self.__check_reload__()
        tag_name = self.bot.navigation.ele_tag(self.element)
        if tag_name:
            self.bot.log.debug(MSG.CB_GETTAG_LOADED.format(tag_name))
        self.tag = tag_name
        return tag_name

    def type_text(self, text, clear=False):
        """Type text on input element

        Arguments:
            text {str} -- string to be typed on web element

        Keyword Arguments:
            clear {bool} -- clear text element at enable key (default: {False})
        """
        self.bot.log.debug(MSG.CB_TYPETEXT_LOADING.format(text))
        self.__check_reload__()
        if clear:
            self.clear()
        self.bot.navigation.ele_write(self.element, text)
        self.text = text

    def clear(self):
        """Clear input element text value"""
        self.bot.log.debug(MSG.CB_CLEAR_LOADING)
        self.__check_reload__()
        self.bot.navigation.ele_clear(self.element)
        self.bot.log.debug(MSG.CB_CLEAR_LOADED)

    def click(self, retry=True):
        """Click on element"""
        self.bot.log.debug(MSG.CB_CLICK_LOADING)
        self.__check_reload__()
        try:
            self.bot.navigation.ele_click(element=self.element)
        except (ElementNotVisibleException, NoSuchElementException) as err:
            if retry:
                self.bot.log.warning(MSG.CB_CLICK_RETRY)
                self.reload(**self.settings)
                self.bot.navigation.ele_click(element=self.element)
            else:
                raise err
        self.bot.log.debug(MSG.CB_CLICK_LOADED)

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
        self.bot.log.debug(MSG.CB_GETTEXT_LOADING)
        self.__check_reload__()
        text = None
        try:
            if self.tag == 'input':
                text = self.get_attr_value('value')
            else:
                text = self.bot.navigation.ele_text(
                    self.element, on_screen=on_screen)
        except CoreException as err:
            self.bot.log.error(MSG.CB_GETTEXT_FAILED)
            raise ControlException(err=err)
        if text:
            self.text = text
            self.bot.log.debug(MSG.CB_GETTEXT_LOADED.format(text))
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
        self.bot.log.debug(MSG.CB_GETATTRS_LOADING)
        self.__check_reload__()
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
        self.bot.log.debug(MSG.CB_GETATTRVALUE_LOADING.format(attr_name))
        self.__check_reload__()
        try:
            value = self.bot.navigation.ele_attribute(
                self.element, attr_name)
            self.bot.log.debug(
                MSG.CB_GETATTRVALUE_LOADED.format(attr_name, value))
            return str(value)
        except CoreException as err:
            self.bot.log.error(MSG.CB_GETATTRVALUE_FAILED)
            raise ControlException(err=err)

    def get_css_value(self, prop_name):
        """Allows to obtain CSS value based on CSS property name

        Arguments:
            prop_name {str} -- CSS property name

        Returns:
            str -- Value of CSS property searched
        """
        self.bot.log.debug(MSG.CB_GETCSSRULE_LOADING)
        self.__check_reload__()
        css_value = self.bot.navigation.ele_css(self.element, prop_name)
        self.bot.log.debug(MSG.CB_GETCSSRULE_LOADED.format(css_value))
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
            MSG.CB_SETCSSRULE_LOADING.format(prop_name, prop_value))
        self.__check_reload__()
        self.bot.navigation.set_css_rule(
            self.selector, prop_name, prop_value,
            css_important=css_important)
        if self.selector is None:
            self.bot.log.error(MSG.CB_SETCSSRULE_FAILED)
            raise ControlException(msg="Couldn't reload element")
        self.reload(**self.settings)

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        class_name = self.__class__.__name__
        self.bot.log.debug(MSG.CB_RELOAD_LOADING.format(class_name))
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
        if class_name == 'ControlBase':
            self.bot.log.debug(MSG.CB_RELOAD_LOADED.format(class_name))

    def wait_invisible(self, timeout=0):
        """Wait for invisible element, returns control"""
        self.element = self.bot.navigation.ele_wait_invisible(
            self.selector, locator=self.locator, timeout=timeout)
        return self

    def wait_visible(self, timeout=0):
        """Wait for visible element, returns control"""
        self.__check_reload__()
        self.element = self.bot.navigation.ele_wait_visible(
            self.element, timeout=timeout)
        return self

    def wait_text(self, text, timeout=0):
        """Wait if the given text is present in the specified control"""
        if self.tag == 'input':
            is_text = self.bot.navigation.ele_wait_value(
                self.selector, text, locator=self.locator, timeout=timeout)
        try:
            is_text = self.bot.navigation.ele_wait_text(
                self.selector, text, locator=self.locator, timeout=timeout)
        except CoreException:
            self.bot.log.warning("skipped failed at wait for text on control")
        self.get_text()
        return is_text

    def wait_blink(self, timeout=0):
        """Wait until control pops and dissapears"""
        return self.wait_visible(
            timeout=timeout).wait_invisible(timeout=timeout)

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
