import numpy as np

import decotra
from decotra import track

BUCKET_NAME = "bucket-name"


class Operation:
    @track(BUCKET_NAME)
    def mul(self, x, y):
        return x * y

    @track(BUCKET_NAME)
    def add(self, x, y):
        return x + y

    @track(BUCKET_NAME)
    def tanh(self, x):
        return np.tanh(x)


def main():
    op = Operation()

    for e in range(500):
        with decotra.path(f"{decotra.saved_prefix}{e}/"):
            op.tanh(op.add(op.mul(1, 2), 3))


if __name__ == '__main__':
    main()
