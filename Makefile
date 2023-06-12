.PHONY: clean-pyc clean-build

VENV = venv
PYTHON = $(VENV)\Scripts\python.exe
PIP = $(VENV)\Scripts\pip.exe

$(VENV)\Scripts\activate.bat: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt
	$(PIP) install --upgrade build
	$(PIP) install --upgrade twine

build: $(VENV)/Scripts/activate.bat
	$(PYTHON) -m build

release: build
	twine check dist/*
	twine upload dist/*

clean-build:
	rmdir /s /q build
	rmdir /s /q dist
	rmdir /s /q src/*.egg-info

clean-pyc:
	del /s /q *.pyc
	del /s /q *.pyo
	del /s /q *~

clean: clean-build clean-pyc
	rmdir /s /q $(VENV)
