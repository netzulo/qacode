# -*- coding: utf-8 -*-
"""TODO"""


from qacode.core.browsers.modules.module import Module
from selenium.common.exceptions import StaleElementReferenceException


class ModuleJs(Module):
    """TODO: doc class"""

    def __init__(self, driver):
        """TODO: doc method"""
        self._driver = driver

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

    def ele_is_staled(self, element):
        """Returns if an element is staled or not"""
        js_script = "return arguments[0].isConnected"
        try:
            return not self.execute_js(js_script, element)
        except StaleElementReferenceException:
            return True
