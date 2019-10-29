# decotra

Save a intermediate product and upload to S3.

Decotra's main feature is concreted with decorator, so it is easy to code and to remove.

In my use case, tracking many results of functions on server and upload to S3(I use minio), analyzing the calculation process ad hoc.

## Requirements

 -  Python >= 3.6

## Install

```shell script
$ pip install decotra
```

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