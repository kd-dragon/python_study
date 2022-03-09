import numpy as np
import timeit


arr = np.arange(1e7)
#list = arr.tolist()


def list_times(alist, mul):
    for i, val in enumerate(alist):
        alist[i] = val * mul
    return alist


starttime2 = timeit.default_timer()
arr * 2
print("numpy array costs : ", timeit.default_timer() - starttime2)

