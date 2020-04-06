Usage Guide
===========

Bots
----

Have classes for this down package: ``qacode.core.bots``


.. code:: python


    from qacode.utils import settings
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
                "edgedriver_64.exe"
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
+ Param **on_instance_search** : enable searching element at instance `ControlBase` , also properties when element it's loaded (*default:* `False`) *access to base properties values obtained from selenium methods at* ``BotBase.navigation``
+ Param **auto_reload** : Allow to reload element searching first when need to use some function of control instance and isn't loaded (*default:* ``True``)

- Methods for **ControlBase**

  + method **__load__** : Load properties from settings dict. Some elements need to search False to be search at future
  + method **__settings_parse__** : Allow to parse settings dict from instance kwargs updating just valid keys with default values if it's required
  + method **__search__** : Load element searching at selenium WebDriver
  + method **__check_reload__** : Allow to check before methods calls to ensure if it's neccessary reload element properties
  + method **find_child** : Find child element using bot with default By.CSS_SELECTOR strategy for internal element trought selenium WebElement
  + method **find_children** : Find children elements using bot with default By.CSS_SELECTOR strategy for internal element trought selenium WebElement
  + method **get_tag** : Returns tag_name from Webelement
  + method **type_text** : Type text on input element
  + method **clear** : Clear input element text value
  + method **click** : Click on element
  + method **get_text** : Get element content textget_attrs
  + method **get_attrs** : Find a list of attributes on WebElement and returns a dict list of {name, value}
  + method **get_attr_value** : Search and attribute name over self.element and get value, if attr_value is obtained, then compare and raise if not
  + method **get_css_value** : Allows to obtain CSS value based on CSS property name
  + method **set_css_value** : Set new value for given CSS property name on ControlBase selector
  + method **reload** : Reload 'self.settings' property:dict and call to instance logic with new configuration
  + method **wait_invisible** : Wait for invisible element, returns control
  + method **wait_visible** : Wait for visible element, returns control
  + method **wait_text** : Wait if the given text is present in the specified control
  + method **wait_blink** : Wait until control pops and dissapears

- Properties for **ControlBase**

  + property **bot** : `GET` + `SET`
  + property **settings** : `GET` + `SET`
  + property **name** : `GET` + `SET`
  + property **selector** : `GET` + `SET`
  + property **element** : `GET` + `SET`
  + property **locator** : `GET` + `SET`
  + property **on_instance_search** : `GET` + `SET`
  + property **auto_reload** : `GET` + `SET`
  + property **tag** : `GET`
  + property **text** : `GET`
  + property **is_displayed** : `GET`
  + property **is_enabled** : `GET`
  + property **is_selected** : `GET`
  + property **attr_id** : `GET`
  + property **attr_class** : `GET`


Example of usage
^^^^^^^^^^^^^^^^

.. code:: python


    from qacode.utils import settings
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
          "on_instance_search": false,
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

ControlDropdown
~~~~~~~~~~~~~~~

- Methods for **ControlDropdown**

  + method **__load__** : Allow to reinstance control properties
  + method **__check_dropdown__** : Internal funcionality for select/deselect methods
  + method **reload** : Reload 'self.settings' property:dict and call to instance logic with new configuration
  + method **select** : The Select class only works with tags which have select tags
  + method **deselect** : The Select class only works with tags which have select tags
  + method **deselect_all** : The Select class only works with tags which have select tags with multiple="multiple" attribute

- Properties for **ControlForm**

  + property **dropdown** : `GET` + `SET`


ControlTable
~~~~~~~~~~~~

- Methods for **ControlTable**

  + method **__check_reload__form__** : Allow to check before methods calls to ensure if it's neccessary reload element properties
  + method **__load_table__** : Allow to load all TR > TD items from a TABLE element
  + method **__load_table_html4__** : Allow to load table with this structure ``TABLE > (TR > TH)+(TR > TD)``
  + method **__load_table_html5__** : Allow to load table with this structure ``TABLE > (THEAD > (TR > TH))+(TBODY > (TR > TH))``
  + method **__get_row__** : Allow to get cells of a <TR> element
  + method **__try__** : Allow to exec some method to handle exception
  + method **__check_reload__** : Allow to check before methods calls to ensure if it's neccessary reload element properties
  + method **reload** : Reload 'self.settings' property:dict and call to instance logic with new configuration

- Properties for **ControlTable**

  + property **table**: `GET` + `SET` for table element ( *just a ``WebElement`` based on ``table`` tag*)
  + property **rows**: `GET` for rows cells based on controls instances

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


    from qacode.utils import settings
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
  + method **cfg_apps** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps'
  + method **cfg_app** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps' filtering by 'app_name' param
  + method **cfg_page** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps[i].pages' filtering by 'page_name' param
  + method **cfg_control** : Obtain inherit dict from 'cls.config' dict named 'config.tests.apps[i].pages[j].controls' filtering by 'control_name' param
- Methods for **Test Suites + Test Cases**

  + method **setup_method** : Configure self.attribute
  + method **teardown_method** : Unload self.attribute
  + method **add_property** : Add property to test instance using param 'name', will setup None if any value it's passed by param
- Methods for **utilities**

  + method **timer** : Timer to sleep browser on testcases
  + method **sleep** : Just call to native python time.sleep method
- Methods for **Asserts**

  + method **equals** : Allow to compare 2 values and check if 1st it's equals to 2nd value
  + method **not_equals** : Allow to compare 2 value to check if 1st isn't equals to 2nd value
  + method **is_instance** : Allow to encapsulate method assertIsInstance(obj, cls, msg='')
  + method **greater** : Allow to encapsulate method assertGreater(a, b, msg=msg)
  + method **lower** : Allow to encapsulate method assertLower(a, b, msg=msg)
  + method **in_list** : Allow to compare if value it's in to 2nd list of values
  + method **not_in_list** : Allow to compare if value it's not in to 2nd list of values
  + method **regex** : Allow to compare if value match pattern
  + method **not_regex** : Allow to compare if value not match pattern
  + method **regex_url** : Allow to compare if value match url pattern, can use custom pattern
  + method **path_exist** : Allow to check if path exist, can check if is_dir also
  + method **path_not_exist** : Allow to check if path not exist, can check if is_dir also
  + method **true** : Allow to compare and check if value it's equals to 'True'
  + method **false** : Allow to compare and check if value it's equals to 'False'
  + method **none** : Allow to compare and check if value it's equals to 'None'
  + method **not_none** : Allow to compare and check if value it's not equals to 'None'


Example : inherit from TestInfoBase class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python


    from qacode.utils import settings
    from qacode.core.bots import BotBase
    from qacode.core.testing.asserts import Assert
    from qacode.core.testing.test_info import TestInfoBase


    ASSERT = Assert()


    class TestAwesome(TestInfoBase):

        def test_some_method(self):
            try:
                _settings = settings('settings.json')
                bot = self.bot_open(**_settings)
                self.log.info("Bot opened for new test method down new test suite")
                ASSERT.is_instance(bot, BotBase)
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


    from qacode.core.testing.asserts import Assert
    from qacode.core.testing.test_info import TestInfoBot


    ASSERT = Assert()


    class TestAwesome(TestInfoBot):

        def test_some_method(self):
            try:
                ASSERT.is_instance(self.bot, BotBase)
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


    from qacode.core.testing.asserts import Assert
    from qacode.core.testing.test_info import TestInfoBotUnique


    ASSERT = Assert()

    class TestAwesomeUnique(TestInfoBotUnique):

        def test_some_method(self):
            try:
                ASSERT.is_instance(self.bot, BotBase)
            except AssertionError as err:
                self.log.error("Bot Fails at assert %s", err.message)
        
        def test_some_another_method(self):
            try:
                # Same bot that was used for 'test_some_method' test
                ASSERT.is_instance(self.bot, BotBase)
            except AssertionError as err:
                self.log.error("Bot Fails at assert %s", err.message)
