import numpy as np

# using loadtxt()
arr = np.loadtxt("firstarray.csv",
                 delimiter=",", dtype=str)
print(arr)
