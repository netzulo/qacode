from qacode.core.exceptions.PageException import PageException
from selenium.webdriver.common.by import By

class PageBase(object):
    """Base class for all Inehrit Page classes wich need selenium functionality througth qacode bot"""
    
    bot = None
    url = None
    selectors = None
    go_url = None
    elements = []

    def __init__(self,bot, url, by=By.CSS_SELECTOR, selectors=[], go_url=True):
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
        if url is None or len(url) <= 0:
            raise PageException("param url is None or len <= 0")
        self.url = url                
        if by is None :            
            self.by = By.CSS_SELECTOR
        else:
            self.by = by           
        if selectors is None:
            raise PageException("param selectors is None")
        self.selectors = selectors
        if go_url is None:
            raise PageException("param go_url is None")
        self.go_url = go_url
        #more logic
        if go_url:
            self.go_page_url()
        if len(selectors) > 0:
            self.elements = self.get_elements()

    def get_elements(self, selectors=[]):
        searchs = None
        elements = []
        if len(selectors) <= 0:            
            searchs = self.selectors
        else:
            searchs = selectors        
        for selector in searchs:
            message_template = "Searching element: by={} with selector={}"
            self.bot.log.debug(message_template.format(self.by,selector))
            element = self.bot.navigation.find_element(selector,self.by)
            if element is None:
                self.bot.log.error(message_template.format(self.by,selector))
            else:
                self.bot.log.debug("Element Found, adding to return method")
                elements.append(element)
        return elements

    def go_page_url(self, url=None, wait_for_load=0):
        if url is None:
            self.bot.navigation.get_url(self.url, wait_for_load=wait_for_load)
        else:            
            self.bot.navigation.get_url(url, wait_for_load=wait_for_load)
