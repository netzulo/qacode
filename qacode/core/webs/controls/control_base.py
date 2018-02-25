# -*- coding: utf-8 -*-
# pylint: disable=too-many-arguments
"""TODO: doc module"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.exceptions.core_exception import CoreException
from selenium.webdriver.common.by import By


class ControlBase(object):
    """Requirements: #35, #70"""

    # Instance properties
    bot = None
    selector = None
    element = None
    # Element properties
    tag = None
    text = None
    is_displayed = None
    is_enabled = None
    is_selected = None
    attr_id = None
    attr_class = None

    def __init__(self, bot, selector='', locator=By.CSS_SELECTOR,
                 element=None, search=True, wait_for_load=False):
        """Base class to manage web element through page system of qacode
            library

        Usage:
            ControlBase(bot, selector, locator)
            ControlBase(bot, element)
            ControlBase(bot, element, search=True)

        Arguments:
            bot {BotBase} -- qacode bot Class to manage control validations

        Keyword Arguments:
            selector {str} -- can be empty string to use element insteadof of
                params to load WebElement
            locator {By} -- selenium search strategy
                (default: {By.CSS_SELECTOR})
            element {WebElement} -- instanced WebElement class
                (default: {None})
            search {bool} -- [description] (default: {True})
            wait_for_load {bool} -- wait for expected condition from selenium
                before to load element (default: {False})

        Raises:
            CoreEx -- param 'bot' can't be None
            ControlException -- param 'selector' can't be None, don't use if
                want to instance with 'element'
            ControlException -- param 'element' can't be None, don't use if
                want to instance with 'selector'
            ControlException -- 'element' found isn't valid to use, check
                selector and element
        """
        message_errors = [
            "param 'bot' can't be None",
            ("param 'selector' can't be None, don't use if want to instance "
             "with 'element'"),
            ("param 'element' can't be None, don't use if want to instance "
             "with 'selector'"),
            ("'element' found isn't valid to use, check ur selector={} and "
             "element={}"),
        ]
        if bot is None:
            raise ControlException(message_errors[0])
        self.bot = bot
        if selector is None:
            raise ControlException(message_errors[1])
        self.selector = selector
        if element is not None:
            search = False
        if search:
            self.element = self.load_element(
                selector, locator=locator, wait_for_load=wait_for_load)
        else:
            self.element = element
        # noqa for this logic, yet
        if self.element is None:
            raise ControlException(
                message_errors[2].format(
                    self.selector, self.element))
        self.tag = self.get_tag()
        self.text = self.get_text()
        self.is_displayed = self.bot.navigation.ele_is_displayed(self.element)
        self.is_enabled = self.bot.navigation.ele_is_enabled(self.element)
        self.is_selected = self.bot.navigation.ele_is_selected(self.element)
        self.attr_id = self.get_attr_value('id')
        self.attr_class = self.get_attr_value('class')

    def load_element(self, selector, locator=By.CSS_SELECTOR,
                     wait_for_load=False):
        """
        Find element using bot with default By.CSS_SELECTOR
            strategy for internal element
        """
        self.bot.log.debug("load_element: selector={}".format(selector))
        try:
            if wait_for_load:
                return self.bot.navigation.find_element_wait(
                    selector, locator=locator)
            return self.bot.navigation.find_element(
                selector, locator=locator)
        except CoreException as err:
            raise ControlException(
                err, message='Element not found at load control_base')

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
        self.bot.log.debug("find_child: selector={}".format(selector))
        return ControlBase(
            self.bot, element=self.element.find_element(
                locator, selector))

    def get_tag(self):
        """Returns tag_name from Webelement"""
        tag_name = self.bot.navigation.ele_tag(self.element)
        self.bot.log.debug("get_tag : tag={}".format(tag_name))
        return tag_name

    def type_text(self, text, clear=False):
        """Type text on input element

        Arguments:
            text {str} -- string to be typed on web element

        Keyword Arguments:
            clear {bool} -- clear text element at enable key (default: {False})
        """
        self.bot.log.debug("type_text : text={}".format(text))
        if clear:
            self.clear()
        self.bot.navigation.ele_write(self.element, text)
        self.text = text

    def clear(self):
        """Clear input element text value"""
        self.bot.navigation.ele_clear(self.element)

    def click(self):
        """Click on element"""
        self.bot.log.debug("click : clicking element...")
        self.bot.navigation.ele_click(element=self.element)

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
        try:
            value = self.bot.navigation.ele_attribute(self.element, attr_name)
            self.bot.log.debug(
                "get_attr : attr_name={}, value={}".format(attr_name, value))
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
        return self.bot.navigation.ele_css(self.element, prop_name)

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
        self.bot.navigation.set_css_rule(
            self.selector, prop_name, prop_value,
            css_important=css_important)
        if self.selector is None:
            raise ControlException(message="Couldn't reload element")
        # reload WebElement
        self.element = self.load_element(self.selector)
