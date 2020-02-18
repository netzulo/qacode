# -*- coding: utf-8 -*-
"""TODO"""


class ModuleScreenshots(object):
    """TODO: doc class"""

    def __init__(self, driver):
        """TODO: doc method"""
        self._driver = driver

    def as_base64(self):
        """Gets the screenshot of the current window as a base64 encoded string
        which is useful in embedded images in HTML
        """
        return self._driver.get_screenshot_as_base64()

    def as_file(self, file_name):
        """Gets the screenshot of the current window. Returns False
            if there is any IOError, else returns True. Use full paths
            in your filename.

        Arguments:
            file_name {str} -- name of file path where
                want to save screenshot

        Returns:
            list(byte) -- file binary object of screenshot bytes
        """
        return self._driver.get_screenshot_as_file(file_name)

    def as_png(self):
        """Gets the screenshot of the current window as a
            binary data.

        Returns:
            File -- file binary object of screenshot with PNG format
        """
        return self._driver.get_screenshot_as_png()

    def save(self, file_name):
        """Gets the screenshot of the current window. Returns False
            if there is any IOError, else returns True.
            Use full paths in your filename.

        Arguments:
            file_name {str} -- name of file path where
                want to save screenshot

        Returns:
            list(byte) -- file binary object of screenshot bytes
        """
        return self._driver.save_screenshot(file_name)
