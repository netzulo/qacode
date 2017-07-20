'''
Created on 04 march 2017

@author: ntz
'''
from selenium.webdriver.common.by import By
from qacode.core.exceptions.CoreException import CoreException

class NavBase(object):
    '''
    classdocs
    '''

    def __init__(self, bot):
        '''
        Constructor
        '''
        self.bot = bot

    def goUrl(self, url):
        self.bot.currDriver.get(url)

    def goUrl(self, url, waitForLoad=0):
        self.bot.currDriver.implicitly_wait(waitForLoad)
        self.bot.currDriver.get(url)

    def getCurrentUrl(self):
        return self.bot.currDriver.current_url

    def getWindowHandle(self):
        return self.bot.currDriver.current_window_handle

    def deleteCookie(self, keyName):
        '''
        Deletes a single cookie with the given name.
        '''
        self.bot.currDriver.delete_cookie(keyName)

    def deleteCookies(self):
        '''
        Delete all cookies in the scope of the session.
        '''
        self.bot.currDriver.delete_all_cookies()

    def getCurrentCapabilities(self):
        return self.bot.currDriver.desired_capabilities

    def execJs(self, script, webElements):
        self.bot.currDriver.execute_script(script, webElements)
    def findElement(self, selector, by=By.CSS_SELECTOR):
        '''
        Just divided execution ways for the future
        '''
        if by == By.CLASS_NAME:
            return self.bot.currDriver.find_element_by_class_name(selector)
        elif by == By.CSS_SELECTOR:
            return self.bot.currDriver.find_element_by_css_selector(selector)
        elif by == By.ID:
            return self.bot.currDriver.find_element_by_id(selector)
        elif by == By.LINK_TEXT:
            return self.bot.currDriver.find_element_by_link_text(selector)
        elif by == By.NAME:
            return self.bot.currDriver.find_element_by_name(selector)
        elif by == By.PARTIAL_LINK_TEXT:
            return self.bot.currDriver.find_element_by_partial_link_text(selector)
        elif by == By.TAG_NAME:
            return self.bot.currDriver.find_element_by_tag_name(selector)
        elif by == By.XPATH:
            return self.bot.currDriver.find_element_by_xpath(selector)

    def forward(self):
        self.bot.currDriver.forward()

    def reload(self):
        self.bot.currDriver.refresh()

    def getLog(self, logName='browser'):
        '''
        Just divided execution ways for the future
        '''
        if logName == 'browser':
            self.bot.currDriver.get_log(logName)
        if logName == 'driver':
            self.bot.currDriver.get_log(logName)
        if logName == 'client':
            self.bot.currDriver.get_log(logName)
        if logName == 'server':
            self.bot.currDriver.get_log(logName)

    def getScreenshotAsBase64(self):
        '''
        Gets the screenshot of the current window as a base64 encoded string
        which is useful in embedded images in HTML.
        '''
        return self.bot.currDriver.get_screenshot_as_base64()
    def getScreenshotAsFile(self, fileName):
        '''
        Gets the screenshot of the current window. Returns False if there is
        any IOError, else returns True. Use full paths in your filename.
        '''
        self.bot.currDriver.get_screenshot_as_file(fileName)

    def getScreenshotAsPngBin(self, fileName):
        '''
        Gets the screenshot of the current window as a binary data.
        '''
        return self.bot.currDriver.get_screenshot_as_png()

    def getScreenshotSave(self, fileName):
        '''
        Gets the screenshot of the current window. Returns False if there is
        any IOError, else returns True. Use full paths in your filename.
        '''
        self.bot.currDriver.save_screenshot(fileName)

    def setJsAsynTimeout(self, timeOut=60):
        '''
        Set the amount of time that the script should wait during an
        execute_async_script call before throwing an error.
        '''
        self.bot.currDriver.set_script_timeout(timeOut)

    def setWindowSize(self, x=800, y=600):
        '''
        Sets the width and height of the current window. (window.resizeTo)
        '''
        self.bot.currDriver.set_window_size(x, y)

    def getTitle(self):
        '''
        Returns the title of the current page.
        '''
        return self.bot.currDriver.title

    def setWebElement(self, attrId):
        '''
        create_web_element
        '''
        self.bot.currDriver.create_web_element(attrId)
    def eleClick(self, element=None, selector=None):
        '''
        Over element perform web click

        if all params are None, then will raise
        if Element is not None,then will use element to perform action
        if Element is None, then will try to use selector search
            if selector is None , then will raise
            if selector is not None, then will search element to perform action
        :param element: WebElement
        :return: element used to click
        '''
        currEle = None

        if element is None and selector is None :
            raise CoreException('Can\'t click over None element and selector arguments')
        else:
            if element is not None :
                currEle = element
                element.click()
                print("Selector it's ignored: {}".format(selector))
            else:
                if selector is None:
                    raise CoreException('Can\'t click over None element and selector arguments')
                else:
                    currEle = self.findElement(selector, by=By.CSS_SELECTOR)
                    currEle.click()
        return currEle


    def eleWrite(self, element, text=None):
        '''
        Over element perform send_keys , if not sended text, then will write empty over element
        :param element: WebElement
        :return: None
        '''
        if text is None :
            element.send_keys()
        else:
            element.send_keys(text)

    def getCurrUrl(self):
        '''
        Return current url from opened bot
        '''
        return self.bot.currDriver.current_url
