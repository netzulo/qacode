# -*- coding: utf-8 -*-
"""TODO"""


class ModuleCommons(object):
    """TODO: doc class"""

    @staticmethod
    def get_title(driver):
        """Obtains the title of the current page and return it"""
        return driver.title

    @staticmethod
    def get_url(driver, url, wait_for_load=0):
        """Do get_url including implicit wait for page load"""
        if wait_for_load > 0:
            driver.implicitly_wait(wait_for_load)
        driver.get(url)

    def get_current_url(driver):
        """Return current url from opened bot"""
        return driver.current_url
    
    def is_url(driver, url, ignore_raises=True):
        """Check if url it's the same what selenium
            current and visible url
        """
        if driver.get_current_url(driver) != url:
            if not ignore_raises:
                raise CoreException("'Current url' is not 'param url'")
            return False
        return True

    @staticmethod
    def get_maximize_window(driver):
        """Maximize browser window"""
        driver.maximize_window()

    @staticmethod
    def get_window_handle(driver):
        """Get window object to handle with selenium on scripts"""
        return driver.current_window_handle

    @staticmethod
    def get_capabilities(driver):
        """Retrieve current capabilities applied to selenium driver"""
        return driver.desired_capabilities
    
    @staticmethod
    def forward(driver):
        """Go forward using browser functionality"""
        driver.forward()

    @staticmethod
    def reload(self):
        """Go reload page using browser functionality"""
        driver.refresh()

    @staticmethod
    def get_log(self, log_name='browser', raises=False):
        """Get selenium log by name, this depends of
            driver mode and browser what it's using each time
        """
        method = self.method_name()
        try:
            return {
                'browser': self.driver.get_log,
                'driver': self.driver.get_log,
                'client': self.driver.get_log,
                'server': self.driver.get_log,
            }[log_name](log_name)
        except (KeyError, WebDriverException) as err:
            if isinstance(err, KeyError):
                raise CoreException(
                    "Can't use not valid value to get log",
                    info_bot={"err": err, "method": method})
            self.log.debug(("nav | get_log: Selenium, not all drivers will"
                            " be handled by them with all optionsvalues"))
            self.log.warning("nav | get_log: log_name={}, err={}".format(
                log_name, err.msg))
        return list()

    @staticmethod
    def get_screenshot_as_base64(driver):
        """Gets the screenshot of the current window as a base64 encoded string
        which is useful in embedded images in HTML
        """
        return driver.get_screenshot_as_base64()

    @staticmethod
    def get_screenshot_as_file(driver, file_name):
        """Gets the screenshot of the current window. Returns False
            if there is any IOError, else returns True. Use full paths
            in your filename.

        Arguments:
            file_name {str} -- name of file path where
                want to save screenshot

        Returns:
            list(byte) -- file binary object of screenshot bytes
        """
        return driver.get_screenshot_as_file(file_name)

    @staticmethod
    def get_screenshot_as_png(driver):
        """Gets the screenshot of the current window as a
            binary data.

        Returns:
            File -- file binary object of screenshot with PNG format
        """
        return driver.get_screenshot_as_png()

    @staticmethod
    def get_screenshot_save(driver, file_name):
        """Gets the screenshot of the current window. Returns False
            if there is any IOError, else returns True.
            Use full paths in your filename.

        Arguments:
            file_name {str} -- name of file path where
                want to save screenshot

        Returns:
            list(byte) -- file binary object of screenshot bytes
        """
        return driver.save_screenshot(file_name)

    @staticmethod
    def set_window_size(driver, pos_x=800, pos_y=600): # YES
        """Sets the width and height of the current
            window. (window.resizeTo)

        Keyword Arguments:
            pos_x {int} -- width of new window size (default: {800})
            pos_y {int} -- height of new window size (default: {600})
        """
        driver.set_window_size(pos_x, pos_y)
