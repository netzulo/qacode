# -*- coding: utf-8 -*-
"""TODO"""


class ModuleScreenshots(object):
    """TODO: doc class"""

    @classmethod
    def get_screenshot_as_base64(cls, driver):
        """Gets the screenshot of the current window as a base64 encoded string
        which is useful in embedded images in HTML
        """
        return driver.get_screenshot_as_base64()

    @classmethod
    def get_screenshot_as_file(cls, driver, file_name):
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

    @classmethod
    def get_screenshot_as_png(cls, driver):
        """Gets the screenshot of the current window as a
            binary data.

        Returns:
            File -- file binary object of screenshot with PNG format
        """
        return driver.get_screenshot_as_png()

    @classmethod
    def get_screenshot_save(cls, driver, file_name):
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