import numpy as np

arr = np.asarray([
    [1, 150, 10.5],
    [2, 220, 3.1],
    [3, 121, 10.1],
    [4, 300, 3.2],
    [5, 541, 6.7],
    [6, 321, 9.9],
])
print(arr)
arr.tofile('all_in_one.csv', sep=',', format='%f')
