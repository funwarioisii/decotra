init:
	poetry install

build:
	poetry build

test:
	- pytest
	- poetry check

prepare-s3-server:
	docker-compose -f docker/docker-compose.yaml up

integration-test:
	export AWS_ACCESS_KEY_ID=accesstoken && \
	export AWS_SECRET_ACCESS_KEY=seacretkey && \
	export S3_ENDPOINT_URL=http://0.0.0.0:9999/ && \
	export PYTHONPATH=$$PYTHONPATH:$(PWD) && \
	python examples/example.py