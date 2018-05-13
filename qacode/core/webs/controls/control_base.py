# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_base"""


from qacode.core.bots.bot_base import BotBase
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.exceptions.core_exception import CoreException

from selenium.webdriver.common.by import By


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
    on_instance_load = None
    auto_reload = None
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
            raise ControlException(message="Bad param 'bot'")
        self.bot = bot
        # load settings before try to instance
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
            "auto_reload": kwargs.get('auto_reload')
        }
        # needed for self._load_* functions
        self.load_settings_keys(self.settings)
        # instance logic
        self._load_search(enabled=self.settings.get('on_instance_search'))
        self._load_properties(enabled=self.settings.get('on_instance_load'))

    def load_settings_keys(self, settings, update=False):
        """Load default setting for ControlBase instance"""
        self.bot.log.debug("control | load_settings_keys: loading keys...")
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
                    value = By.CSS_SELECTOR
                elif key == 'on_instance_search':
                    value = False
                elif key == 'on_instance_load':
                    value = False
                elif key == 'auto_reload':
                    value = True
                else:
                    raise ControlException(
                        message=("Bad settings: "
                                 "key={}, value={}").format(
                                     key, value))
            setattr(self, key, value)
        self.bot.log.debug("control | load_settings_keys: loaded keys!")

    def _load_search(self, enabled=False):
        if not enabled or enabled is None:
            self.bot.log.warning(
                "control | _load_search: !Disabled searching element!")
            return False
        self.bot.log.debug("control | _load_search: searching element...")
        try:
            self.element = self.bot.navigation.find_element(
                self.selector, locator=self.locator)
        except CoreException:
            self.bot.log.warning(
                "control | _load_search: waiting for element...")
            self.element = self.bot.navigation.find_element_wait(
                self.selector, locator=self.locator)
        self.bot.log.debug("control | _load_search: element found!")
        return True

    def _load_properties(self, enabled=False):
        if enabled and not self.settings.get('on_instance_search'):
            msg = ("Can't call to load_properties "
                   "wihout call first to load_search")
            self.bot.log.error(msg)
            raise ControlException(message=msg)
        if not enabled or enabled is None:
            self.bot.log.warning(
                ("control | _load_properties: "
                 "!Disabled loading ControlBase properties!"))
            return False
        self.bot.log.debug(
            "control | _load_properties: loading ControlBase properties...")
        self.tag = self.get_tag()
        self.text = self.get_text()
        self.is_displayed = self.bot.navigation.ele_is_displayed(self.element)
        self.is_enabled = self.bot.navigation.ele_is_enabled(self.element)
        self.is_selected = self.bot.navigation.ele_is_selected(self.element)
        self.attr_id = self.get_attr_value('id')
        self.attr_class = self.get_attr_value('class').split()
        self.bot.log.debug(
            "control | _load_properties: loaded ControlBase properties!")
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
        self.bot.log.debug(
            "control | find_child: selector={}".format(selector))
        settings = {
            "locator": locator,
            "selector": selector
        }
        return ControlBase(self.bot, **settings)

    def get_tag(self):
        """Returns tag_name from Webelement"""
        self.bot.log.debug("control | get_tag : obtaining tag...")
        if not self.element:
            self.reload(**self.settings)
        tag_name = self.bot.navigation.ele_tag(self.element)
        self.bot.log.debug(
            "control | get_tag : tag={}".format(tag_name))
        return tag_name

    def type_text(self, text, clear=False):
        """Type text on input element

        Arguments:
            text {str} -- string to be typed on web element

        Keyword Arguments:
            clear {bool} -- clear text element at enable key (default: {False})
        """
        self.bot.log.debug(
            "control | type_text : text={}".format(text))
        if not self.element:
            self.reload(**self.settings)
        if clear:
            self.clear()
        self.bot.navigation.ele_write(self.element, text)
        self.text = text

    def clear(self):
        """Clear input element text value"""
        self.bot.log.debug("control | clear : clearing text...")
        if not self.element:
            self.reload(**self.settings)
        self.bot.navigation.ele_clear(self.element)
        self.bot.log.debug("control | clear : cleared text!")

    def click(self):
        """Click on element"""
        self.bot.log.debug("control | click : clicking element...")
        if not self.element:
            self.reload(**self.settings)
        self.bot.navigation.ele_click(element=self.element)
        self.bot.log.debug("control | click : clicked!")

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
        self.bot.log.debug("control | get_text : obtaining text...")
        if not self.element:
            self.reload(**self.settings)
        try:
            return self.bot.navigation.ele_text(
                self.element, on_screen=on_screen)
        except CoreException as err:
            if isinstance(err, CoreException):
                raise ControlException(err, message=err.message)
            else:
                raise Exception(err, message=err.message)

    def get_attrs(self, attr_names):
        """Find a list of attributes on WebElement
        and returns a dict list of {name, value}

        Arguments:
            attr_names {list of str} -- list of attr_name to search
                for each one name and value on self.element

        Returns:
            dict -- a dict list of {name, value}
        """
        self.bot.log.debug("control | get_attrs : obtaining attrs...")
        if not self.element:
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
        self.bot.log.debug(
            ("control | get_attr_value : "
             "obtaining value for attr_name='{}'...").format(attr_name))
        if not self.element:
            self.reload(**self.settings)
        try:
            value = self.bot.navigation.ele_attribute(
                self.element, attr_name)
            self.bot.log.debug(
                ("control | get_attr_value : obtained "
                 "attr_name={}, value={}").format(attr_name, value))
            return value
        except CoreException as err:
            raise ControlException(err, message=err.message)

    def get_css_value(self, prop_name):
        """Allows to obtain CSS value based on CSS property name

        Arguments:
            prop_name {str} -- CSS property name

        Returns:
            str -- Value of CSS property searched
        """
        self.bot.log.debug("control | get_css_value : obtaining css_value...")
        if not self.element:
            self.reload(**self.settings)
        css_value = self.bot.navigation.ele_css(self.element, prop_name)
        self.bot.log.debug(
            "control | get_css_value : css_value={}".format(css_value))
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
            ("control | set_css_value : setting new CSS rule, "
             "prop_name={}, prop_value={}").format(
                prop_name, prop_value))
        if not self.element:
            self.reload(**self.settings)
        self.bot.navigation.set_css_rule(
            self.selector, prop_name, prop_value,
            css_important=css_important)
        if self.selector is None:
            raise ControlException(message="Couldn't reload element")
        self.reload(**self.settings)

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        self.bot.log.debug(
            "control | reload: reloading control...")
        # load settings again
        config = kwargs.copy()
        # needed for self._load_* functions
        self.load_settings_keys(config, update=True)
        # instance logic
        self._load_search(
            enabled=config.get('on_instance_search'))
        self._load_properties(
            enabled=config.get('on_instance_load'))
        self.bot.log.debug(
            "control | reload: reloaded control!")

    def __repr__(self):
        """Show basic properties for this object"""
        return ("ControlBase: name={}, "
                "bot.browser={}, bot.mode={} \n"
                "settings={}").format(
            self.settings.get('url'),
            self.bot.settings.get('browser'),
            self.bot.settings.get('mode'),
            self.settings)
