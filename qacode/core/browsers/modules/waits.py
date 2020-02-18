# -*- coding: utf-8 -*-
"""TODO"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ModuleWaits(object):
    """TODO: doc class"""

    def __init__(self, driver_wait):
        """TODO: doc method"""
        self._driver_wait = driver_wait

    def ele_invisible(self, selector, locator=By.CSS_SELECTOR):
        """Wait for invisible element (display:none), returns element"""
        if selector is None:
            raise Exception("Not selector provided")
        expectation = EC.invisibility_of_element_located((locator, selector))
        return self._driver_wait.until(expectation)

    def ele_visible(self, element):
        """Wait for visible condition element, returns self"""
        if element is None:
            raise Exception("Not element provided")
        expectation = EC.visibility_of(element)
        return self._driver_wait.until(expectation)

    def ele_text(self, selector, text, locator=By.CSS_SELECTOR):
        """Wait if the given text is present in the specified element"""
        if selector is None:
            raise Exception("Not selector provided")
        expectation = EC.text_to_be_present_in_element(
            (locator, selector), text)
        return self._driver_wait.until(expectation)

    def ele_value(self, selector, value, locator=By.CSS_SELECTOR):
        """Wait if the given value is present in the specified element"""
        if selector is None:
            raise Exception("Not selector provided")
        expectation = EC.text_to_be_present_in_element_value(
            (locator, selector), value)
        return self._driver_wait.until(expectation)
