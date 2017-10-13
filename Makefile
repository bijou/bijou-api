PYTHON ?= /usr/bin/env python3

clean:
	$(MAKE) -C docs clean
	rm -rf build *.egg-info dist site

build:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install

docs:
	$(MAKE) -C docs html

default: build

.PHONY: clean build install docs
