SHELL=./make-venv
-include .env
export

# Get the absolute path to the running Makefile
ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# Colours
BLUE:=			\033[0;34m
RED:=			\033[0;31m
LIGHT_RED:=		\033[1;31m
WHITE:=			\033[1;37m
LIGHT_VIOLET := \033[1;35m
NO_COLOUR := 	\033[0m

# Environment : { dev, staging, prod }
ENV := dev

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
	cp .env-sample .env
	echo Requirements installed, now you need to fill .env file created with the needed tokens

test:
	python3 -m unittest

run:
	flask run

run-with-gunicorn:
	gunicorn --bind 0.0.0.0\:5000 source_code.infrastructure.app\:app
