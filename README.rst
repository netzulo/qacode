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

+-----------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Branch                | Linux Deploy                                                      | Windows Deploy                                                                                 |
+=======================+===================================================================+================================================================================================+
|  master               | .. image:: https://travis-ci.org/netzulo/qacode.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true |
+-----------------------+-----------------------+-------------------------------------------+------------------------------------------------------------------------------------------------+


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


TOX environments
****************

+---------------------+--------------------------------+
| Env name            | Env description                |
+=====================+================================+
| py27,py34,py35,py36 | Python supported versions      |
+---------------------+--------------------------------+
| docs                | Generate doc HTML in /docs     |
+---------------------+--------------------------------+
| flake8              | Exec linter in qalab/ tests/   |
+---------------------+--------------------------------+
| coverage            | Generate XML and HTML reports  |
+---------------------+--------------------------------+


Configuration File
------------------


::

    {
      "bot": {
        "mode": "remote",
        "browser": "chrome",
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
