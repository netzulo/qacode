# -*- coding: utf-8 -*-
"""TODO"""


from qacode.core.exceptions.PageException import PageException
from selenium.webdriver.common.by import By


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

    def __init__(self, bot, url, by=By.CSS_SELECTOR, selectors=None,
                 go_url=True):
        """
        required:
          bot: BotBase or inherit class instance
          url: page url for class
        optionals:
          by: strategy used to search all selectors passed,
              default value it's By.CSS_SELECTOR
          selectors: list of CSS_SELECTOR strings to search elements
          go_url: go to url at instance page class by default, can be disable
        """
        if bot is None:
            raise PageException("param bot is None")
        self.bot = bot
        if url is None:
            raise PageException(
                message='Param url can\'t be None or empty')
        self.url = url
        if by is None:
            raise PageException(message='Param by can\'t be None')
        self.locator = by
        self.selectors = selectors
        if go_url is None:
            raise PageException(message='Param go_url can\'t be None')
        self.go_url = go_url
        if self.go_url:
            self.go_page_url()

        if self.selectors is not None:
            self.elements = self.get_elements()

    def get_elements(self, selectors=None):
        """
        Search elements on Bot instance, choose selectors
          from instance or by param
        """
        searchs = None
        elements = []
        if selectors is None:
            searchs = self.selectors
        else:
            searchs = selectors
        for selector in searchs:
            message_template = "Searching element: with selector={} by={}"
            self.bot.log.debug(message_template.format(selector, self.locator))
            element = self.bot.navigation.find_element(selector, self.locator)
            if element is None:
                self.bot.log.error(message_template.format(selector, self.locator))
            else:
                self.bot.log.debug("Element Found, adding to return method")
                elements.append(element)
        return elements

    def go_page_url(self, url=None, wait_for_load=0):
        """Go to url, choose url from instance or by params"""
        if url is None:
            self.bot.navigation.get_url(self.url, wait_for_load=wait_for_load)
        else:
            self.bot.navigation.get_url(url, wait_for_load=wait_for_load)
