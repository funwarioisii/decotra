# decotra

Save a intermediate product and upload to S3.

`Decotra`'s main feature is concreted with decorator, so it is easy to code and to remove.

In my use case, tracking many results of functions on server and upload to S3 (I use minio), analyzing the calculation process ad-hoc.

## Requirements

 -  Python >= 3.6

## Install

```shell script
$ pip install decotra
```

and if you use local s3 server (like a minio), please set a environmental parameters `S3_ENDPOINT_URL`.

Example.

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

When uploading file, decotra refers to decotra.saved_prefix.
`with decotra.path` will help you to treat save_prefix.

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

## for developer

### requirements
- S3 environment
- [poetry](https://github.com/python-poetry/poetry)

I don't have open s3 sandbox.
Please prepare S3 environment.
I use [minio](https://min.io) for developing and testing.

### build
Run `poetry build`, you'll pack decotra.

### testing
Sorry, Work In Progress. If you have nice testing idea, please Pull Requests.

I only check this module working well with running `example/example.py`.

### publish
Now, I run `poetry publish` manually.
I'll set up GitHub Actions and automate to publish by push or merge to master branch.

## tips
### Q. In debugging, i don't want to upload files and to change own codes. 
__A.__ Set `USE_DECOTRA=-1`.

Before upload files, `decotra` checks environment parameter `USE_DECOTRA`.

You do `export USE_DECOTRA=-1`, you can skip uploading process.