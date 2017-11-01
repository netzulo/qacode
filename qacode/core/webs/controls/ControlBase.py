# -*- coding: utf-8 -*-
# pylint: disable=too-many-arguments
""""TODO: doc module"""


from selenium.webdriver.common.by import By
from qacode.core.exceptions.ControlException import ControlException


class ControlBase(object):
    """Requirements: #35, #70"""

    bot = None
    selector = None
    element = None
    # noqa for this properties, yet
    text = None
    attrs = None

    def __init__(self, bot, selector='', locator=By.CSS_SELECTOR,
                 element=None, search=True):
        """
        Args:
            selector: can be empty string to use element insteadof
                      of params to load WebElement
            locator: selenium search strategy
            element: instanced WebElement class
        Usage:
            ControlBase(bot, selector, locator) :TODO
            ControlBase(bot, element) :TODO
            ControlBase(bot, element, search=True) :TODO, must raise CoreEx
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
            self.element = self.find_element(selector, locator=locator)
        else:
            self.element = element
        # noqa for this logic, yet
        if self.element is None:
            raise ControlException(message_errors[2].format(self.selector,
                                                            self.element))
        self.attrs = {
            "id" : self.get_attr('id'),
            "class" : self.get_attr('class')
        }
        self.text = self.get_text()

    def find_element(self, selector, locator=By.CSS_SELECTOR):
        """
        Find element using bot with default By.CSS_SELECTOR strategy for
        internal element
        """
        self.bot.log.debug("find_element: selector={}".format(selector))
        return self.bot.navigation.find_element(selector, locator=locator)

    def type_text(self, text):
        """Type text on input element

        Args:
            text: string
        """
        self.bot.navigation.ele_write(self.element, text)

    def click(self):
        """Click on element"""
        self.bot.navigation.ele_click(element=self.element)

    def get_text(self):
        """Return element content text"""
        return self.bot.navigation.ele_text(self.element)

    def get_attrs(self, attr_names):
        """Find a list of attributes on WebElement with this name"""
        attrs = list(attr_names)
        for attr_name in attr_names:
            attrs.append(self.get_attr(attr_name))
        return attrs

    def get_attr(self, attr_name, attr_value=None, return_name_too=False):
        """
        Search and attribute name over self.element and get value,
        if attr_value is obtained, then compare and raise if not
        Args:
            attr_name : find an attribute on WebElement with this name
            attr_value: if value it's not None, check if
                        endswith attr_value
            return_name_too: returns tuple of (name, value)
                             instead of value
        """
        is_valid = False
        name, value = self.bot.navigation.ele_attribute(
            self.element, attr_name)
        if attr_value is not None:
            is_valid = str(attr_value).endswith(value)
        if is_valid:
            return value
        if return_name_too:
            return name, value
