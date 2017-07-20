import logging
from selenium import webdriver as WebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver import DesiredCapabilities

from qacode.core.bots.modules.NavBase import NavBase
from qacode.core.exceptions.CoreException import CoreException
from qacode.core.loggers.LoggerManager import LoggerManager

class BotBase(object):
    '''
    TODO: implement logger
    '''
    caps = None # Capabilities class
    currDriver = None # WebDriver class
    navs = None # bot methods
    options = None # bot options

    loggerManager = None # from options
    log = None # log

    def __init__(self, options):
        if options is None:
            raise Exception('[FAILED]', 'BotBase Options can\'t be none: bad BotOptions provided')
        else:
            try:
                self.options = options
                self.loggerManager = options.loggerManager
                self.log = self.loggerManager.get_log()
            except Exception as err:
                raise CoreException('BotBase, Error: at create LoggerManager', err)
            self.navs = NavBase(self)  # por implementar

            if self.options.botMode == 'local':
                self.modeLocal()
            elif self.options.botMode == 'remote':
                self.modeRemote()
            else:
                raise Exception('[FAILED]', 'options.mode unkown word | ' + self.options.mode)

    def modeLocal(self):
        self.log.debug('Starting browser with mode : LOCAL')
        if self.options.botBrowser == 'firefox':
            self.currCaps = DesiredCapabilities.FIREFOX.copy()
            # profile = WebDriver.FirefoxProfile.profile_dir = self.options.botProfilePath
            self.currDriver = WebDriver.Firefox(
                capabilities=self.currCaps,
                executable_path="{}/{}".format(self.options.botDriversPath, "geckodriver.exe")
                )

        elif self.options.botBrowser == 'chrome':
            self.currCaps = DesiredCapabilities.CHROME.copy()
            self.currDriver = WebDriver.Chrome(
                executable_path="{}/{}".format(self.options.botDriversPath, "chromedriver.exe"),
                desired_capabilities=self.currCaps)

        elif self.options.botBrowser == 'iexplorer':
            self.currCaps = DesiredCapabilities.INTERNETEXPLORER.copy()
            self.currDriver = WebDriver.Ie(
                executable_path="{}/{}".format(self.options.botDriversPath, "IEDriverServer_32.exe"),
                desired_capabilities=self.currCaps)

        elif self.options.botBrowser == 'edge':
            self.currCaps = DesiredCapabilities.EDGE.copy()
            self.currDriver = WebDriver.Edge(
                executable_path="{}/{}".format(self.options.botDriversPath, "EdgeDriver_64.exe"),
                desired_capabilities=self.currCaps)

        elif self.options.botBrowser == 'phantomjs':
            self.currCaps = DesiredCapabilities.PHANTOMJS.copy()
            self.currDriver = WebDriver.PhantomJS(
                executable_path="{}/{}".format(self.options.botDriversPath, "phantomjs.exe"),
                desired_capabilities=self.currCaps)
        else:
            raise Exception()
        self.log.debug('Started browser with mode : LOCAL OK')

    def modeRemote(self):
        '''
        WebDriver.Remote(
            command_executor,
            desired_capabilities,
            browser_profile,
            proxy,
            keep_alive,
            file_detector)
        '''
        self.log.debug('Starting browser with mode : REMOTE')
        if self.options.botBrowser == 'firefox':
            self.currCaps = DesiredCapabilities.FIREFOX.copy()
            #profile.accept_untrusted_certs = True
            #profile.update_preferences()

        elif self.options.botBrowser == 'chrome':
            self.currCaps = DesiredCapabilities.CHROME.copy()

        elif self.options.botBrowser == 'iexplorer':
            self.currCaps = DesiredCapabilities.INTERNETEXPLORER.copy()

        elif self.options.botBrowser == 'phantomjs':
            self.currCaps = DesiredCapabilities.PHANTOMJS.copy()

        elif self.options.botBrowser == 'edge':
            self.currCaps = DesiredCapabilities.EDGE.copy()

        else:
            raise Exception("Bad browser selected")
        #STARTs REMOTE
        self.currDriver = RemoteWebDriver(
            command_executor=self.options.botUrlHub,
            desired_capabilities=self.currCaps) # browser_profile=profile
        self.log.debug('Started browser with mode : REMOTE OK')

    def close(self):
        self.log.debug('Closing browser')
        self.currDriver.close()
        self.currDriver.quit()
        self.log.debug('Closed browser OK')
