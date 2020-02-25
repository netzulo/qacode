# -*- coding: utf-8 -*-
"""Package module qacode.core.controls.control"""


from qacode.core.controls.control_config import ControlConfig


class Control(object):
    """This class allow to reference remote NodeElement (JS) or Html Tag to
        use checks , obtain information or handle actions using this instance.
        Wrapper for Selenium class named 'WebElement' using wrapper of
        WebDriver named qacode.core.bots.BotBase
    """

    def __init__(self, browser, **kwargs):
        """Initialize an instance of ControlBase"""
        self._browser = browser
        self._log = self._browser.log
        self._config = ControlConfig(**kwargs)
        self._element = None
        self._id = None
        if self._config.search:
            self.__search__()

    def __search__(self):
        """Element must be ensure it's ready before call this"""
        self._element = self._browser.elements.find(
            self._config.selector, locator=self._config.locator
        )
        self._id = self._element._id

    def __is_staled__(self):
        """TODO: doc method"""
        if not self._element:
            raise Exception("Not web element, search it first")
        return self._id != self._element._id

    def __check_element_ready__(self):
        """TODO: doc method"""
        if self.__is_staled__():
            raise Exception("Staled element, disappeared from the DOM")

    def attr(self, name):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.attr(self._element, name)

    def attr_value(self, name):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.attr_value(self._element, name)

    def css(self, name):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.css(self._element, name)

    def clear(self):
        """Clear input element text value"""
        self.__check_element_ready__()
        self._browser.elements.clear(self._element)

    def type_text(self, text, clear=False):
        """Type text on input element"""
        self.__check_element_ready__()
        if clear:
            self.clear()
        self._browser.elements.write(self._element, text)

    def click(self):
        """Click on element"""
        self.__check_element_ready__()
        self._browser.elements.click(self._element)

    def wait_invisible(self, timeout=1):
        """Wait for invisible element, chaining at returns"""
        self.__check_element_ready__()
        self._element = self._browser.waits.ele_invisible(
            self._config.selector,
            locator=self._config.locator,
            timeout=timeout)
        return self

    def wait_visible(self, timeout=1):
        """Wait for invisible element, chaining at returns"""
        self.__check_element_ready__()
        self._element = self._browser.waits.ele_visible(
            self._element,
            timeout=timeout)
        return self

    def wait_text(self, text, timeout=1):
        """Wait if the given text is present in the specified control"""
        self.__check_element_ready__()
        if self.tag == 'input':
            wait_method = self._browser.waits.ele_value
        else:
            wait_method = self._browser.waits.ele_text
        is_text = wait_method(
            self._config.selector,
            text,
            locator=self._config.locator,
            timeout=timeout)
        return is_text

    def wait_blink(self, to_visible=1, to_invisible=1):
        """Wait until control pops and dissapears"""
        return self.wait_visible(
            timeout=to_visible).wait_invisible(timeout=to_invisible)

    @property
    def config(self):
        """TODO: doc method"""
        return self._config

    @property
    def id(self):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._element._id

    @property
    def text(self):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.get_text(self._element)

    @property
    def tag(self):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.tag(self._element)

    @property
    def is_displayed(self):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.is_displayed(self._element)

    @property
    def is_enabled(self):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.is_enabled(self._element)

    @property
    def is_selected(self):
        """TODO: doc method"""
        self.__check_element_ready__()
        return self._browser.elements.is_selected(self._element)
