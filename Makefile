SHELL=./make-venv
-include .env
export

# Colours
BLUE:=			\033[0;34m
RED:=			\033[0;31m
LIGHT_RED:=		\033[1;31m
WHITE:=			\033[1;37m
LIGHT_VIOLET := \033[1;35m
NO_COLOUR := 	\033[0m

PROJECT_NAME := 🎵 toolify 🎵

MSG_SEPARATOR := "*********************************************************************"
MSG_IDENT := "    "

.SILENT:

help:
	echo "\n${MSG_SEPARATOR}\n$(LIGHT_VIOLET)$(PROJECT_NAME)$(NO_COLOUR)\n${MSG_SEPARATOR}\n"
	echo "${MSG_IDENT}=======   ✨  BASIC   =====================================\n   "
	echo "${MSG_IDENT}  install                 - ️📩  Install requirements"
	echo "${MSG_IDENT}  test                    -  ✅  Run Unit tests"
	echo "${MSG_IDENT}  run                     -  🚀  Run the app"
	echo "${MSG_IDENT}  run-with-gunicorn       -  🚀  Run the app using gunicorn"

######################################################################
########################   BASIC    #################################
######################################################################
install:
	pip install -r requirements.txt
	echo Requirements installed
ifneq ("$(wildcard .env)","")
	echo env file is already created
else
	cp .env-sample .env
	echo env file created, now you need to fill .env file created with the needed tokens
endif

test:
	echo Running test suite...
	echo
	python -m unittest
	echo
	echo Analyzing code with mypy...
	echo
	mypy source_code/

run:
	flask run

run-with-gunicorn:
	gunicorn --bind localhost:5000 source_code.infrastructure.app:app
