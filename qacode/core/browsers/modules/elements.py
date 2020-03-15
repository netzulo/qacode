# -*- coding: utf-8 -*-
"""TODO"""


from qacode.core.browsers.modules.module import Module
from selenium.webdriver.common.by import By


class ModuleElements(Module):
    """TODO: doc class"""

    def __init__(self, driver, driver_wait):
        """TODO: doc method"""
        self._driver = driver
        self._driver_wait = driver_wait

    def find(self, selector, locator=By.CSS_SELECTOR):
        """Just divided execution ways for search
            web element throught selenium
        """
        self.__check_not_none__("locator", locator)
        # Not found: NoSuchElementException, StaleElementReferenceException
        return self._driver.find_element(locator, selector)

    def finds(self, selector, locator=By.CSS_SELECTOR,
              raises_zero=True):
        """Just divided execution ways for search
            web elements throught selenium
        """
        self.__check_not_none__("locator", locator)
        # Not found: NoSuchElementException, StaleElementReferenceException
        elements = self._driver.find_elements(locator, selector)
        if len(elements) == 0 and raises_zero:
            raise Exception("finds: 0 elements found")
        return elements

    def find_child(self, element, child_selector, locator=By.CSS_SELECTOR):
        """TODO: doc method"""
        self.__check_not_none__("locator", locator)
        # Not found: NoSuchElementException, StaleElementReferenceException
        return element.find_element(locator, child_selector)

    def find_children(self, element, child_selector, locator=By.CSS_SELECTOR):
        """TODO: doc method"""
        self.__check_not_none__("locator", locator)
        # Not found: NoSuchElementException, StaleElementReferenceException
        return element.find_elements(locator, child_selector)

    def finds_child(self):
        """TODO: doc method"""
        # at Java lang exist 1 expected condition
        # named : visibilityOfNestedElementsLocatedBy
        # doc : https://selenium-python.readthedocs.io/waits.html
        # maybe must exist at python too
        # then, create and use new method named: find_element_child_wait()
        # raise NotImplementedError("TODO:open an issue at github please")
        raise NotImplementedError("TODO: open an issue at github please")

    def finds_children(self):
        """TODO: doc method"""
        # at Java lang exist 1 expected condition
        # named : visibilityOfNestedElementsLocatedBy
        # doc : https://selenium-python.readthedocs.io/waits.html
        # maybe must exist at python too
        # then, create and use new method named: find_element_child_wait()
        # raise NotImplementedError("TODO:open an issue at github please")
        raise NotImplementedError("TODO: open an issue at github please")

    def click(self, element):
        """Perform click webelement with element

        Returns:
            WebElement -- returns element clicked (to allow chaining)
        """
        element.click()
        return element

    def write(self, element, text=None):
        """Over element perform send_keys , if not sended will
            write empty over element

        Returns:
            WebElement -- returns element clicked (to allow chaining)
        """
        if not text:
            # it's neccessary because some fields shows
            #   validation message and color just after
            #   try to send empty message
            element.send_keys()
        else:
            element.send_keys(text)
        return element

    def attr(self, element, attr_name):
        """Returns tuple with (attr, value) if founds
            This method will first try to return the value of a property with
            the given name. If a property with that name doesn't exist, it
            returns the value of the attribute with the same name. If there's
            no attribute with that name, None is returned.
        """
        value = element.get_attribute(attr_name)
        if value is None:
            raise Exception("Attr '{}' not found".format(attr_name))
        return value

    def input_value(self, element):
        """Return value of value attribute, usefull for inputs"""
        return self.attr(element, 'value')

    def clear(self, element):
        """Clear element text"""
        return element.clear()

    def css(self, element, prop_name):
        """Allows to obtain CSS value based on CSS property name"""
        return element.value_of_css_property(prop_name)

    def is_displayed(self, element):
        """Whether the element is visible to a user
            Webdriver spec to determine if element it's displayed:
            https://w3c.github.io/webdriver/webdriver-spec.html#widl-WebElement-isDisplayed-boolean
        """
        return element.is_displayed()

    def is_enabled(self, element):
        """Returns whether the element is enabled"""
        return element.is_enabled()

    def is_selected(self, element):
        """Returns whether the element is selected"""
        return element.is_selected()

    def attr_value(self, element, attr_name):
        """Search and attribute name over self.element and get value,
        if attr_value is obtained, then compare and raise if not
        Arguments:
            attr_name {str} -- find an attribute on WebElement
                with this name
        Returns:
            str -- value of html attr_name
        """
        return str(self.attr(element, attr_name))

    def get_text(self, element):
        """TODO: doc method"""
        if self.is_displayed(element):
            return str(element.text)
        else:
            return self.attr(element, 'innerText')

    def tag(self, element):
        """Returns element.tag_name value"""
        return element.tag_name
