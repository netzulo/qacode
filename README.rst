QA Code
=======


.. image:: https://img.shields.io/github/issues/netzulo/qacode.svg
  :alt: Issues on Github
  :target: https://github.com/netzulo/qacode/issues

.. image:: https://img.shields.io/github/issues-pr/netzulo/qacode.svg
  :alt: Pull Request opened on Github
  :target: https://github.com/netzulo/qacode/issues

.. image:: https://img.shields.io/github/release/netzulo/qacode.svg
  :alt: Release version on Github
  :target: https://github.com/netzulo/qacode/releases/latest

.. image:: https://img.shields.io/github/release-date/netzulo/qacode.svg
  :alt: Release date on Github
  :target: https://github.com/netzulo/qacode/releases/latest

+-----------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Branch                | Linux Deploy                                                      | Windows Deploy                                                                                 | CircleCI - Docker                                                                                                         | CodeClimate                                                                            |
+=======================+===================================================================+================================================================================================+===========================================================================================================================+========================================================================================+
|  master               | .. image:: https://travis-ci.org/netzulo/qacode.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true | .. image:: https://circleci.com/gh/netzulo/qacode.svg?&style=shield&circle-token=80384cb2233d112dc0785278d5b7c3d8c6a5686c | .. image:: https://api.codeclimate.com/v1/badges/46279cf9a6a47ed583d6/maintainability  |
+-----------------------+-----------------------+-------------------------------------------+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+


Python tested versions
----------------------

+-------------------+-------------------+-------------------+-------------------+
|  **3.7**          |  **3.6**          |  **3.5**          |  **<=3.4**        |
+===================+===================+===================+===================+
|    *Supported*    |    *Supported*    |    *Supported*    |  *Not Supported*  |
+-------------------+-------------------+-------------------+-------------------+


How to install ?
----------------

+ Install from PIP : ``pip install qacode``

+ Install from setup.py file : ``python setup.py install``


Documentation
-------------

+ How to use library, searching for `Usage Guide`_ or auto updated `QAcode's Documentation`_. https://netzulo.github.io/


How to exec tests ?
-------------------

+ Tests from setup.py file : ``python setup.py test``

+ Install from PIP file : ``pip install tox``
+ Tests from tox : ``tox -l && tox -e TOX_ENV_NAME`` ( *see tox.ini file to get environment names* )


+---------------------+--------------------------------+
| TOX Env name        | Env description                |
+=====================+================================+
| py35,py36,py37      | Python supported versions      |
+---------------------+--------------------------------+
| flake8              | Exec linter in qalab/ tests/   |
+---------------------+--------------------------------+
| coverage            | Generate XML and HTML reports  |
+---------------------+--------------------------------+
| docs                | Generate doc HTML in /docs     |
+---------------------+--------------------------------+

Configuration File
~~~~~~~~~~~~~~~~~~


::

    {
      "bot": {
        "log_output_file": "logs/",
        "log_name": "qacode",
        "log_level": "DEBUG",
        "mode": "remote",
        "browser": "chrome",
        "options": { "headless": false },
        "url_hub": "http://localhost:11000/wd/hub",
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


Getting Started
~~~~~~~~~~~~~~~

*Just starting example of usage before read* `Usage Guide`_ (*or refer to `QAcode's Documentation`_*).

.. code:: python


    from qacode.core.bots.bot_base import BotBase
    from qacode.core.webs.controls.control_base import ControlBase
    from qacode.utils import settings
    
    
    SETTINGS = settings(
        file_path="/home/user/config/dir/",
        file_name="settings.json"
    )
    
    
    try:
        bot = BotBase(**SETTINGS)
        bot.navigation.get_url("http://the-internet.herokuapp.com/login")
        ctl_config = { "selector": "input[name='username']"}
        ctl = ControlBase(bot, **ctl_config)
        # END
        import pdb; pdb.set_trace() # TODO, remove DEBUG lane
        print(ctl)
    except Exception as err:
        print("ERROR: {}".format(err))
    finally:
        bot.close()





.. _Usage Guide: USAGE.rst
.. _`QAcode's Documentation`: https://netzulo.github.io/