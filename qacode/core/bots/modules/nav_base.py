# -*- coding: utf-8 -*-
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods

'''
Created on 04 march 2017

@author: ntz
'''


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from qacode.core.exceptions.core_exception import CoreException


class NavBase(object):
    '''
    Main navigation methods to use on selenium scripts
    + driver
    '''
    driver = None
    log = None

    def __init__(self, driver, log,driver_wait=None):
        '''
        Initialize self properties
        '''
        self.driver = driver
        self.log = log
        self.driver_wait = driver_wait

    def get_url(self, url, wait_for_load=0):
        """
        Do get_url including implicit wait for page load
        """
        if wait_for_load > 0:
            self.driver.implicitly_wait(wait_for_load)
        self.driver.get(url)

    def get_maximize_window(self):
        """
        Maximize browser window
        """
        self.driver.maximize_window()

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

    def execute_js(self, script, *args):
        """Execute arbitrary Javascript code
        
        Arguments:
            script {str} -- JS code to be executed on WebDriver
            *args {[type]} -- More arguments ( like element selector )

        Returns:
            str -- JS script returns
        """
        return self.driver.execute_script(script, *args)
    
    def set_css_rule(self, css_selector, css_prop, css_value, css_important=False, index=0):
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
        css_important_text = ''
        if css_important:
            css_important_text = '!important'
        css_rule = " {0!s} {{ {1!s} : {2!s} {3!s}; }}".format(
            css_selector,
            css_prop,
            css_value,
            css_important_text)
        js_script = "document.styleSheets[0].insertRule(\"{0!s}\", {1:d})".format(
            css_rule, index)
        return self.execute_js(js_script)

    def find_element(self, selector, locator=By.CSS_SELECTOR):
        """
        Just divided execution ways for search web element throught selenium
        """
        msg = 'Locator not selected at find_element, selector={}'.format(
            selector)
        msg_err = 'Error at find_element: selector={}'.format(
            selector)
        if locator is None:
            raise CoreException(message=msg)
        try:
            return self.driver.find_element(locator, selector)
        except NoSuchElementException as err:
            raise CoreException(err, message=msg_err)

    def find_elements(self, selector, locator=By.CSS_SELECTOR):
        """
        Just divided execution ways for search web elements throught selenium
        """
        msg = 'Locator not selected at find_element, selector={}'.format(
            selector)
        msg_err = 'Error at find_elements: selector={}'.format(
            selector)
        if locator is None:
            raise CoreException(message=msg)
        try:
            return self.driver.find_elements(locator, selector)
        except NoSuchElementException as err:
            raise CoreException(err, message=msg_err)

    def find_element_wait(self, selector,
                          locator=By.CSS_SELECTOR,
                          driver_wait=None):
        """
        Search element using WebDriverWait class
         and ElementConditions presence_of_element_located
        """
        if driver_wait is None and self.driver_wait is None:
            raise CoreException(message='Nav instanced without driver_wait')
        if driver_wait is None:
            driver_wait = self.driver_wait
        return driver_wait.until(
            EC.presence_of_element_located((locator, selector)))

    def forward(self):
        """Go forward using browser functionality"""
        self.driver.forward()

    def reload(self):
        """Go reload page using browser functionality"""
        self.driver.refresh()

    def get_log(self, log_name='browser'):
        """
        Get selenium log by name, valid values are
        default value : browser
          browser, driver, client, server
        """
        if log_name == 'browser':
            return self.driver.get_log(log_name)
        if log_name == 'driver':
            return self.driver.get_log(log_name)
        if log_name == 'client':
            return self.driver.get_log(log_name)
        if log_name == 'server':
            return self.driver.get_log(log_name)
        raise CoreException(
            'selenium log_name just can be: [browser,driver,client,server]')

    def get_screenshot_as_base64(self):
        """
        Gets the screenshot of the current window as a base64 encoded string
        which is useful in embedded images in HTML.
        """
        return self.driver.get_screenshot_as_base64()

    def get_screenshot_as_file(self, file_name):
        """
        Gets the screenshot of the current window. Returns False if there is
        any IOError, else returns True. Use full paths in your filename.
        TODO: support default name
        """
        self.driver.get_screenshot_as_file(file_name)

    def get_screenshot_as_png(self):
        """
        Gets the screenshot of the current window as a binary data.
        TODO: support default name
        """
        return self.driver.get_screenshot_as_png()

    def get_screenshot_save(self, file_name):
        """
        Gets the screenshot of the current window. Returns False if there is
        any IOError, else returns True. Use full paths in your filename.
        TODO: support default name
        """
        return self.driver.save_screenshot(file_name)

    def js_set_timeout(self, timeout=60):
        """
        Set the amount of time that the script should wait during an
        execute_async_script call before throwing an error.
        """
        self.driver.set_script_timeout(timeout)

    def set_window_size(self, pos_x=800, pos_y=600):
        """
        Sets the width and height of the current window. (window.resizeTo)
        """
        self.driver.set_window_size(pos_x, pos_y)

    def get_title(self):
        '''
        Returns the title of the current page.
        '''
        return self.driver.title

    def get_current_url(self):
        """Return current url from opened bot"""
        err_msg = "Failed at obtain selenium driver property 'current_url'"
        try:
            return self.driver.current_url
        except Exception as err:
            raise CoreException(err, message=err_msg)

    def is_url(self, url, ignore_raises=True):
        """
        Check if url it's the same what selenium current and visible url

        :Attributes:
            url: string value used to verify url
            ignore_raises: not raise exceptions if enabled
        """
        if self.get_current_url() != url:
            if not ignore_raises:
                raise CoreException("'Current url' is not 'param url'")
            return False
        return True

    def set_web_element(self, new_attr_id):
        """create_web_element"""
        self.driver.create_web_element(new_attr_id)

    def ele_click(self, element=None, selector=None, locator=By.CSS_SELECTOR):
        """
        Perform click webelement with locator param or search it by default
        CSS_SELECTOR value if element it's none but selector it's not default
        value
        """
        curr_ele = element
        curr_selector = selector
        can_click = False

        if curr_ele is None and curr_selector is None:
            raise CoreException(
                "Can't click over None element and None selector arguments: "
                "curr_ele={}, curr_selector={}"
                .format(curr_ele, curr_selector)
            )
        elif curr_ele is None:
            curr_ele = self.find_element(curr_selector, locator=locator)
            can_click = True
        elif curr_ele is not None and isinstance(curr_ele, WebElement):
            can_click = True
        if can_click:
            curr_ele.click()
        return curr_ele

    def ele_write(self, element, text=None):
        """
        Over element perform send_keys , if not sended text, then will write
        empty over element
        :param element: WebElement
        :return: None
        """
        if not isinstance(element, WebElement):
            raise CoreException(
                "Param 'locator' it's not instance of WebElement class")
        if text is not None:
            element.send_keys(text)
        else:
            # it's neccessary because some fields shows validation message and
            # color after try to send empty message
            element.send_keys()

    def ele_is_displayed(self, element):
        """Whether the element is visible to a user

        Webdriver spec to determine if element it's displayed: 
            https://w3c.github.io/webdriver/webdriver-spec.html#widl-WebElement-isDisplayed-boolean
        
        Arguments:
            element {WebElement} -- selenium web element
        
        Returns:
            bool -- Value based on selenium SPEC to determine if  an element is enabled
        """
        return element.is_displayed()

    def ele_is_enabled(self, element):
        """Returns whether the element is enabled
        
        Arguments:
            element {WebElement} -- selenium web element
        
        Returns:
            bool -- Value based on selenium SPEC to determine if  an element is enabled
        """
        return element.is_enabled()

    def ele_is_selected(self, element):
        """Returns whether the element is selected
        
        Arguments:
            element {WebElement} -- selenium web element
        
        Returns:
            bool -- Value based on selenium SPEC to determine if  an element is enabled
        """
        return element.is_selected()

    def ele_text(self, element, on_screen=True):
        """Get element content text.
            If the isDisplayed() method can sometimes trip over when
            the element is not really hidden but outside the viewport
            get_text() returns an empty string for such an element.
        
        Keyword Arguments:
            on_screen {bool} -- allow to obtain text if element
                it not displayed to this element before
                read text (default: {True})

        Returns:
            str -- Return element content text (innerText property)
        """
        if on_screen:
            text = element.text
        else:
            text = self.ele_attribute(element, 'innerText')[1]
            self.log.warning("text obtained from innerText")
            if self.ele_is_displayed(element):
                raise CoreException(
                    message="on_screen param must be"
                    "use when element it's not displayed")
        return text

    def ele_text_input(self, element):
        """Return value of value attribute, usefull for inputs"""
        return element.get_attribute('value')

    def ele_attribute(self, element, attr_name):
        """Returns tuple with (attr, value) if founds"""
        return (attr_name, element.get_attribute(attr_name))

    def ele_tag(self, element):
        """Returns element.tag_name value"""
        return element.tag_name

    def ele_clear(self, element):
        """Clear element text"""
        return element.clear()

    def ele_css(self, element, prop_name):
        """Allows to obtain CSS value based on CSS property name

        Arguments:
            element {WebElement} -- WebElement to modify CSS property
            prop_name {str} -- CSS property name

        Returns:
            str -- Value of CSS property searched
        """
        return element.value_of_css_property(prop_name)
