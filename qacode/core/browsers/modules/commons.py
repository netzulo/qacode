# -*- coding: utf-8 -*-
"""TODO"""


from selenium.common.exceptions import WebDriverException


class ModuleCommons(object):
    """TODO: doc class"""

    def __init__(self, driver):
        """TODO: doc method"""
        self._driver = driver

    def get_maximize_window(self):
        """Maximize browser window"""
        self._driver.maximize_window()

    def get_title(self):
        """Obtains the title of the current page and return it"""
        return self._driver.title

    def get_window_handle(self):
        """Get window object to handle with selenium on scripts"""
        return self._driver.current_window_handle

    def get_capabilities(self):
        """Retrieve current capabilities applied to selenium driver"""
        return self._driver.desired_capabilities

    def forward(self):
        """Go forward using browser functionality"""
        self._driver.forward()

    def reload(self):
        """Go reload page using browser functionality"""
        self._driver.refresh()

    def get_url(self, url, wait=0):
        """Do get_url including implicit wait for page load"""
        if wait > 0:
            self._driver.implicitly_wait(wait)
        self._driver.get(url)

    def get_current_url(self):
        """Return current url from opened bot"""
        return self._driver.current_url

    def is_url(self, url):
        """Check if url it's the same what selenium
            current and visible url
        """
        if self.get_current_url() != url:
            return False
        return True

    def get_log(self, log_name='browser'):
        """Get selenium log by name, this depends of
            driver mode and browser what it's using each time
        """
        try:
            return {
                'browser': self._driver.get_log,
                'driver': self._driver.get_log,
                'client': self._driver.get_log,
                'server': self._driver.get_log,
            }[log_name](log_name)
        except (KeyError, WebDriverException) as err:
            if isinstance(err, KeyError):
                raise Exception("Can't use not valid value to get log")
        return list()

    def set_window_size(self, x=800, y=600):
        """Sets the width and height of the current
            window. (window.resizeTo)

        Keyword Arguments:
            x {int} -- width of new window size (default: {800})
            y {int} -- height of new window size (default: {600})
        """
        self._driver.set_window_size(x, y)
