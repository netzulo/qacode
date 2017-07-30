'''
Created on 04 march 2017

@author: ntz
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from qacode.core.exceptions.CoreException import CoreException

class NavBase(object):
    '''
    Main navigation methods to use on selenium scripts
    + bot
    + driver
    '''
    bot = None
    driver = None

    def __init__(self, bot):
        '''
        Initialize self properties        
        '''
        self.bot = bot
        self.driver = self.bot.curr_driver

    def get_url(self, url):
        """
        Obtains url passed by param using selenium driver from bot class
        """
        self.driver.get(url)

    def get_url(self, url, wait_for_load=0):
        """
        Do get_url including implicit wait for page load
        """
        self.driver.implicitly_wait(wait_for_load)
        self.driver.get(url)

    def get_window_handle(self):
        """
        Get window object to handle with selenium on scripts
        """
        return self.driver.current_window_handle

    def delete_cookie_by_key(self, key_name):
        '''
        Deletes a single cookie with the given name.
        '''
        self.driver.delete_cookie(key_name)

    def delete_cookies(self):
        '''
        Delete all cookies in the scope of the session.
        '''
        self.driver.delete_all_cookies()

    def get_capabilities(self):
        """
        Retrieve current capabilities applied to selenium driver
        """
        return self.driver.desired_capabilities

    def execute_js(self, script, elements):
        self.driver.execute_script(script, elements)

    def find_element(self, selector, by=By.CSS_SELECTOR):
        '''
        Just divided execution ways for search web element throught selenium
        '''
        if by == By.CLASS_NAME:
            return self.driver.find_element_by_class_name(selector)
        elif by == By.CSS_SELECTOR:
            return self.driver.find_element_by_css_selector(selector)
        elif by == By.ID:
            return self.driver.find_element_by_id(selector)
        elif by == By.LINK_TEXT:
            return self.driver.find_element_by_link_text(selector)
        elif by == By.NAME:
            return self.driver.find_element_by_name(selector)
        elif by == By.PARTIAL_LINK_TEXT:
            return self.driver.find_element_by_partial_link_text(selector)
        elif by == By.TAG_NAME:
            return self.driver.find_element_by_tag_name(selector)
        elif by == By.XPATH:
            return self.driver.find_element_by_xpath(selector)

    def find_elements(self, selector, by=By.CSS_SELECTOR):
        '''
        Just divided execution ways for search web elements throught selenium
        '''
        if by == By.CLASS_NAME:
            return self.driver.find_elements_by_class_name(selector)
        elif by == By.CSS_SELECTOR:
            return self.driver.find_elements_by_css_selector(selector)
        elif by == By.ID:
            return self.driver.find_elements_by_id(selector)
        elif by == By.LINK_TEXT:
            return self.driver.find_elements_by_link_text(selector)
        elif by == By.NAME:
            return self.driver.find_elements_by_name(selector)
        elif by == By.PARTIAL_LINK_TEXT:
            return self.driver.find_elements_by_partial_link_text(selector)
        elif by == By.TAG_NAME:
            return self.driver.find_elements_by_tag_name(selector)
        elif by == By.XPATH:
            return self.driver.find_elements_by_xpath(selector)

    def forward(self):
        """
        Go forward using browser functionality
        """
        self.driver.forward()

    def reload(self):
        """
        Go reloa page using browser functionality
        """
        self.driver.refresh()

    def get_log(self, log_name='browser'):
        '''
        Get selenium log by name, valid values are
        + default value : browser
        + [browser,driver,client, server]        
        '''
        if log_name == 'browser':
            self.driver.get_log(log_name)
        if log_name == 'driver':
            self.driver.get_log(log_name)
        if log_name == 'client':
            self.driver.get_log(log_name)
        if log_name == 'server':
            self.driver.get_log(log_name)

    def get_screenshot_as_base64(self):
        '''
        Gets the screenshot of the current window as a base64 encoded string
        which is useful in embedded images in HTML.
        '''
        return self.driver.get_screenshot_as_base64()

    def get_screenshot_as_file(self, file_name):
        '''
        Gets the screenshot of the current window. Returns False if there is
        any IOError, else returns True. Use full paths in your filename.
        TODO: support default name
        '''
        self.driver.get_screenshot_as_file(file_name)

    def get_screenshot_as_png(self):
        '''
        Gets the screenshot of the current window as a binary data.
        TODO: support default name
        '''
        return self.driver.get_screenshot_as_png()

    def get_screenshot_save(self, file_name):
        '''
        Gets the screenshot of the current window. Returns False if there is
        any IOError, else returns True. Use full paths in your filename.
        TODO: support default name
        '''
        return self.driver.save_screenshot(file_name)

    def js_set_timeout(self, timeout=60):
        '''
        Set the amount of time that the script should wait during an
        execute_async_script call before throwing an error.
        '''
        self.driver.set_script_timeout(timeout)

    def set_window_size(self, x=800, y=600):
        '''
        Sets the width and height of the current window. (window.resizeTo)
        '''
        self.driver.set_window_size(x, y)

    def get_title(self):
        '''
        Returns the title of the current page.
        '''
        return self.driver.title

    def set_web_element(self, new_attr_id):
        '''
        create_web_element
        '''
        self.driver.create_web_element(new_attr_id)

    def ele_click(self, element=None, selector=None, by=By.CSS_SELECTOR):
        '''
        Perform click over webelement passed by param or search it by default CSS_SELECTOR value
        if element it's none but selector it's not default value
        '''
        curr_ele = element
        curr_selector = selector
        can_click = False

        if curr_ele is None and curr_selector is None :            
            raise CoreException("Can\'t click over None element and None selector arguments: curr_ele={}, curr_selector={}".format(curr_ele,curr_selector))
        elif curr_ele is None :
            curr_ele = self.find_element(curr_selector, by=by)                
            can_click = True
        elif curr_ele is not None and isinstance(curr_ele, WebElement):            
            can_click = True
        if can_click:
            curr_ele.click()
        return curr_ele


    def ele_write(self, element, text=None):
        '''
        Over element perform send_keys , if not sended text, then will write empty over element
        :param element: WebElement
        :return: None
        '''
        if not isinstance(element, WebElement):
            raise CoreException("Element passed by param it's not instance of WebElement class")
        if text is not None:
            element.send_keys(text)            
        else:
            # it's neccessary because some fields shows validation message and color after try to send empty message
            element.send_keys()

    def get_curr_url(self):
        '''
        Return current url from opened bot
        '''
        return self.driver.current_url
