# decotra

This tool saves intermediate objects such as models files in machine learning project s and upload them to S3.

The main features of `Decotra` is provided with Python decorator, and therefore we can easy to add them to the codes and remove them.

We can apply this tool for tracking results of functions on a server and analyzing the calculation process iteratively.

## Requirements

 -  Python >= 3.6

## Install

```shell script
$ pip install decotra
```

When you use local s3 server (such as a minio), please set a environmental parameters `S3_ENDPOINT_URL`.

The following is an example.

`export S3_ENDPOINT_URL=http://s3.foo.co`

## Simple Usage

```python
import decotra

@decotra.track('bucket-name')
def add(a, b):
    return a + b

add(1, 2)
```

## Basic Usage

When uploading file, decotra refers to `decotra.saved_prefix`.
`with decotra.path` will help you to treat `saved_prefix`.

```python
import numpy as np

import decotra

BUCKET_NAME = "bucket-name"


class Operation:
    @decotra.track(BUCKET_NAME)
    def mul(self, x, y):
        return x * y

    @decotra.track(BUCKET_NAME)
    def add(self, x, y):
        return x + y

    @decotra.track(BUCKET_NAME)
    def tanh(self, x):
        return np.tanh(x)


def main():
    op = Operation()
    print(decotra.saved_prefix)  # print current time yyyy-mm-dd-hh-mm-ss format
    
    for e in range(500):
        with decotra.path(f"{decotra.saved_prefix}{e}/"):
            print(op.tanh(op.add(op.mul(1, 2), 3)))


if __name__ == '__main__':
    main()
```

## For developer
<details>

<summary>requirements and how to develop</summary>

### requirements

- S3 environment
- [poetry](https://github.com/python-poetry/poetry)

When you do not have open s3 sandbox, please prepare S3 environment.
For example one member of decotra develper uses [minio](https://min.io) for developing and testing.

### build

Run `poetry build` packs decotra.

### testing

Currently decotra does not have enough testing. If you have nice testing idea, please Pull Requests.

I only check this module working well with running `example/example.py`.

### publish

Run `poetry publish` manually. We set up GitHub Actions and automate to publish by push or merge to master branch.

### other

Some commands are written on `Makefile` (for my memorandum). 

</details>

## Tips

### Q. In debugging, i don't want to upload files and to change own codes. 
__A.__ Set `USE_DECOTRA=-1`.

Before upload files, `decotra` checks environment parameter `USE_DECOTRA`.

You do `export USE_DECOTRA=-1`, you can skip uploading process.