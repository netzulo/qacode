# -*- coding: utf-8 -*-
"""Base module for inherit new Test Suites"""


import time
from qacode.core.bots.bot_base import BotBase
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers.logger_manager import Log
from qatestlink.core.testlink_manager import TLManager


ASSERT_MSG_DEFAULT = "Fails at '{}': actual={}, expected={}"
ASSERT_REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501


class TestInfoBase(object):
    """Base class for inherit new Test classes"""

    is_loaded = False
    log = None
    config = None
    tlm = None  # Testlink Manager class

    @classmethod
    def load(cls, config):
        """Load default config dict"""
        if config is None and not cls.is_loaded:
            raise CoreException("Bad param 'config' provided")
        cls.add_property('config', value=config)
        if cls.log is None:
            config_bot = cls.config.get('bot')
            log_path = "{}/".format(
                config_bot.get('log_output_file'))
            log = Log(
                log_path=log_path,
                log_name=config_bot.get('log_name'),
                log_level=config_bot.get('log_level')
            )
            cls.add_property('log', log)
            tl_key = cls.config.get('testlink')
            if cls.tlm is None and tl_key is not None:
                cls.tlm = TLManager(settings=tl_key)
        cls.is_loaded = True

    @classmethod
    def bot_open(cls, config):
        """Open browser using BotBase instance

        Returns:
            BotBase -- wrapper browser handler for selenium
        """
        return BotBase(**config)

    @classmethod
    def bot_close(cls, bot):
        """Close bot calling bot.close() from param"""
        return bot.close()

    @classmethod
    def cfg_apps(cls):
        """Obtain inherit dict from 'cls.config' dict named
            'config.tests.apps'
        """
        if cls.config is None:
            raise CoreException("Call to cls.load() first")
        return cls.config.get('tests').get('apps')

    @classmethod
    def cfg_pages(cls):
        """Obtain inherit dict from 'cls.config' dict named
            'config.tests.apps[i].pages'
        """
        if cls.config is None:
            raise CoreException("Call to cls.load() first")
        pages = []
        for app in cls.cfg_apps():
            pages.extend(app.get('pages'))
        return pages

    @classmethod
    def cfg_controls(cls):
        """Obtain inherit dict from 'cls.config' dict named
            'config.tests.apps[i].pages[j].controls'
        """
        if cls.config is None:
            raise CoreException("Call to cls.load() first")
        controls = []
        for page in cls.cfg_pages():
            controls.extend(page.get('controls'))
        return controls

    @classmethod
    def cfg_app(cls, app_name):
        """Obtain inherit dict from 'cls.config' dict named
            'config.tests.apps' filtering by 'app_name' param
        """
        for app in cls.cfg_apps():
            if app.get('name') == app_name:
                return app
        raise Exception(
            "Not found for: app_name={}".format(
                app_name))

    @classmethod
    def cfg_page(cls, page_name, app_name=None):
        """Obtain inherit dict from 'cls.config' dict named
            'config.tests.apps[i].pages' filtering by 'page_name' param
        """
        apps = []
        if app_name is None:
            apps.extend(cls.cfg_apps())
        else:
            apps.append(cls.cfg_app(app_name))
        for app in apps:
            for page in app.get('pages'):
                if page.get('name') == page_name:
                    return page

    @classmethod
    def cfg_control(cls, control_name, page_name=None, app_name=None):
        """Obtain inherit dict from 'cls.config' dict named
            'config.tests.apps[i].pages[j].controls' filtering by
            'control_name' param
        """
        controls = []
        if page_name is None:
            controls.extend(cls.cfg_controls())
        else:
            controls.extend(cls.cfg_page(page_name, app_name=app_name))
        for control in controls:
            if control.get('name') == control_name:
                return control

    def setup_method(self, test_method, **kwargs):
        """Configure self.attribute"""
        self.load(kwargs.get('config'))
        self.log.info("Started testcase named='{}'".format(
            test_method.__name__))

    def teardown_method(self, test_method):
        """Unload self.attribute"""
        self.log.info("Finished testcase named='{}'".format(
            test_method.__name__))

    @classmethod
    def add_property(cls, name, value=None):
        """Add property to test instance using param 'name', will setup
            None if any value it's passed by param
        """
        setattr(cls, name, value)

    def timer(self, wait=5, print_each=5):
        """Timer to sleep browser on testcases

        Keyword Arguments:
            wait {int} -- seconds to wait (default: {5})
            print_each {int} -- print message each seconds, must be divisible
                by 5, negatives are accepted (default: {5})

        Raises:
            Exception -- [description]
        """
        msg_err = "Timer can't works if print_each param isn't divisible by 1"
        if (print_each % 1) != 0:
            raise Exception(msg_err)
        while wait > 0:
            self.sleep(print_each)
            wait -= print_each

    def sleep(self, wait=0):
        """Just call to native python time.sleep method

        Keyword Arguments:
            wait {int} -- Wait time on Runtime execution before execute
                next lane of code (default: {0})
        """
        if wait > 0:
            time.sleep(wait)


class TestInfoBot(TestInfoBase):
    """Inherit class what implements bot on each testcase"""

    bot = None

    def setup_method(self, test_method, **kwargs):
        """Configure self.attribute.
        If skipIf mark applied and True as first param for args tuple
            then not open bot
        """
        super(TestInfoBot, self).setup_method(test_method, **kwargs)
        if 'skipIf' in dir(test_method) and test_method.skipIf.args[0]:
            return False
        if not isinstance(self.bot, BotBase):
            self.add_property('bot', value=self.bot_open(self.config))

    def teardown_method(self, test_method, close=True):
        """Unload self.attribute, also close bot"""
        super(TestInfoBot, self).teardown_method(test_method)
        try:
            if close:
                self.bot_close(self.bot)
            else:
                self.log.debug(
                    "Not closing bot by optional param 'close'")
        except Exception as err:
            self.log.error(
                "Fails at try to close bot: {}".format(
                    err))


class TestInfoBotUnique(TestInfoBot):
    """Inherit class what implements bot on each testcase"""

    @classmethod
    def setup_class(cls, **kwargs):
        """Configure 'cls.attribute'. If name start with 'test_' and have
            decorator skipIf with value True, then not open bot
        """
        tests_methods = []
        skip_methods = []
        skip_force = kwargs.get('skip_force')
        for method_name in dir(cls):
            if method_name.startswith("test_"):
                method = getattr(cls, method_name)
                tests_methods.append(method)
                if 'skipIf' in dir(method) and method.skipIf.args[0]:
                    skip_methods.append(method)
        if tests_methods == skip_methods or skip_force:
            return False
        else:
            if not isinstance(cls.bot, BotBase):
                cls.load(kwargs.get('config'))
                cls.add_property(
                    'bot', value=cls.bot_open(cls.config))

    @classmethod
    def teardown_class(cls):
        """Unload self.attribute, closing bot from 'cls.bot' property"""
        if cls.bot:
            cls.bot_close(cls.bot)

    def teardown_method(self, test_method, close=False):
        """Unload self.attribute, also disable closing bot from TestInfoBot"""
        super(TestInfoBotUnique, self).teardown_method(
            test_method, close=close)
