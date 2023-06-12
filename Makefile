.PHONY: clean-pyc clean-build

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	$(PIP) install --upgrade build
	$(PIP) install --upgrade twine

build: $(VENV)/bin/activate
	$(PYTHON) -m build

release: build
	twine check dist/*
	twine upload dist/*

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr src/*.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-build clean-pyc
	rm -rf $(VENV)