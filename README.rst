QA Code
=======

.. image:: https://img.shields.io/github/downloads/netzulo/qacode/total.svg
  :alt: Downloads on Github
  :target: https://img.shields.io/github/downloads/netzulo/qacode/total.svg
.. image:: https://img.shields.io/github/release/netzulo/qcode.svg
  :alt: GitHub release
  :target: https://img.shields.io/github/release/netzulo/qcode.svg

+-----------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Branch                | Linux Deploy                                                      | Windows Deploy                                                                                 |
+=======================+===================================================================+================================================================================================+
|  master               | .. image:: https://travis-ci.org/netzulo/qacode.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true |
+-----------------------+-----------------------+-------------------------------------------+------------------------------------------------------------------------------------------------+
|  devel                | .. image:: https://travis-ci.org/netzulo/qacode.svg?branch=devel  | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/devel?svg=true  |
+-----------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------+


Python tested versions
----------------------

+  **3.6**
+  **3.5**
+  **3.4**
+  **3.3** (*not supported*)
+  **3.2** (*not supported*)
+  **2.7**


Code Metrics by sonarqube
----------------------------

.. image:: http://qalab.tk:82/api/badges/gate?key=qacode
  :alt: Quality Gate
  :target: http://qalab.tk:82/api/badges/gate?key=qacode
.. image:: http://qalab.tk:82/api/badges/measure?key=qacode&metric=lines
  :alt: Lines
  :target: http://qalab.tk:82/api/badges/gate?key=qacode
.. image:: http://qalab.tk:82/api/badges/measure?key=qacode&metric=bugs
  :alt: Bugs
  :target: http://qalab.tk:82/api/badges/gate?key=qacode
.. image:: http://qalab.tk:82/api/badges/measure?key=qacode&metric=vulnerabilities
  :alt: Vulnerabilities
  :target: http://qalab.tk:82/api/badges/gate?key=qacode
.. image:: http://qalab.tk:82/api/badges/measure?key=qacode&metric=code_smells
  :alt: Code Smells
  :target: http://qalab.tk:82/api/badges/gate?key=qacode
.. image:: http://qalab.tk:82/api/badges/measure?key=qacode&metric=sqale_debt_ratio
  :alt: Debt ratio
  :target: http://qalab.tk:82/api/badges/gate?key=qacode
.. image:: http://qalab.tk:82/api/badges/measure?key=qacode&metric=comment_lines_density
  :alt: Comments
  :target: http://qalab.tk:82/api/badges/gate?key=qacode


PIP install
-----------

``pip install qacode``

SETUP.py install
----------------

``python setup.py install``

Tests
-----

``python setup.py test``

Unitaries
*********

::

    pytest tests/unitaries/TestConfig.py
    pytest tests/unitaries/TestLoggerManager.py
    pytest tests/unitaries/TestTestInfoBase.py


Functionals
***********

::
    
    pytest tests/functionals/TestBotBase.py
    pytest tests/functionals/TestTestInfoBot.py
    pytest tests/functionals/TestNavBase.py
    pytest tests/functionals/TestPageBase.py
    pytest tests/functionals/TestPageLogin.py
    pytest tests/functionals/TestControlBase.py


Configuration File
------------------

.. highlight:: json
.. code-block:: json
   :linenos:

::

    {
      "bot": {
        "mode": "remote",
        "browser": "chrome",
        "url_hub": "http://146.255.101.51:11000/wd/hub",
        "url_node": "http://146.255.101.51:11001/wd/hub",
        "drivers_path": "../../modules/qadrivers",
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
        ],
        "log_output_file": "logs",
        "log_name": "qacode"
      },
      "testlink": {
        "enabled": false,
        "url_api": "http://qalab.tk:86/lib/api/xmlrpc/v1/xmlrpc.php",
        "dev_key": "ae2f4839476bea169f7461d74b0ed0ac",
        "data":{
          "generate": false,
          "test_proyects":[
            {"id_prefix":"qacode", "name":"qacode", "desc":"Main QA library"}
          ]
        }
      },
      "tests": {
        "unitaries": {
          "url": "https://www.netzulo.com"
        },
        "functionals": {
          "url_login": "http://qalab.tk:82/sessions/new",
          "url_logout": "http://qalab.tk:82/sessions/logout",
          "url_logged": "http://qalab.tk:82/",
          "url_404": "http://qalab.tk:82/sessions/login",
          "selectors_login": [
            "#login",
            "#password",
            "[name='commit']"
          ],
          "creed_user": "qacode",
          "creed_pass": "qacode",
          "url_selector_parent": "http://qalab.tk:82/sessions/new",
          "selector_parent": "#login_form",
          "selector_child": "#login"
          }
        }
      },
      "build": {
        "travis":{ "skip_tests": true }
      }
    }


Live example
************

.. image:: https://asciinema.org/a/phH5ISjGEfwXZUp648dvMOqox.png
  :target: https://asciinema.org/a/phH5ISjGEfwXZUp648dvMOqox
  :alt: asciicast


