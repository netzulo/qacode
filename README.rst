QA Code
=======

.. image:: https://img.shields.io/github/downloads/netzulo/qacode/total.svg
  :alt: Downloads on Github
  :target: https://img.shields.io/github/downloads/netzulo/qacode/total.svg
.. image:: https://img.shields.io/pypi/dd/qacode.svg
  :alt: Downloads on Pypi
  :target: https://img.shields.io/pypi/dd/qacode.svg
.. image:: https://img.shields.io/github/release/netzulo/qcode.svg
  :alt: GitHub release
  :target: https://img.shields.io/github/release/netzulo/qcode.svg

+-----------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Branch                | Linux Deploy                                                      |Windows Deploy                                                                                  |
+=======================+===================================================================+================================================================================================+
|  master               | .. image:: https://travis-ci.org/netzulo/qacode.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true |
+-----------------------+-----------------------+-------------------------------------------+------------------------------------------------------------------------------------------------+
|  master               | .. image:: https://travis-ci.org/netzulo/qacode.svg?branch=devel  | .. image:: https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/devel?svg=true  |
+-----------------------+-----------------------+-------------------------------------------+------------------------------------------------------------------------------------------------+


Python tested versions
----------------------
+  **3.6**
+  **3.5**
+  **3.4**
+  **3.3**
+ **3.2** *(not supported)*
+  **2.7**


Code Metrics
------------

.. image:: http://qalab.tk:82/api/badges/gate?key=qacode
  :alt: Quality Gate


PIP install
-----------

``pip install qacode``

SETUP.py install
----------------

``python setup.py install``


Configuration File
------------------

:: 

    # author: Netzulo
    [BOT]
    # DRIVERMODE: local , remote
    mode=remote
    # BROWSER: firefox , chrome , iexplorer, edge, phantomjs
    browser=chrome
    # REMOTEDRIVER
    url_hub=http://146.255.101.51:11000/wd/hub
    # NODEWEBDRIVER
    url_node=http://146.255.101.51:11001/wd/hub
    # DRIVERS PATH
    drivers_path=../../modules/qadrivers
    # DRIVERS NAMES
    drivers_names= [
        "chromedriver_32.exe","chromedriver_64.exe","chromedriver_32","chromedriver_64",
        "firefoxdriver_32.exe", "firefoxdriver_64.exe","firefoxdriver_64.exe","firefoxdriver_32",
        "phantomjsdriver_32.exe", "phantomjsdriver_64.exe","phantomjsdriver_32","phantomjsdriver_64",
        "iexplorerdriver_32.exe","iexplorerdriver_64.exe",
        "edgedriver_32.exe","edgedriver_64.exe"]
    # FILE NAME FOR LOGGER
    log_name=qacode
    # OUTPUT FILE NAME FOR LOGGER
    log_output_file=logs
  
    [TESTLINK]
    # Url for testlink API : http://localhost/lib/api/xmlrpc/v1/xmlrpc.php
    url=http://localhost/lib/api/xmlrpc/v1/xmlrpc.php
    # Devkey provided by testlink: 182c5b87c776ff2956b68e23eae866d9
    devkey=182c5b87c776ff2956b68e23eae866d9

    [TEST_UNITARIES]
    url=https://www.netzulo.com

Tests
-----

Unitaries
*********

::

    nosetests tests/unitaries/TestConfig.py --tc-file="qacode/configs/settings.ini"
    nosetests tests/unitaries/TestLoggerManager.py --tc-file="qacode/configs/settings.ini"
    nosetests tests/unitaries/TestTestInfoBase.py --tc-file="qacode/configs/settings.example.ini"


Functionals
***********

::

    nosetests tests/functionals/TestBotBase.py --tc-file="qacode/configs/settings.example.ini"
    nosetests tests/functionals/TestNavBase.py --tc-file="qacode/configs/settings.example.ini"
    nosetests tests/functionals/TestPageBase.py --tc-file="qacode/configs/settings.example.ini"


Live example
************

.. image:: https://asciinema.org/a/HEk8Dm0zL6eDoyj8MA19wawAx.png
  :target: https://asciinema.org/a/HEk8Dm0zL6eDoyj8MA19wawAx
  :alt: asciicast
