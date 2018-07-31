# -*- coding: utf-8 -*-
"""package module qacode.core.webs.pages.page_base"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.exceptions.page_exception import PageException
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_form import ControlForm
from qacode.core.webs.controls.control_group import ControlGroup

from selenium.webdriver.common.by import By


class PageBase(object):
    """
    Base class for all Inehrit Page classes wich need selenium functionality
    througth qacode bot
    """

    bot = None
    log = None
    settings = None

    def __init__(self, bot, **kwargs):
        """Instance of PageBase class

        Arguments:
            bot {BotBase} -- BotBase or inherit class instance

        Keyword Arguments:
            url {str} -- string for url of page
            locator {BY} -- strategy used to search all selectors
                passed, default value it's locator.CSS_SELECTOR
                (default: {BY.CSS_SELECTOR})
            go_url {bool} -- navigate to 'self.url' at instance
                (default: {False})
            wait_url {int} -- seconds to wait for 'self.url' load
                at instance (default: {0})
            maximize {bool} -- allow to maximize browser window
                before to load elements at instance (default: {False})
            controls {list(dict)} -- list of dicts with settings for each
                control which want to load

        Raises:
            PageException -- if required param 'bot' is None
            PageException -- if required param 'url' is None or empty str
        """
        if not bot:
            raise PageException(message="param bot is None")
        self.bot = bot
        if not isinstance(kwargs, dict):
            raise PageException(message='Optional params must be a dict')
        self.settings = kwargs
        if not self.settings.get('url'):
            raise PageException(
                message='Param url can\'t be None, just empty string')
        if not self.settings.get('locator'):
            self.settings.update({'locator': By.CSS_SELECTOR})
        if not self.settings.get('go_url'):
            self.settings.update({'go_url': False})
        if not self.settings.get('wait_url'):
            self.settings.update({'wait_url': 0})
        if not self.settings.get('maximize'):
            self.settings.update({'maximize': False})
        if not self.settings.get('controls'):
            self.settings.update({'controls': []})
        self._load()

    def _load(self, settings=None):
        """Loads page elements and maximize browser window"""
        # TODO: tests passed ?
        self.log = self.bot.log
        if not settings:
            settings = self.settings
        if settings.get('url'):
            self.url = settings.get('url')
        if settings.get('go_url'):
            self.go_url()
        if settings.get('maximize'):
            self.log.debug('page action: maximizing browser window')
            self.bot.navigation.get_maximize_window()
        if not settings.get('controls'):
            self.log.debug(
                'page action: empty list of controls for this page')
            return
        for cfg_control in settings.get('controls'):
            self.log.debug(
                ("page action: Loading element "
                 "as property name='{}'").format(cfg_control.get('name')))
            control = None
            instance = cfg_control.get('instance')
            # load default value
            if instance is None:
                instance = 'ControlBase'
            try:
                control = {
                    'ControlBase': ControlBase,
                    'ControlForm': ControlForm,
                    'ControlGroup': ControlGroup,
                }[instance](self.bot, **cfg_control)
            except KeyError:
                self.log.debug(("Bad instance name selected for "
                                "cfg_control={}").format(cfg_control))
                control = ControlBase(self.bot, **cfg_control)
            cfg_control.update({'instance': control})
            self._set_control(cfg_control)

    def _set_control(self, cfg_control):
        """Set control as property of PageBase instance

        Arguments:
            cfg_control {dict} -- config dictionary for manage WebElement

        Raises:
            PageException -- if param cfg_control is None
        """
        if not cfg_control:
            raise PageException(message='cfg_control can not be None')
        setattr(
            self,
            cfg_control.get('name'),
            cfg_control.get('instance'))

    def get_element(self, config_control):
        """Search element on Bot instance

        Arguments:
            config_controls {dict} -- base dict for ControlBase class

        Returns:
            ControlBase -- an element to be use
                throught selenium
        """
        return self.get_elements([config_control])[0]

    def get_elements(self, config_controls):
        """Search element on Bot instance, choose selector
            from instance or locator param

        Arguments:
            config_controls {dict} -- base dict for ControlBase class

        Returns:
            list(ControlBase) -- an element to be use as wrapper
                for selenium functionality
        """
        msg_notfound = "Page element not found: "
        "url={}, selector={}"
        controls = []
        for config_control in config_controls:
            instance = config_control.get("instance")
            control = None
            try:
                if isinstance(instance, (ControlBase, ControlForm)):
                    controls.append(control)
                else:
                    raise PageException(
                        message="Bad instance name for control")
            except (ControlException, Exception) as err:
                if not isinstance(err, ControlException):
                    raise Exception(err)
                self.log.warning(msg_notfound.format(
                    self.url,
                    config_control.get('selector')))
        return controls

    def go_url(self, url=None, wait_for_load=0):
        """Go to url, choose url from instance or locator params

        Keyword Arguments:
            url {str} -- string of FQDN, if None, load value from settings
                (default: {self.settings.get('url')})
            wait_for_load {int} -- [description] (default: {0})
        """
        if url is None:
            url = self.settings.get('url')
        self.log.debug('page action: navigate to url={}'.format(url))
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
            url = self.settings.get('url')
        try:
            return self.bot.navigation.is_url(url, ignore_raises=ignore_raises)
        except CoreException as err:
            raise PageException(err, "'Current url' is not 'page url'")

    def __repr__(self):
        """Show basic properties for this object"""
        return 'PageBase: url={}, bot.browser={}, bot.mode={}'.format(
            self.settings.get('url'),
            self.bot.settings.get('browser'),
            self.bot.settings.get('mode'))
