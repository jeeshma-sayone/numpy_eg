"""
It creates an array by using the evenly spaced values over the given interval. The syntax to use the function is given below.

numpy.arrange(start, stop, step, dtype)
It accepts the following parameters.

start: The starting of an interval. The default is 0.
stop: represents the value at which the interval ends excluding this value.
step: The number by which the interval values change.
dtype: the data type of the numpy array items.
"""

import numpy as np

arr = np.arange(0, 10, 2, float)
print(arr)
