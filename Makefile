HERE = $(shell pwd)
VENV = $(HERE)/venv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python

init:
	virtualenv $(VENV)
	$(BIN)/pip install -r requirements.txt -i http://pypi.douban.com/simple/

unittest:
	$(BIN)/py.test tests
