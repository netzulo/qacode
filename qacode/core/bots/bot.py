# -*- coding: utf-8 -*-
"""TODO"""


class Bot(object):
    """Class Base for handle selenium functionality throught this wrapper"""

    def __init__(self, **kwargs):
        """TODO: doc method"""
        self._browsers = []
        self._pages = []
        self._controls = []

    def browser(self, session_id):
        """TODO: doc method"""
        for browser in self.browsers:
            if browser.session_id == session_id:
                return browser
        raise Exception("browser not found")

    def page(self, url):
        """TODO: doc method"""
        for page in self.pages:
            if page.url == url:
                return page
        raise Exception("page not found")

    def control(self, selector):
        """TODO: doc method"""
        for control in self.controls:
            if control.selector == selector:
                return control
        raise Exception("control not found")

    @property
    def browsers(self):
        """TODO: doc method"""
        return self._browsers

    @browsers.setter
    def browsers(self, value):
        """TODO: doc method"""
        self._browsers = value
    
    @property
    def pages(self):
        """TODO: doc method"""
        return self._pages

    @pages.setter
    def pages(self, value):
        """TODO: doc method"""
        self._pages = value
    
    @property
    def controls(self):
        """TODO: doc method"""
        return self._controls

    @controls.setter
    def controls(self, value):
        """TODO: doc method"""
        self._controls = value
