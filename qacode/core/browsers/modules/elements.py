# -*- coding: utf-8 -*-
"""TODO"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ModuleElements(object):
    """TODO: doc class"""

    def __init__(self, driver, driver_wait):
        """TODO: doc method"""
        self._driver = driver
        self._driver_wait = driver_wait

    def find(self, selector, locator=By.CSS_SELECTOR):
        """Just divided execution ways for search
            web element throught selenium
        """
        if locator is None:
            raise Exception("find: Locator can't be None")
        # Not found: NoSuchElementException, StaleElementReferenceException
        return self._driver.find_element(locator, selector)

    def finds(self, selector, locator=By.CSS_SELECTOR,
              raises_zero=True):
        """Just divided execution ways for search
            web elements throught selenium
        """
        if locator is None:
            raise Exception("finds: Locator can't be None")
        # Not found: NoSuchElementException, StaleElementReferenceException
        elements = self._driver.find_elements(locator, selector)
        if len(elements) == 0 and raises_zero:
            raise Exception("finds: 0 elements found")
        return elements

    def find_wait(self, selector, locator=By.CSS_SELECTOR):
        """Search element using WebDriverWait class
            and ElementConditions presence_of_element_located
        """
        if locator is None:
            raise Exception("find_wait: Locator can't be None")
        # Not found: NoSuchElementException, StaleElementReferenceException
        expectation = EC.presence_of_element_located((locator, selector))
        return self._driver_wait.until(expectation)

    def finds_wait(self, selector, locator=By.CSS_SELECTOR):
        """Search elements using WebDriverWait class
            and ElementConditions presence_of_all_elements_located
        """
        if locator is None:
            raise Exception("finds_wait: Locator can't be None")
        # Not found: NoSuchElementException, StaleElementReferenceException
        expectation = EC.presence_of_all_elements_located((locator, selector))
        return self._driver_wait.until(expectation)

    def find_child(self, element, child_selector, locator=By.CSS_SELECTOR):
        """TODO: doc method"""
        if locator is None:
            raise Exception("finds_wait: Locator can't be None")
        # Not found: NoSuchElementException, StaleElementReferenceException
        return element.find_element(locator, child_selector)

    def find_children(self, element, child_selector, locator=By.CSS_SELECTOR):
        """TODO: doc method"""
        if locator is None:
            raise Exception("finds_wait: Locator can't be None")
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

    def ele_click(self, element):
        """Perform click webelement with element

        Returns:
            WebElement -- returns element clicked (to allow chaining)
        """
        element.click()
        return element

    def ele_write(self, element, text=None):
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

    def ele_attribute(self, element, attr_name):
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

    def ele_input_value(self, element):
        """Return value of value attribute, usefull for inputs"""
        return self.ele_attribute(element, 'value')

    def ele_clear(self, element):
        """Clear element text"""
        return element.clear()

    def ele_css(self, element, prop_name):
        """Allows to obtain CSS value based on CSS property name"""
        return element.value_of_css_property(prop_name)
