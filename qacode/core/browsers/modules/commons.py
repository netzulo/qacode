# -*- coding: utf-8 -*-
"""TODO"""


from selenium.common.exceptions import WebDriverException


class ModuleCommons(object):
    """TODO: doc class"""

    @classmethod
    def get_maximize_window(cls, driver):
        """Maximize browser window"""
        driver.maximize_window()

    @classmethod
    def get_title(cls, driver):
        """Obtains the title of the current page and return it"""
        return driver.title

    @classmethod
    def get_window_handle(cls, driver):
        """Get window object to handle with selenium on scripts"""
        return driver.current_window_handle

    @classmethod
    def get_capabilities(cls, driver):
        """Retrieve current capabilities applied to selenium driver"""
        return driver.desired_capabilities

    @classmethod
    def forward(cls, driver):
        """Go forward using browser functionality"""
        driver.forward()

    @classmethod
    def reload(cls, driver):
        """Go reload page using browser functionality"""
        driver.refresh()

    @classmethod
    def get_url(cls, driver, url, wait_for_load=0):
        """Do get_url including implicit wait for page load"""
        if wait_for_load > 0:
            driver.implicitly_wait(wait_for_load)
        driver.get(url)

    @classmethod
    def get_current_url(cls, driver):
        """Return current url from opened bot"""
        return driver.current_url

    @classmethod
    def is_url(cls, driver, url):
        """Check if url it's the same what selenium
            current and visible url
        """
        if cls.get_current_url(driver) != url:
            return False
        return True

    @classmethod
    def get_log(cls, driver, log_name='browser'):
        """Get selenium log by name, this depends of
            driver mode and browser what it's using each time
        """
        try:
            return {
                'browser': driver.get_log,
                'driver': driver.get_log,
                'client': driver.get_log,
                'server': driver.get_log,
            }[log_name](log_name)
        except (KeyError, WebDriverException) as err:
            if isinstance(err, KeyError):
                raise Exception("Can't use not valid value to get log")
            # self.log.debug(("nav | get_log: Selenium, not all drivers will"
            #                 " be handled by them with all optionsvalues"))
            # self.log.warning("nav | get_log: log_name={}, err={}".format(
            #     log_name, err.msg))
        return list()

    @classmethod
    def set_window_size(cls, driver, x=800, y=600):
        """Sets the width and height of the current
            window. (window.resizeTo)

        Keyword Arguments:
            x {int} -- width of new window size (default: {800})
            y {int} -- height of new window size (default: {600})
        """
        driver.set_window_size(x, y)
