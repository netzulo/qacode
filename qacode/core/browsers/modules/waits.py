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

    def ele_invisible(self, selector, locator=By.CSS_SELECTOR, timeout=None):
        """Wait for invisible element (display:none), returns element"""
        driver_wait = self._driver_wait
        self.__check_not_none__("selector", selector)
        if timeout:
            driver_wait = WebDriverWait(self._driver, timeout)
        expectation = EC.invisibility_of_element_located((locator, selector))
        return driver_wait.until(expectation)

    def ele_visible(self, element, timeout=None):
        """Wait for visible condition element, returns self"""
        driver_wait = self._driver_wait
        self.__check_not_none__("element", element)
        if timeout:
            driver_wait = WebDriverWait(self._driver, timeout)
        expectation = EC.visibility_of(element)
        return driver_wait.until(expectation)

    def ele_text(self, selector, text, locator=By.CSS_SELECTOR):
        """Wait if the given text is present in the specified element"""
        self.__check_not_none__("selector", selector)
        expectation = EC.text_to_be_present_in_element(
            (locator, selector), text)
        return self._driver_wait.until(expectation)

    def ele_value(self, selector, value, locator=By.CSS_SELECTOR):
        """Wait if the given value is present in the specified element"""
        self.__check_not_none__("selector", selector)
        expectation = EC.text_to_be_present_in_element_value(
            (locator, selector), value)
        return self._driver_wait.until(expectation)
