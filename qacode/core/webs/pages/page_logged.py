# -*- coding: utf-8 -*-
# pylint: disable=too-many-arguments
"""Package qacode.core.webs.pages"""


from selenium.webdriver.common.by import By
from qacode.core.webs.pages.page_base import PageBase
from qacode.core.webs.pages.page_login import PageLogin
from qacode.core.exceptions.page_exception import PageException


class PageLogged(PageBase):
    """
    Inherit PageBase class with logout button
     and session check methods
    """

    url_logout = None
    btn_logout = None

    def __init__(self, bot, url, url_logout, selectors=None, locator=By.CSS_SELECTOR,
                 go_url=True, maximize=False):
        """
        :Attributes:
            bot: BotBase or inherit classes instance
            url: page url value
            url_logout: page logout url value for logout checks
        Optionals:
            selectors: a list of selectors ready to search elements
            locator: change default locator selector 'CSS_SELECTOR'
            go_url_maximize: change default page load,
             open browser maximized
        """
        super(PageLogged, self).__init__(
            bot, url, selectors, locator=locator,
            go_url=go_url, maximize=maximize)
        if selectors is None:
            raise PageException(message='Param selectors can\'t be None')
        if len(selectors) != 1:
            raise PageException(
                message='Can\'t instance PageLogin elements '
                'need at least 1 selector'
            )
        if url_logout is None:
            raise PageException(message='Param url_logout can\'t be None')
        self.url_logout = url_logout
        self.btn_logout = self.elements[0]

    def logout(self):
        """Allows to do logout on a logged web page using button click"""
        self.btn_logout.click()
        is_url_logout = self.is_url(url=self.url_logout)
        if not is_url_logout:
            raise PageException('logout failed after click')
        return True

    def is_logged(self, page_login):
        """Returns is_logged property from PageLogin instance"""
        if not isinstance(page_login, PageLogin):
            raise PageException(
                "param page_login must be instance of PageLogin class")
        return page_login.is_logged
