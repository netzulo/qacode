Usage Guide
===========

Bots
----

Have classes for this down package: ``qacode.core.bots``


.. code:: python


    from qautils.files import settings
    from qacode.core.bots import BotBase
    # SETTINGS = settings()
    SETTINGS = {
        "bot": {
            "log_output_file": "logs/",
            "log_name": "qacode",
            "log_level": "DEBUG"
            "mode": "remote",
            "browser": "chrome",
            "options": { "headless": false },
            "url_hub": "http://qalab.tk:11000/wd/hub",
            "drivers_path": "../qadrivers",
            "drivers_names": [
                "chromedriver_32.exe",
                "chromedriver_64.exe",
                "chromedriver_32",
                "chromedriver_64",
                "firefoxdriver_32.exe",
                "firefoxdriver_64.exe",
                "firefoxdriver_64.exe",
                "firefoxdriver_32",
                "phantomjsdriver_32.exe",
                "phantomjsdriver_64.exe",
                "phantomjsdriver_32",
                "phantomjsdriver_64",
                "iexplorerdriver_32.exe",
                "iexplorerdriver_64.exe",
                "edgedriver_32.exe",
                "edgedriver_64.exe",
                "operadriver_32.exe",
                "operadriver_64.exe",
                "operadriver_32",
                "operadriver_64"
            ]
        }
    }
    # Open bot now
    bot = BotBase(**SETTINGS)

Controls
--------

Have classes for this down package: `qacode.core.bots.webs.controls`

ControlBase
~~~~~~~~~~~

It's base control to load web element from ``WebDriver + browser session`` , *this class must be use to inherit new* `ControlAwesome` *classes*

+ Param **selector** (**REQUIRED**): Valid selector for locator selected
+ Param **name** : Allows to set value to ``ControlBase.name`` property, also it's used by pages to set property page with ``control.name`` value
+ Param **locator** : This text it's parsed down selenium class ``selenium.webdriver.common.by.By`` (*default:* ``css selector`` == ``By.CSS_SELECTOR``)
+ Param **instance** : Allow to generate your own inherit classes from ``ControlBase`` and instance them  using qacode strategy (*default:* ``ControlBase``)
+ Param **auto_reload** : Allow to reload element searching first when need to use some function of control instance and isn't loaded (*default:* ``True``)
+ Param **on_instance_search** : enable searching element at instance `ControlBase` (*default:* `False`)
+ Param **on_instance_load** : enable loading ``ControlBase`` properties when element it's loaded (*default:* ``False``) , will need enabled if want to access to base properties values obtained from selenium methods at ``BotBase.navigation``

Example of usage
^^^^^^^^^^^^^^^^

.. code:: python


    from qautils.files import settings
    from qacode.core.bots import BotBase

    # Load settings for bot and controls
    SETTINGS = settings()
    CONTROLS = [
        {
          "name": "txt_username", "selector": "#username"
        },
        {
          "name": "txt_password", "selector": "#password"
        },
        {
          "name": "btn_submit",
          "locator": "css selector",
          "selector": "button[type='submit']",
          "instance": "ControlBase",
          "on_instance_search": false,
          "on_instance_load": false,
          "auto_reload": True,
        }
    ]

    # Open bot now
    bot = BotBase(**SETTINGS)
    bot.navigation.get_url("http://the-internet.herokuapp.com/login")

    # Obtains WebElement and wrap into ControlBase
    txt_username = ControlBase(bot, **CONTROLS[0])
    txt_password = ControlBase(bot, **CONTROLS[1])
    btn_login = ControlBase(bot, **CONTROLS[2])

    # Do some stuff
    txt_username.type_text('tomsmith', clear=True)
    txt_password.type_text('SuperSecretPassword!', clear=True)
    btn_login.click()

ControlForm
~~~~~~~~~~~

+ Param **on_instance_strict** : by default it's disabled, at enable raises when strict_rules type warning logs message with 'hight severity' or when type error log messages with 'medium or more severity'
+ Param **strict_rules** : Allow to add strict_rules configuration to laod StrictRule class for each rule ( example: ``strict_rule = StrictRule('my_named_rule', StrictType.TAG, StrictSeverity.HIGHT)`` )


ControlGroup
~~~~~~~~~~~~

+ Param **on_instance_group** : by default it's disabled, at enable raises when strict_rules type warning logs message with 'hight severity' or when type error log messages with 'medium or more severity'
+ Param **group** : allow to track all ControlBase elements using `elements` (*instances of WebElement*) and `group` (*instances of ControlBase*) properties 

Pages
-----

Have classes for this down package: ``qacode.core.bots.webs.pages``

PageBase
~~~~~~~~

+ Param **url** : string for url of page
+ Param **locator** : strategy used to search all selectors passed, default value it's locator.CSS_SELECTOR (default: {BY.CSS_SELECTOR})
+ Param **go_url** : navigate to 'self.url' at instance (default: {False})
+ Param **wait_url** : seconds to wait for 'self.url' load at instance (default: {0})
+ Param **maximize** : allow to maximize browser window before to load elements at instance (default: {False})
+ Param **controls** : list of dicts with settings for each control which want to load

Example : just using pages methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python


    from qautils.files import settings
    from qacode.core.bots import BotBase

    # Load settings for bot and pages
    SETTINGS = settings('settings.json')
    PAGES = [
        {
            "name": "nav_tests_home",
            "url": "http://the-internet.herokuapp.com/",
            "locator": "css selector",
            "go_url": false,
            "wait_url": 0,
            "maximize": false,
            "controls": []
          }
    ]
    # Open bot now
    bot = BotBase(**SETTINGS)

    # Create page now
    page = PageBase(bot, **PAGES[0])

    # Do some stuff
    page.go_url()
    page.is_url() == True


Tests
-----

Have classes for this down package: ``qacode.core.testing.test_info``

TestInfoBase
~~~~~~~~~~~~
- Methods for **Class**

  + constructor : If use on inherit classes, **pytest will fail at execute tests!**
- Methods for **Settings**

  + method **load** : Load default config dict
  + method **bot_open** : Open browser using BotBase instance
  + method **bot_close** : Close bot calling bot.close() from param
  + method **settings_apps** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps'
  + method **settings_app** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps' filtering by 'app_name' param
  + method **settings_page** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps[i].pages' filtering by 'page_name' param
  + method **settings_control** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps[i].pages[j].controls' filtering by 'control_name' param
- Methods for **Test Suites + Test Cases**

  + method **setup_method** : Configure self.attribute
  + method **teardown_method** : Unload self.attribute
  + method **add_property** : Add property to test instance using param 'name', will setup None if any value it's passed by param
- Methods for **utilities**

  + method **timer** : Timer to sleep browser on testcases
  + method **sleep** : Just call to native python time.sleep method
- Methods for **Asserts**

  + method **assert_equals** : Allow to compare 2 values and check if 1st it's equals to 2nd value
  + method **assert_not_equals** : Allow to compare 2 value to check if 1st isn't equals to 2nd value
  + method **assert_equals_url** : Allow to compare 2 urls and check if 1st it's equals to 2nd url
  + method **assert_not_equals_url** : Allow to compare 2 urls to check if 1st isn't equals to 2nd url
  + method **assert_contains_url** : Allow to compare 2 urls and check if 1st contains 2nd url
  + method **assert_not_contains_url** : Allow to compare 2 urls and check if 1st not contains 2nd url
  + method **assert_is_instance** : Allow to encapsulate method assertIsInstance(obj, cls, msg='')
  + method **assert_raises** : Allow to encapsulate pytest.raises
  + method **assert_greater** : Allow to encapsulate method assertGreater(a, b, msg=msg)
  + method **assert_lower** : Allow to encapsulate method assertLower(a, b, msg=msg)
  + method **assert_in** : Allow to compare if value it's in to 2nd list of values
  + method **assert_not_in** : Allow to compare if value it's not in to 2nd list of values
  + method **assert_regex** : Allow to compare if value match pattern
  + method **assert_not_regex** : Allow to compare if value not match pattern
  + method **assert_regex_url** : Allow to compare if value match url pattern, can use custom pattern
  + method **assert_path_exist** : Allow to check if path exist, can check if is_dir also
  + method **assert_path_not_exist** : Allow to check if path not exist, can check if is_dir also
  + method **assert_true** : Allow to compare and check if value it's equals to 'True'
  + method **assert_false** : Allow to compare and check if value it's equals to 'False'
  + method **assert_none** : Allow to compare and check if value it's equals to 'None'
  + method **assert_not_none** : Allow to compare and check if value it's not equals to 'None'


Example : inherit from TestInfoBase class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python


    from qautils.files import settings
    from qacode.core.bots import BotBase
    from qacode.core.testing.test_info import TestInfoBase


    class TestAwesome(TestInfoBase):

        def test_some_method(self):
            try:
                _settings = settings('settings.json')
                bot = self.bot_open(**_settings)
                self.log.info("Bot opened for new test method down new test suite")
                self.assert_is_instance(bot, BotBase)
            except AssertionError as err:
                self.log.error("Bot Fails at assert %s", err.message)


TestInfoBot
~~~~~~~~~~~

- Methods for **Class**

  + constructor : If use on inherit classes, **pytest will fail at execute tests!**
  + method **setup_method** : Configure self.attribute. If skipIf mark applied and True as first param for args tuple then not open bot
  + method **teardown_method** : Unload self.attribute, also close bot

Example : inherit from TestInfoBot class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python


    from qacode.core.testing.test_info import TestInfoBot


    class TestAwesome(TestInfoBot):

        def test_some_method(self):
            try:
                self.assert_is_instance(self.bot, BotBase)
            except AssertionError as err:
                self.log.error("Bot Fails at assert %s", err.message)


TestInfoBotUnique
~~~~~~~~~~~~~~~~~

- Methods for **Class**

  + constructor : If use on inherit classes, **pytest will fail at execute tests!**
  + method **setup_class** : Configure 'cls.attribute'. If name start with 'test_' and have decorator skipIf with value True, then not open bot
  + method **teardown_class** : Unload self.attribute, closing bot from 'cls.bot' property
  + method **teardown_method** : Unload self.attribute, also disable closing bot from TestInfoBot



Example : inherit from TestInfoBotUnique class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python


    from qacode.core.testing.test_info import TestInfoBotUnique


    class TestAwesomeUnique(TestInfoBotUnique):

        def test_some_method(self):
            try:
                self.assert_is_instance(self.bot, BotBase)
            except AssertionError as err:
                self.log.error("Bot Fails at assert %s", err.message)
        
        def test_some_another_method(self):
            try:
                # Same bot that was used for 'test_some_method' test
                self.assert_is_instance(self.bot, BotBase)
            except AssertionError as err:
                self.log.error("Bot Fails at assert %s", err.message)
