# -*- coding: utf-8 -*-
"""TODO"""


from qacode.core.browsers.modules.module import Module
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ModuleWaits(Module):
    """TODO: doc class"""

    def __init__(self, driver, driver_wait):
        """TODO: doc method"""
        self._driver = driver
        self._driver_wait = driver_wait

    def __driver_wait__(self, timeout=None):
        """TODO: doc method"""
        driver_wait = self._driver_wait
        if timeout:
            driver_wait = WebDriverWait(self._driver, timeout)
        return driver_wait

    def find_wait(self, selector, locator=By.CSS_SELECTOR, timeout=None):
        """Search element using WebDriverWait class
            and ElementConditions presence_of_element_located
        """
        self.__check_not_none__("locator", locator)
        # Not found: NoSuchElementException, StaleElementReferenceException
        expectation = EC.presence_of_element_located((locator, selector))
        return self.__driver_wait__(timeout=timeout).until(expectation)

    def finds_wait(self, selector, locator=By.CSS_SELECTOR, timeout=None):
        """Search elements using WebDriverWait class
            and ElementConditions presence_of_all_elements_located
        """
        self.__check_not_none__("locator", locator)
        # Not found: NoSuchElementException, StaleElementReferenceException
        expectation = EC.presence_of_all_elements_located((locator, selector))
        return self.__driver_wait__(timeout=timeout).until(expectation)

    def ele_invisible(self, selector, locator=By.CSS_SELECTOR, timeout=None):
        """Wait for invisible element (display:none), returns element"""
        self.__check_not_none__("selector", selector)
        expectation = EC.invisibility_of_element_located((locator, selector))
        return self.__driver_wait__(timeout=timeout).until(expectation)

    def ele_visible(self, element, timeout=None):
        """Wait for visible condition element, returns self"""
        self.__check_not_none__("element", element)
        expectation = EC.visibility_of(element)
        return self.__driver_wait__(timeout=timeout).until(expectation)

    def ele_text(self, selector, text, locator=By.CSS_SELECTOR, timeout=None):
        """Wait if the given text is present in the specified element"""
        self.__check_not_none__("selector", selector)
        expectation = EC.text_to_be_present_in_element(
            (locator, selector), text)
        return self.__driver_wait__(timeout=timeout).until(expectation)

    def ele_value(self, selector, value, locator=By.CSS_SELECTOR,
                  timeout=None):
        """Wait if the given value is present in the specified element"""
        self.__check_not_none__("selector", selector)
        expectation = EC.text_to_be_present_in_element_value(
            (locator, selector), value)
        return self.__driver_wait__(timeout=timeout).until(expectation)
