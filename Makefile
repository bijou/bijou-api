PYTHON ?= /usr/bin/env python3
DOCS ?= html

clean:
	$(MAKE) -C docs clean
	rm -rf build *.egg-info dist site htmlcov docs/*.auto.rst

build:
	$(PYTHON) setup.py build

test:
	$(PYTHON) -m tox

install:
	$(PYTHON) setup.py install

docs:
	sphinx-apidoc --no-toc -s auto.rst -o docs bijou *tests*
	$(MAKE) -C docs $(DOCS)

default: build

.PHONY: clean build test install docs
