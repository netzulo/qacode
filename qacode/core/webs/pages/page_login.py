# -*- coding: utf-8 -*-
# pylint: disable=too-many-arguments
"""Package qacode.core.webs.pages"""


from qacode.core.exceptions.page_exception import PageException
from qacode.core.webs.pages.page_base import PageBase
from selenium.webdriver.common.by import By


class PageLogin(PageBase):
    """Inherit PageBase class with login and valitation methods

        txt_username {WebElement} -- web element used as 'user name' input

        txt_password {WebElement} -- web element used as 'user password' input

        btn_login {WebElement} -- web element used as 'confirm login' button

        is_logged {bool} -- will be true after success call to method 'login'
    """

    url_logged = None
    txt_username = None
    txt_password = None
    btn_login = None

    is_logged = False

    def __init__(self, bot, url, url_logged, selectors=None,
                 locator=By.CSS_SELECTOR, go_url=True, maximize=False):
        """
        :Attributes:
            bot: BotBase or inherit classes instance
            url: page url value
            url_logged: page logged url value for login checks
        Optionals:
            selectors: a list of selectors ready to search elements
            locator: change default locator selector 'CSS_SELECTOR'
            go_url_maximize: change default page load,
             open browser maximized
        """
        super(PageLogin, self).__init__(
            bot, url, selectors, locator=locator,
            go_url=go_url, maximize=maximize)
        if selectors is None:
            raise PageException(message='Param selectors can\'t be None')
        if len(selectors) != 3:
            raise PageException(
                message='Can\'t instance PageLogin elements '
                'need at least 3 selectors'
            )
        if url_logged is None:
            raise PageException(message='Param url_logged can\'t be None')
        self.url_logged = url_logged
        self.txt_username = self.elements[0]
        self.txt_password = self.elements[1]
        self.btn_login = self.elements[2]

    def login(self, username, password, is_login_now=True):
        """
        Allows to do login on a page loaded throught selenium

        :Params:
            username: string used on web element 'txt_username'.
            password: string used on web element 'txt_password'.
            is_login_now: refer about it's clicking now
                          or just fill up form.
        """
        error_template = "Can't '{}' '{}' on field '{}' for class PageLogin"
        error_username = error_template.format(
            "send_keys", username, "txt_username")
        error_password = error_template.format(
            "send_keys", username, "txt_password")
        error_btn = error_template.format(
            "click", '', "btn_login")
        try:
            self.txt_username.type_text(username)
        except Exception as err:
            raise PageException(err=err, message=error_username)
        try:
            self.txt_password.type_text(password)
        except Exception as err:
            raise PageException(err=err, message=error_password)
        if is_login_now:
            try:
                self.btn_login.click()
            except Exception as err:
                raise PageException(err=err, message=error_btn)
        self.is_logged = self.is_url(self.url_logged)
