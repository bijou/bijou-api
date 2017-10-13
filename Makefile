PYTHON ?= /usr/bin/env python3

clean:
	$(MAKE) -C docs clean
	rm -rf build *.egg-info dist site docs/*.auto.rst

build:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install

docs:
	sphinx-apidoc --no-toc -s auto.rst -o docs bijou
	$(MAKE) -C docs html

default: build

.PHONY: clean build install docs
