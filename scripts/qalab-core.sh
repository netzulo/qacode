#!/bin/bash
# -------------------------
# CONFIGURATIONs
export TEST_NAME=$1
export TEST_CFG=$2
export CURR_PATH='.'
# -------------------------
# Library functions
function qalab-core-fail-not-implemented {
    echo -e "[qalab-core] : ERROR, function not implemented"
    exit 1
}

function qalab-core-fail {
    echo -e "[qalab-core] : FAILED execution on path --> $CURR_PATH"
    exit 1
}

function qalab-core-end {
    echo -e "[qalab-core] : finished execution on path --> $CURR_PATH"
}


function qalab-core-help {
    echo -e "-------------------------------------"
	echo -e "USAGE: \n"
	echo -e "  bash qalab-core.sh [-h] [TEST_NAME] [TEST_CFG]"
	echo -e "VERSION: "
	echo -e "  v0.0.0-unstable: still building proyects"
	echo -e "-------------------------------------\n"
	echo -e "COMMANDS for TEST_NAME: valid values are \n"
	echo -e "  install: install pip dependencies"
	echo -e "  help : [-h] Show this help message"
	echo -e "  test : exec file ./test/"
	echo -e "  test-unitaries : exec file ./test/unitaries/"
	echo -e "  test-loggers: exec file ./test/unitaries/TestLoggerManager.py"
	echo -e "  test-configs: exec file ./test/unitaries/TestConfig.py"
	echo -e "  test-functionals: exec file ./test/functionals/"
	echo -e "  test-bots: exec file ./test/functionals/TestBotBase.py"
    echo -e "\nCOMMANDS for TEST_CFG: valid values are \n"
    echo -e "  [empty value] : use config file on ./configs/settings.example.ini"
	echo -e "  [ini file] : specify absolut pathname for ini file"
    echo -e "-------------------------------------"
    qalab-core-end
}

function qalab-core-test {
	if [ -n "$TEST_NAME" ]
	then
	    echo -e "\e[34m [qalab-core]: Tests starting... \e[92m OK \e[39m"
	else
		echo -e "\e[34m [qalab-core]: FAILED at start tests, bad test name provided \e[91m KO \e[39m"
		exit 1
	fi
	
	if [ -n "$TEST_CFG" ]
	then
	    echo -e "\e[34m [qalab-core]: Config ready... \e[92m OK \e[39m"
	else
	    echo -e "\e[34m [qalab-core]: FAILED at read config for test \e[91m KO \e[39m"
		exit 1
	fi

	nosetests $TEST_NAME --tc-file="$TEST_CFG"
	
	if [ $? -eq 0 ]
	then
		echo -e "\e[34m [qalab-core]: Tests executed... \e[92m OK \e[39m"
	else
		echo -e "\e[34m [qalab-core]: FAILED at execute tests \e[91m KO \e[39m"
		exit 1
	fi
}


function qalab-core-test-select {
    echo -e "[qalab-core] : Selecting Tests by name--> $TEST_NAME"
    case $TEST_NAME in
		"help")
		qalab-core-help
		;;
		"install")
		qalab-core-install
		;;
		"test")
		TEST_NAME=../tests/
		;;		
		"test-unitaries")
		TEST_NAME=../tests/unitaries
		;;
		"test-loggers")
		TEST_NAME=../tests/unitaries/TestLoggerManager.py
		;;
		"test-configs")
		TEST_NAME=../tests/unitaries/TestConfig.py
		;;
		"test-functionals")
		TEST_NAME=../tests/functionals
		;;		
		"test-bots")
		TEST_NAME=../tests/functionals/TestBotBase.py
		;;
		*)
		echo -e "[qalab-core] : ERROR, provided test name doesn't exist at library: $TEST_NAME"
		qalab-core-fail
		;;
	esac
	echo -e "[qalab-core] : Selected Tests named--> $TEST_NAME"
	qalab-core-test
}

function qalab-core-install {
	mkdir -p $CURR_PATH/logs

	if [ $? -eq 0 ]
		then
			echo -e "\e[34m LOGS FOLDER CREATED: \e[92m OK \e[39m"
		else
			echo -e "\e[34m LOGS FOLDER failet at CREATE: \e[91m KO \e[39m"
			exit 1
	fi

	pip install -r ../requirements.txt

	if [ $? -eq 0 ]
		then
			echo -e "\e[34m PIP DEPENDENCIES INSTALLED: \e[92m OK \e[39m"
		else
			echo -e "\e[34m PIP DEPENDENCIES FAILED at INSTALL: \e[91m KO \e[39m"
			exit 1
	fi
}


function qalab-core {
	echo -e "[qalab-core] : starting on path --> $CURR_PATH"
	TEST_NAME=$1
	TEST_CFG=$2

	if [ "$TEST_NAME" == "-h" ] || [ "$TEST_NAME" == "help" ];
	then
		qalab-core-help
	else
		if [ "$TEST_NAME" == "" ];	then
			echo -e "[qalab-core] : TEST_NAME can't be empty, no test name provided..."
			qalab-core-fail
		fi
		if [ "$TEST_CFG" == "" ];	then
			echo -e "[qalab-core] : $TEST_CFG can be empty, using default config on... $CURR_PATH/configs/settings.example.ini"
			TEST_CFG=../configs/settings.example.ini
		fi
		qalab-core-test-select
  fi	
}
# -------------------------
# CONSTRUCTOR
qalab-core $1 $2
