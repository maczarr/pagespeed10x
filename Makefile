all: init test

init:
	pip install -r requirements.txt

test:
	nose2 -v

.PHONY: all init test