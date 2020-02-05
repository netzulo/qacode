# -*- coding: utf-8 -*-
"""TODO"""


from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class ModuleElements(object):
    """TODO: doc class"""

    @classmethod
    def find_element(cls, driver, selector, locator=By.CSS_SELECTOR):
        """Just divided execution ways for search
            web element throught selenium
        """
        if locator is None:
            raise Exception("find_element: Locator can't be None")
        try:
            return driver.find_element(locator, selector)
        except NoSuchElementException:
            raise Exception("find_element: Element not found")

    @classmethod
    def find_elements(cls, driver, selector, locator=By.CSS_SELECTOR,
                      raises_zero=True):
        """Just divided execution ways for search
            web elements throught selenium
        """
        if locator is None:
            raise Exception("find_elements: Locator can't be None")
        try:
            elements = driver.find_elements(locator, selector)
            if len(elements) == 0 and raises_zero:
                raise Exception("find_elements: 0 elements found")
            return elements
        except NoSuchElementException:
            raise Exception("find_elements: Element not found")

    @classmethod
    def find_element_wait(cls, driver_wait, selector,
                          locator=By.CSS_SELECTOR):
        """Search element using WebDriverWait class
            and ElementConditions presence_of_element_located
        """
        try:
            return driver_wait.until(
                EC.presence_of_element_located((locator, selector)))
        except (NoSuchElementException, StaleElementReferenceException):
            return driver_wait.until(
                EC.visibility_of_element_located((locator, selector)))

    @classmethod
    def find_elements_wait(cls, driver_wait, selector,
                           locator=By.CSS_SELECTOR):
        """Search elements using WebDriverWait class
            and ElementConditions presence_of_all_elements_located
        """
        try:
            return driver_wait.until(
                EC.presence_of_all_elements_located((locator, selector)))
        except (NoSuchElementException, StaleElementReferenceException):
            return driver_wait.until(
                EC.visibility_of_all_elements_located((locator, selector)))

    @classmethod
    def find_element_child(cls, driver, element, child_selector,
                           locator=By.CSS_SELECTOR):
        """TODO: doc method"""
        if element is None or not isinstance(element, WebElement):
            raise Exception("Cant find child if not element")
        try:
            return element.find_element(locator, child_selector)
        except (NoSuchElementException, StaleElementReferenceException) as err:
            # at Java lang exist 1 expected condition
            # named : visibilityOfNestedElementsLocatedBy
            # doc : https://selenium-python.readthedocs.io/waits.html
            # maybe must exist at python too
            # then, create and use new method named: find_element_child_wait()
            # raise NotImplementedError("TODO:open an issue at github please")
            raise Exception(err)

    @classmethod
    def find_element_children(cls, driver, element, child_selector,
                              locator=By.CSS_SELECTOR):
        """TODO: doc method"""
        if element is None or not isinstance(element, WebElement):
            raise Exception("Cant find children if not element found")
        try:
            return element.find_elements(locator, child_selector)
        except (NoSuchElementException, StaleElementReferenceException) as err:
            # at Java lang exist 1 expected condition
            # named : visibilityOfNestedElementsLocatedBy
            # doc : https://selenium-python.readthedocs.io/waits.html
            # maybe must exist at python too
            # then, create and use new method named: find_element_child_wait()
            # raise NotImplementedError("TODO:open an issue at github please")
            raise Exception(err)

    @classmethod
    def find_elements_child(cls):
        """TODO: doc method"""
        raise NotImplementedError("TODO: open an issue at github please")

    @classmethod
    def find_elements_children(cls):
        """TODO: doc method"""
        raise NotImplementedError("TODO: open an issue at github please")

    @classmethod
    def ele_click(cls, element):
        """Perform click webelement with element

        Returns:
            WebElement -- returns element clicked (to allow chaining)
        """
        element.click()
        return element

    @classmethod
    def ele_write(cls, element, text=None):
        """Over element perform send_keys , if not sended will
            write empty over element
        """
        if not isinstance(element, WebElement):
            raise Exception("Param 'element' it's not WebElement")
        if text is not None:
            element.send_keys(text)
        else:
            # it's neccessary because some fields shows validation message and
            # color after try to send empty message
            element.send_keys()

    @classmethod
    def ele_attribute(cls, element, attr_name):
        """Returns tuple with (attr, value) if founds
            This method will first try to return the value of a property with
            the given name. If a property with that name doesn't exist, it
            returns the value of the attribute with the same name. If there's
            no attribute with that name, None is returned.
        """
        value = str(element.get_attribute(attr_name))
        if value is None or value == attr_name:
            raise Exception("Attr '{}' not found".format(attr_name))
        return value

    @classmethod
    def ele_input_value(cls, element):
        """Return value of value attribute, usefull for inputs"""
        return cls.ele_attribute(element, 'value')

    @classmethod
    def ele_clear(cls, element):
        """Clear element text"""
        return element.clear()

    @classmethod
    def ele_css(cls, element, prop_name):
        """Allows to obtain CSS value based on CSS property name"""
        return element.value_of_css_property(prop_name)
