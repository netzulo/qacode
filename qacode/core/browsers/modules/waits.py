# -*- coding: utf-8 -*-
"""TODO"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ModuleWaits(object):
    """TODO: doc class"""

    @staticmethod
    def ele_invisible(driver_wait, selector, locator=By.CSS_SELECTOR):
        """Wait for invisible element (display:none), returns element"""
        if selector is None:
            raise Exception("Not selector provided")
        expectation = EC.invisibility_of_element_located((locator, selector))
        return driver_wait.until(expectation)

    @staticmethod
    def ele_visible(driver_wait, element):
        """Wait for visible condition element, returns self"""
        if element is None:
            raise Exception("Not element provided")
        expectation = EC.visibility_of(element)
        return driver_wait.until(expectation)

    @staticmethod
    def ele_text(driver_wait, selector, text, locator=By.CSS_SELECTOR):
        """Wait if the given text is present in the specified element"""
        if selector is None:
            raise Exception("Not selector provided")
        expectation = EC.text_to_be_present_in_element(
            (locator, selector), text)
        return driver_wait.until(expectation)

    @staticmethod
    def ele_value(driver_wait, selector, value, locator=By.CSS_SELECTOR):
        """Wait if the given value is present in the specified element"""
        if selector is None:
            raise Exception("Not selector provided")
        expectation = EC.text_to_be_present_in_element_value(
            (locator, selector), value)
        return driver_wait.until(expectation)
