# QA Code

| Branch  | Linux Deploy | Windows Deploy |
| ------------- | ------------- |  ------------- |
| master  | [![Build Status](https://travis-ci.org/netzulo/qadoc.svg?branch=master)](https://travis-ci.org/netzulo/qacode)  | [![Build status](https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/master?svg=true)](https://ci.appveyor.com/project/netzulo/qacode/branch/master)  |
| devel  | [![Build Status](https://travis-ci.org/netzulo/qadmin.svg?branch=devel)](https://travis-ci.org/netzulo/qacode)  | [![Build status](https://ci.appveyor.com/api/projects/status/4a0tc5pis1bykt9x/branch/devel?svg=true)](https://ci.appveyor.com/project/netzulo/qacode/branch/devel)  |

Python tested versions :

  +  **3.6**
  +  **3.5**
  +  **3.4**
  +  **3.3**
  +  **3.2**
  +  **2.7**

## PIP installation ?

```
pip install qacode
```

## SETUP.py installation

```
python setup.py install
```

## Configuration File

+ 1. Configure path for key : **drivers_path**
+ 2. Configure path for key : **log_output_file**

```
# author: Netzulo
[BOT]
# DRIVERMODE: local , remote
mode=local
# BROWSER: firefox , chrome , iexplorer, phantomjs
browser=chrome
# REMOTEDRIVER
url_hub=http://localhost:11000/wd/hub
# NODEWEBDRIVER
url_node=http://localhost:11001/wd/hub
# FIREFOXPROFILE
profile_path=
# DRIVERS PATH
drivers_path=drivers
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
url=http://demoqa.com

```
