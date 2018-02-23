# -*- coding: utf-8 -*-
"""TODO"""


from qacode.core.exceptions.core_exception import CoreException
from qacode.core.exceptions.page_exception import PageException
from qacode.core.webs.controls.control_base import ControlBase
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

    def __init__(self, bot, url, selectors=None, locator=By.CSS_SELECTOR,
                 go_url=True, maximize=False):
        """
        :Args:
         required:
          bot: BotBase or inherit class instance
          url: page url for class, can be empty string
         optionals:
          locator: strategy used to search all selectors passed,
              default value it's locator.CSS_SELECTOR
          selectors: list of CSS_SELECTOR strings to search elements
          go_url: allow to disable go to url at instance page
            class locator default
        """
        if bot is None:
            raise PageException(message="param bot is None")
        self.bot = bot
        if url is None:
            raise PageException(
                message='Param url can\'t be None, just empty string')
        self.url = url
        if locator is None:
            raise PageException(message='Param locator can\'t be None')
        self.locator = locator
        if go_url is None:
            raise PageException(message='Param go_url can\'t be None')
        if maximize is None:
            raise PageException(message='Param maximize can\'t be None')
        self.go_url = go_url
        self._load_page(selectors, go_url=self.go_url, maximize=maximize)

    def _load_page(self, selectors, go_url=True, maximize=True):
        """Loads page elements and maximize browser window"""
        self.selectors = selectors
        if go_url:
            self.go_page_url()
        if maximize:
            self.bot.log.debug('maximizing page window')
            self.bot.navigation.get_maximize_window()
        if self.selectors is None:
            self.bot.log.debug(
                'Not searching elements if it\'s None')
        else:
            self.bot.log.debug(
                'Searching page elements with selectors')
            self.elements = self.get_elements(
                self.selectors, as_controls=True)

    def get_element(self, selector, as_control=False):
        """
        Search element on Bot instance, choose selector
          from instance or locator param
        :Args:
        :optionals:
            :selector:
                if not selector passed,
                then use instance property
            :as_control:
                if True, return
                ControlBase element loaded
                from selector
        """
        return self.get_elements([selector], as_controls=as_control)[0]

    def get_elements(self, selectors, as_controls=False):
        """
        Search elements on Bot instance, choose selectors
          from instance or locator param
        :Args:
        :optionals:
            :selectors:
                if not selectors passed,
                then use instance property
            :as_controls:
                if True, return list
                of ControlBase elements loaded
                from selectors
        """
        msg_page_element_notfound = "Page element not found: "
        "url={}, selector={}"
        elements = []
        if selectors is None:
            raise PageException(
                message='Can\'t use None selectors to get elements')
        for selector in list(selectors):
            self.bot.log.debug(
                "Searching element: with selector={} locator={}".format(
                    selector, self.locator))
            if as_controls:
                element = ControlBase(self.bot, selector, self.locator)
            else:
                try:
                    element = self.bot.navigation.find_element(
                        selector, self.locator)
                except CoreException:
                    raise PageException(
                        message=msg_page_element_notfound.format(
                            self.bot.navigation.get_current_url(),
                            selector))
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

    def is_url(self, url=None, ignore_raises=True):
        """Allows to check if current selenium visible url it's the same
            what self.url value

        :Attributes:
            url: default page url but can be string
                 value used to verify url
            ignore_raises: not raise exceptions if enabled
        """
        if url is None:
            url = self.url
        try:
            return self.bot.navigation.is_url(url, ignore_raises=ignore_raises)
        except CoreException as err:
            raise PageException(err, "'Current url' is not 'page url'")
