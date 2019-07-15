# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_base"""


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
    """This class allow to reference remote NodeElement (JS) or Html Tag to
        use checks , obtain information or handle actions using this instance.
        Wrapper for Selenium class named 'WebElement' using wrapper of
        WebDriver named qacode.core.bots.BotBase

    Arguments:
        object {object} -- Base class to inherit
    """

    def __init__(self, bot, **kwargs):
        """Initialize an instance of ControlBase

        Arguments:
            bot {BotBase} -- BotBase instance
        """
        if not bot or not isinstance(bot, BotBase):
            raise ControlException(msg="Bad param 'bot'")
        # instance minimal data
        self._bot = bot
        self._name = None
        self._locator = None
        self._selector = None
        self._element = None
        self._on_instance_search = None
        self._auto_reload = None
        # __search__, step 2
        self._tag = None
        self._text = None
        self._is_displayed = None
        self._is_enabled = None
        self._is_selected = None
        self._attr_id = None
        self._attr_class = None
        self._bot.log.debug(
            "ctl | Generating instance of type {}...".format(
                self.__class__.__name__))
        self.__load__(**kwargs)

    def __load__(self, **kwargs):
        """Allow to reinstance control properties"""
        self._settings = self.__settings_parse__(**kwargs)
        if self._element:
            # Control instanced from child
            self._bot.log.debug("ctl | Child instance...")
            if self._on_instance_search:
                raise ControlException(
                    "ctl | Can't auto search when child element")
        if not self._on_instance_search:
            self.bot.log.debug(MSG.CB_SEARCH_DISABLED)
            self.bot.log.debug(MSG.CB_PROP_DISABLED)
            return
        self.__search__()

    def __settings_parse__(self, **kwargs):
        """Allow to parse settings dict from instance kwargs updating
            just valid keys with default values if it's required
        """
        self.bot.log.debug(MSG.CB_SETTINGS_LOADING)
        self._selector = kwargs.get("selector")
        self._name = kwargs.get("name")
        self._locator = kwargs.get("locator")
        self._on_instance_search = kwargs.get("on_instance_search")
        self._auto_reload = kwargs.get("auto_reload")
        self._element = kwargs.get("element")
        # validate params
        if self._selector is None or self._selector == '':
            raise ControlException(
                "ctl | Selector it's required to use instance")
        if self._name is None:
            self._name = "UNNAMED"
        if self._locator is None:
            self._locator = By.CSS_SELECTOR
        if self._on_instance_search is None:
            self._on_instance_search = False
        if self._auto_reload is None:
            self._auto_reload = True
        settings = {
            "name": self._name,
            "locator": self._locator,
            "selector": self._selector,
            "on_instance_search": self._on_instance_search,
            "auto_reload": self._auto_reload,
        }
        self.bot.log.debug(MSG.CB_SETTINGS_LOADED)
        return settings

    def __search__(self):
        """Load element searching at selenium WebDriver"""
        self.bot.log.debug(MSG.CB_SEARCH_LOADING)
        # Step 1 ensure web element
        is_element = isinstance(self._element, WebElement)
        nav = self.bot.navigation
        if self._element and not is_element:
            raise ControlException("Child is not instance of WebElement")
        if self._element and is_element:
            # nothing to do
            self.bot.log.debug(MSG.CB_SEARCH_FOUND_CHILD)
            return
        try:
            self._element = nav.find_element(
                self._selector, locator=self._locator)
        except CoreException:
            self.bot.log.warning(MSG.CB_SEARCH_WAITING)
            self._element = nav.find_element_wait(
                self._selector, locator=self._locator)
        if self._element:
            self.bot.log.debug(MSG.CB_SEARCH_FOUND)
        # Step 2 load minimal properties defined by qacode
        self.bot.log.debug(MSG.CB_PROP_LOADING)
        self._tag = self.get_tag()
        self._text = self.get_text()
        self._is_displayed = nav.ele_is_displayed(self.element)
        self._is_enabled = nav.ele_is_enabled(self.element)
        self._is_selected = nav.ele_is_selected(self.element)
        self._attr_id = self.get_attr_value('id')
        self._attr_class = self.get_attr_value('class').split()
        self.bot.log.debug(MSG.CB_PROP_LOADED)

    def __check_reload__(self):
        """Allow to check before methods calls to ensure
            if it's neccessary reload element properties
        """
        if not self._element and self._auto_reload:
            self.reload()
            return True
        return False

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
        tag = self.bot.navigation.ele_tag(self.element)
        self.bot.log.debug(MSG.CB_GETTAG_LOADED.format(tag))
        self._tag = tag
        return tag

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
        self._text = text

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
            self._text = text
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
        self.__load__(**config)
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

    @property
    def bot(self):
        """GET for _bot attribute"""
        return self._bot

    @bot.setter
    def bot(self, value):
        """SET for _bot attribute"""
        if not value or not isinstance(value, BotBase):
            raise ControlException(msg="Bad param 'bot'")
        self._bot = value

    @property
    def settings(self):
        """GET for _settings attribute"""
        return self._settings

    @settings.setter
    def settings(self, value):
        """SET for _settings attribute"""
        if not value or not isinstance(value, dict):
            raise ControlException(msg="Bad param 'settings'")
        self._settings = self.__settings_parse__(**value)

    @property
    def name(self):
        """GET for _name attribute"""
        return self._name

    @name.setter
    def name(self, value):
        """SET for _name attribute"""
        if not value or not isinstance(value, str):
            raise ControlException(msg="Bad param 'name'")
        self._name = value

    @property
    def selector(self):
        """GET for _selector attribute"""
        return self._selector

    @selector.setter
    def selector(self, value):
        """SET for _selector attribute"""
        if not value or not isinstance(value, str):
            raise ControlException(msg="Bad param 'selector'")
        self._selector = value

    @property
    def element(self):
        """GET for _element attribute"""
        return self._element

    @element.setter
    def element(self, value):
        """SET for _element attribute"""
        self._element = value

    @property
    def locator(self):
        """GET for _locator attribute"""
        return self._locator

    @property
    def on_instance_search(self):
        """GET for _on_instance_search attribute"""
        return self._on_instance_search

    @property
    def auto_reload(self):
        """GET for _auto_reload attribute"""
        return self._auto_reload

    @property
    def tag(self):
        """GET for _tag attribute"""
        return self._tag

    @property
    def text(self):
        """GET for _text attribute"""
        return self._text

    @property
    def is_displayed(self):
        """GET for _is_displayed attribute"""
        return self._is_displayed

    @property
    def is_enabled(self):
        """GET for _is_enabled attribute"""
        return self._is_enabled

    @property
    def is_selected(self):
        """GET for _is_selected attribute"""
        return self._is_selected

    @property
    def attr_id(self):
        """GET for _attr_id attribute"""
        return self._attr_id

    @property
    def attr_class(self):
        """GET for _attr_class attribute"""
        return self._attr_class
