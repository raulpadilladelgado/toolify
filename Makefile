SHELL=./make-venv
-include .env
export

.SILENT:

help:
	echo =======   ✨  BASIC   =====================================
	echo install                 - ️📩  Install requirements
	echo test                    -  ✅  Run Unit tests
	echo run                     -  🚀  Run the app
	echo run-with-gunicorn       -  🚀  Run the app using gunicorn

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
	mypy source_code/ --strict

run:
	flask run

run-with-gunicorn:
	gunicorn --bind localhost:5000 source_code.infrastructure.app:app
