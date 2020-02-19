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
        if log_name not in ['browser', 'driver', 'client', 'server']:
            raise Exception("Can't use not valid value to get log")
        try:
            return self._driver.get_log(log_name)
        except WebDriverException:
            # silenced error because some browsers got
            # different errors when no logs or obtaining
            # server on local driver or client on remote driver
            return list()

    def set_window_size(self, x=800, y=600):
        """Sets the width and height of the current
            window. (window.resizeTo)

        Keyword Arguments:
            x {int} -- width of new window size (default: {800})
            y {int} -- height of new window size (default: {600})
        """
        self._driver.set_window_size(x, y)

    def execute_js(self, script, *args):
        """Execute arbitrary Javascript code
        Arguments:
            script {str} -- JS code to be executed on WebDriver
            *args {[type]} -- More arguments ( like element selector )
        Returns:
            str -- JS script returns
        """
        return self._driver.execute_script(script, *args)

    def set_css_rule(self, css_selector, css_prop, css_value, **kwargs):
        """Set new value for given CSS property name
        Arguments:
            css_selector {str} -- CSS selector to apply rule
            css_prop {str} -- CSS property to be applied to rule
            css_value {str} -- CSS property value to be applied to rule
        Keyword Arguments:
            css_important {bool} -- Allow to include '!important'
                to rule (default: {False})
            index {int} -- Position to insert new CSS rule
                on first stylesheet (default: {0})
        Returns:
            str -- JS script returns
        """
        css_important = kwargs.get("css_important") or False
        index = kwargs.get("index") or 0
        css_important_text = ''
        if css_important:
            css_important_text = '!important'
        css_rule = " {0!s} {{ {1!s} : {2!s} {3!s}; }}".format(
            css_selector,
            css_prop,
            css_value,
            css_important_text)
        js_script = "document.styleSheets[0].insertRule(\"{0!s}\", {1:d});".format(  # noqa: E501
            css_rule, index)
        return self.execute_js(js_script)
