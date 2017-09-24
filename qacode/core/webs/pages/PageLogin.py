from qacode.core.webs.pages.PageBase import PageBase
from qacode.core.exceptions.PageException import PageException
from selenium.webdriver.common.by import By

class PageLogin(PageBase):
    """Inherit PageBase class with login and valitation methods"""

    txt_username = None
    txt_password = None
    btn_login = None

    def __init__(self,bot, url, by=By.CSS_SELECTOR, selectors=[], go_url=True):
        super(PageLogin,self).__init__(bot, url, by ,selectors, go_url)
        if len(selectors) != 3:
            raise PageException("Can't instance PageLogin elements if not have 3 selectors")
        self.txt_username = self.elements[0]
        self.txt_password = self.elements[1]
        self.btn_login = self.elements[2]    

    def login(self,username,password,is_login_now=True):
        message_error = "Can't '{}' '{}' on field '{}' for class PageLogin"
        try:
            self.txt_username.send_keys(username)
        except Exception as err: 
            raise PageException(message_error.format("send_keys", username, "txt_username"))
        try:
           self.txt_password.send_keys(password)
        except Exception as err:
            raise PageException(message_error.format("send_keys", password, "txt_password"))
        if is_login_now:
            try:
               self.btn_login.click()
            except Exception as err:
               raise PageException(message_error.format("click", password, "btn_login"))