# -*- coding: utf-8 -*-


from qacode.core.exceptions.ControlException import ControlException


class ControlBase(object):
    """Requirements: #35"""

    bot = None
    selector = None
    element = None
    # noqa for this properties, yet
    text = None

    def __init__(self, bot, selector="", element=None, search=True):
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
            self.element = self.find_element(selector)
        else:
            self.element = element
        # noqa for this logic, yet
        if self.element is None:
            raise ControlException(message_errors[2].format(self.selector,
                                                            self.element))
        self.text = self.text()

    def find_element(self, selector):
        """
        Find element using bot with default By.CSS_SELECTOR strategy for
        internal element
        """
        self.bot.log.debug("find_element: selector={}".format(selector))
        return self.bot.navigation.find_element(selector)

    def type(self, text):
        """Type text on input element"""
        self.bot.navigation.ele_write(self.element, text)

    def click(self):
        """Click on element"""
        self.bot.navigation.ele_click(element=self.element)

    def text(self):
        """Return element content text"""
        return self.bot.navigation.ele_text(self.element)

    def attrs(self, attr_names=[]):
        """Find a list of attributes on WebElement with this name"""
        attrs = []
        for attr_name in attr_names:
            attrs.append(self.attr(attr_name))
        return attrs

    def attr(self, attr_name, attr_value=None):
        """
        attr_name : find an attribute on WebElement with this name
        attr_value: if value it's not None, then validate value
        """
        validated = False
        name, value = self.bot.navigation.ele_attribute(
            self.element, attr_name
        )
        if attr_value is not None:
            validated = str(attr_value).endswith(value)
        return (name, value, validated)
