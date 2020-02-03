# -*- coding: utf-8 -*-
"""TODO"""


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class ModuleWaits(object):
    """TODO: doc class"""

    @staticmethod
    def ele_wait_invisible(driver, selector, locator=By.CSS_SELECTOR, timeout=0):
        """Wait for invisible element (display:none), returns element"""
        if selector is None:
            raise CoreException(
                "Can't wait invisible element if None selector given")
        locator_tuple = (locator, selector)
        driver_wait = WebDriverWait(driver, timeout)
        try:
            element = driver_wait.until(
                EC.invisibility_of_element_located(locator_tuple))
        except Exception:
            raise CoreException("Fails at wait for invisible element")
        return element

    @staticmethod
    def ele_wait_visible(driver, element, timeout=0):
        """Wait for visible condition element, returns self"""
        if element is None:
            raise CoreException("Can't wait visible if element is None")
        driver_wait = WebDriverWait(driver, timeout)
        try:
            element = driver_wait.until(EC.visibility_of(element))
        except Exception:
            raise CoreException("Fails at wait for visible element")
        return element

    @staticmethod
    def ele_wait_text(WebDriverWait, selector, text,
                      locator=By.CSS_SELECTOR, timeout=0):
        """Wait if the given text is present in the specified element"""
        locator_tuple = (locator, selector)
        driver_wait = WebDriverWait(driver, timeout)
        try:
            return driver_wait.until(
                EC.text_to_be_present_in_element(locator_tuple, text))
        except Exception:
            raise CoreException("Fails at wait for element text")

    @staticmethod
    def ele_wait_value(driver, selector, value,
                       locator=By.CSS_SELECTOR, timeout=0):
        """Wait if the given value is present in the specified element"""
        locator_tuple = (locator, selector)
        driver_wait = WebDriverWait(driver, timeout)
        try:
            return driver_wait.until(
                EC.text_to_be_present_in_element_value(locator_tuple, value))
        except Exception:
            raise CoreException("Fails at wait for element value")
