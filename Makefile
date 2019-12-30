init:
	poetry install

build:
	poetry build

test:
	- pytest
	- poetry check
