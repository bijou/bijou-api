PYTHON ?= /usr/bin/env python3

clean:
	rm -rf build *.egg-info dist site

build:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install

default: build

.PHONY: clean build install docs
