# QA Code

+ **Linux Deploy**: [![Build status ](https://travis-ci.org/netzulo/qacode.svg?branch=master)](https://travis-ci.org/netzulo/qacode)
+ **Windows Deploy**: [![Build status](https://ci.appveyor.com/api/projects/status/rykjetai0968blwt?svg=true)](https://ci.appveyor.com/api/projects/status/rykjetai0968blwt?svg=true)

Python library for : **3.6**

## PIP installation ?

```
pip install qacode
```

## Prerequisites ?

+ 1. Install python environment manager: `sudo apt-get install mkvirtualenv`
+ 2. Create virtual environment: `mkvirtualenv qalab-core`
+ 3. Activate environment ? `workon qalab-core`
+ 4. Install dependencies (mkvirtual autoinstall dependencies): `pip install -r requirements.txt`
+ 5. Configure settings.ini file
+ 6. Download Drivers __(just chrome it's required for now)__ : https://chromedriver.storage.googleapis.com/index.html?path=2.30/
+ 7. Pass all tests with environment active: `bash qalab-core.sh test`

## Configuration File

+ 1. Configure path for key : **drivers_path**
+ 2. Configure path for key : **log_output_file**

```
# @author: Netzulo
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
drivers_path=
# FILE NAME FOR LOGGER
log_name=qalabCore
# OUTPUT FILE NAME FOR LOGGER
log_output_file=

[TESTLINK]
# Url for testlink API : http://localhost/lib/api/xmlrpc/v1/xmlrpc.php
url=
# Devkey provided by testlink: 182c5b87c776ff2956b68e23eae866d9
devkey= 
[TEST_UNITARIES]
url=http://demoqa.com

```

---

## Command Usage

```

USAGE: \n
  bash qacode.sh [-h] [TEST_NAME] [TEST_CFG]
VERSION: 
  v0.0.0-unstable: still building proyects
-------------------------------------
COMMANDS for TEST_NAME: valid values are
  install: install pip dependencies
  help : [-h] Show this help message
  	test : exec file ./test/
	test-unitaries : exec file ./test/unitaries/
	test-loggers: exec file ./test/unitaries/TestLoggerManager.py
	test-configs: exec file ./test/unitaries/TestConfig.py
	test-functionals: exec file ./test/functionals/
	test-bots: exec file ./test/functionals/TestBotBase.py
COMMANDS for TEST_CFG: valid values are
    [empty value] : use config file on ./configs/settings.example.ini
  [ini file] : specify absolut pathname for ini file

```
