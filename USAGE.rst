Usage Guide
===========

Bots
----

Have classes for this down package: `qacode.core.bots`


.. code-block:: python
   :linenos:

    from qacode.core.utils import settings
    from qacode.core.bots import BotBase
    # SETTINGS = settings()
    SETTINGS = {
        "bot": {
            "mode": "remote",
            "browser": "chrome",
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
            ],
            "log_output_file": "logs",
            "log_name": "qacode",
            "log_level": "DEBUG"
        }
    }
    # Open bot now
    bot = BotBase(**SETTINGS)

Controls
--------

Have classes for this down package: `qacode.core.bots.webs.controls`

ControlBase
~~~~~~~~~~~

It's base control to load web element from `WebDriver + browser session` , *this class must be use to inherit new* `ControlAwesome` *classes*

+ Param **name** : allows to set value to `ControlBase.name` property, also it's used by pages to set property page with `control.name` value
+ Param **locator** : This text it's parsed down selenium class `selenium.webdriver.common.by.By` (*default:* `css selector` == `By.CSS_SELECTOR`)
+ Param **selector** : valid selector for locator selected
+ Param **instance** : allow to generate your own inherit classes from `ControlBase` and instance them  using qacode strategy (*default:* `ControlBase`)
+ Param **on_instance_search** : enable searching element at instance `ControlBase` (*default:* `True`)
+ Param **on_instance_load** : enable loading `ControlBase` properties when element it's loaded (*default:* `False`) , will need enabled if want to access to base properties values obtained from selenium methods at `BotBase.navigation`

Example of usage
^^^^^^^^^^^^^^^^

.. code-block:: python
   :linenos:

    from qacode.core.utils import settings
    from qacode.core.bots import BotBase

    # Load settings for bot and controls
    SETTINGS = settings()
    CONTROLS = [
        {
            "name": "txt_username",
            "locator": "css selector",
            "selector": "#username",
            "instance": "ControlBase",
            "on_instance_search": true,
            "on_instance_load": false
        },
        {
          "name": "txt_password",
          "locator": "css selector",
          "selector": "#password",
          "instance": "ControlBase",
          "on_instance_search": true,
          "on_instance_load": false
        },
        {
          "name": "btn_submit",
          "locator": "css selector",
          "selector": "button[type='submit']",
          "instance": "ControlBase",
          "on_instance_search": true,
          "on_instance_load": false
        },
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

+ Param **on_instance_strict** : `TODO: document this, open issue on github`
+ Param **strict_rules** : `TODO: document this, open issue on github`


Pages
-----

Have classes for this down package: `qacode.core.bots.webs.pages`

PageBase
~~~~~~~~

+ Param **name** : `TODO: document this, open issue on github`
+ Param **url** : `TODO: document this, open issue on github`
+ Param **locator** : `TODO: document this, open issue on github`
+ Param **go_url** : `TODO: document this, open issue on github`
+ Param **wait_url** : `TODO: document this, open issue on github`
+ Param **maximize** : `TODO: document this, open issue on github`
+ Param **controls** : `TODO: document this, open issue on github`

Example : just using pages methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   :linenos:

    from qacode.core.utils import settings
    from qacode.core.bots import BotBase

    # Load settings for bot and pages
    SETTINGS = settings()
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

Have classes for this down package: `qacode.core.testing.test_info`

TestInfoBase
~~~~~~~~~~~~
- Methods for **Class**

  + constructor : If use on inherit classes, **pytest will fail at execute tests!**
- Methods for **Settings**

  + method **bot_open** : `TODO: document this, open issue on github`
  + method **bot_close** : `TODO: document this, open issue on github`
  + method **settings_apps** : `TODO: document this, open issue on github`
  + method **settings_app** : `TODO: document this, open issue on github`
  + method **settings_page** : `TODO: document this, open issue on github`
  + method **settings_control** : `TODO: document this, open issue on github`
- Methods for **Test Suites + Test Cases**

  + method **setup_class** : `TODO: document this, open issue on github`
  + method **teardown_class** : `TODO: document this, open issue on github`
  + method **setup_method** : `TODO: document this, open issue on github`
  + method **teardown_method** : `TODO: document this, open issue on github`
  + method **add_property** : `TODO: document this, open issue on github`
- Methods for **utilities**

  + method **timer** : `TODO: document this, open issue on github`
  + method **sleep** : `TODO: document this, open issue on github`
- Methods for **Asserts**
  + method **assert_equals** : `TODO: document this, open issue on github`
  + method **assert_not_equals** : `TODO: document this, open issue on github`
  + method **assert_equals_url** : `TODO: document this, open issue on github`
  + method **assert_not_equals_url** : `TODO: document this, open issue on github`
  + method **assert_contains_url** : `TODO: document this, open issue on github`
  + method **assert_raises** : `TODO: document this, open issue on github`
  + method **assert_greater** : `TODO: document this, open issue on github`
  + method **assert_lower** : `TODO: document this, open issue on github`
  + method **assert_in** : `TODO: document this, open issue on github`
  + method **assert_not_in** : `TODO: document this, open issue on github`
  + method **assert_regex** : `TODO: document this, open issue on github`
  + method **assert_not_regex** : `TODO: document this, open issue on github`
  + method **assert_regex_url** : `TODO: document this, open issue on github`
  + method **assert_path_exist** : `TODO: document this, open issue on github`
  + method **assert_path_not_exist** : `TODO: document this, open issue on github`
  + method **assert_true** : `TODO: document this, open issue on github`
  + method **assert_false** : `TODO: document this, open issue on github`
  + method **assert_none** : `TODO: document this, open issue on github`
  + method **assert_not_none** : `TODO: document this, open issue on github`

Example : inherit from TestInfoBase class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   :linenos:

    from qacode.core.bots import BotBase
    from qacode.core.testing.test_info import TestInfoBase


    class TestAwesome(TestInfoBase):

        def test_some_method(self):
            try:
                bot = self.bot_open(
                self.log.info("Bot opened for new test method down new test suite")
                self.assert_is_instance(bot, BotBase)
            except AssertionError as err:
                self.log.error("Bot Fails at assert %s", err.message)
