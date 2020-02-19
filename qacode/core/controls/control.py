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
        if self._config.search:
            self.__search__()

    def __search__(self):
        """Element must be ensure it's ready before call this"""
        self._element = self._browser.elements.find(
            self._config.selector, locator=self._config.locator
        )

    def __check_element_ready__(self):
        """TODO: doc method"""
        raise NotImplementedError("WIP")

    def attr(self, name):
        """TODO: doc method"""
        # self.__check_element_ready__()
        return self._browser.elements.ele_attr(self._element, name)

    def attr_value(self, name):
        """TODO: doc method"""
        # self.__check_element_ready__()
        return self._browser.elements.ele_attr_value(self._element, name)

    def css(self, name):
        """TODO: doc method"""
        return self._browser.elements.ele_css(self._element, name)

    def clear(self):
        """Clear input element text value"""
        # self.__check_element_ready__()
        self._browser.elements.ele_clear(self._element)

    def type_text(self, text, clear=False):
        """Type text on input element"""
        # self.__check_element_ready__()
        if clear:
            self.clear()
        self._browser.elements.ele_write(self._element, text)

    def click(self):
        """Click on element"""
        self.bot.navigation.ele_click(element=self.element)

    def wait_invisible(self, timeout=1):
        """Wait for invisible element, chaining at returns"""
        self.element = self._browser.waits.ele_invisible(
            self._config.selector,
            locator=self._config.locator,
            timeout=timeout)
        return self

    def wait_visible(self, timeout=1):
        """Wait for invisible element, chaining at returns"""
        self.element = self._browser.waits.ele_visible(
            self._config.selector,
            locator=self._config.locator,
            timeout=timeout)
        return self

    def wait_text(self):
        """TODO: doc method"""
        raise NotImplementedError("WIP")

    def wait_blink(self):
        """TODO: doc method"""
        raise NotImplementedError("WIP")

    @property
    def config(self):
        """TODO: doc method"""
        return self._config

    @property
    def text(self):
        """TODO: doc method"""
        # self.__check_element_ready__()
        return self._browser.waits.ele_text(self._element)

    @property
    def is_displayed(self):
        """TODO: doc method"""
        # self.__check_element_ready__()
        return self._browser.elements.ele_is_displayed(self._element)

    @property
    def is_enabled(self):
        """TODO: doc method"""
        # self.__check_element_ready__()
        return self._browser.elements.ele_is_enabled(self._element)

    @property
    def is_selected(self):
        """TODO: doc method"""
        # self.__check_element_ready__()
        return self._browser.elements.ele_is_selected(self._element)
