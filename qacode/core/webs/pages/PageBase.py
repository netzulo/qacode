# -*- coding: utf-8 -*-
"""TODO"""


from selenium.webdriver.common.by import By
from qacode.core.exceptions.PageException import PageException
from qacode.core.webs.controls.ControlBase import ControlBase


class PageBase(object):
    """
    Base class for all Inehrit Page classes wich need selenium functionality
    througth qacode bot
    """

    bot = None
    url = None
    selectors = None
    go_url = None
    elements = []
    locator = None

    def __init__(self, bot, url, selectors=None, locator=By.CSS_SELECTOR,
                 go_url=True, maximize=False):
        """
        required:
          bot: BotBase or inherit class instance
          url: page url for class
        optionals:
          locator: strategy used to search all selectors passed,
              default value it's locator.CSS_SELECTOR
          selectors: list of CSS_SELECTOR strings to search elements
          go_url: go to url at instance page class locator default, can be disable
        """
        if bot is None:
            raise PageException(message="param bot is None")
        self.bot = bot
        if url is None:
            raise PageException(
                message='Param url can\'t be None or empty')
        self.url = url
        if locator is None:
            raise PageException(message='Param locator can\'t be None')
        self.selectors = selectors
        self.locator = locator
        if go_url is None:
            raise PageException(message='Param go_url can\'t be None')
        if maximize is None:
            raise PageException(message='Param maximize can\'t be None')
        self.go_url = go_url
        self.load_page(self.selectors, go_url=self.go_url, maximize=maximize)

    def load_page(self, selectors, go_url=True, maximize=True):
        """
        Loads page elements and maximize browser window
        """
        if go_url:
            self.go_page_url()
        if maximize:
            self.bot.log.debug('maximizing page window')
            self.bot.navigation.get_maximize_window()
        if selectors is not None:
            self.bot.log.debug('start to search page elements')
            self.elements = self.get_elements(as_controls=True)

    def get_elements(self, selectors=None, as_controls=False):
        """
        Search elements on Bot instance, choose selectors
          from instance or locator param
        """
        selectors_selected = None
        elements = []
        if selectors is None:
            selectors_selected = self.selectors
        else:
            selectors_selected = selectors
        for selector in selectors_selected:
            message_template = "Searching element: with selector={} locator={}"
            self.bot.log.debug(message_template.format(selector, self.locator))
            if as_controls:
                element = ControlBase(self.bot, selector, self.locator)
            else:
                element = self.bot.navigation.find_element(selector, self.locator)
            if element is None:
                self.bot.log.error(message_template.format(selector, self.locator))
            else:
                self.bot.log.debug("Element Found, adding to return method")
                elements.append(element)
        return elements

    def go_page_url(self, url=None, wait_for_load=0):
        """Go to url, choose url from instance or locator params"""
        if url is None:
            self.bot.log.debug('go to url={}'.format(self.url))
            self.bot.navigation.get_url(self.url, wait_for_load=wait_for_load)
        else:
            self.bot.log.debug('go to url={}'.format(url))
            self.bot.navigation.get_url(url, wait_for_load=wait_for_load)
