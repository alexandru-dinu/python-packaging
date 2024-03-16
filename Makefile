SHELL := /usr/bin/bash
SRC := $(shell find ./hello_world/ ./tests/ -name "*.py")

clean:
	rm -rfv *.egg-info __pycache__

test:
	pytest -vv tests/

dev:
	which pip3

format:
	autoflake --remove-all-unused-imports -i $(SRC) \
		&& isort $(SRC) \
		&& black --line-length 100 $(SRC)
