import numpy as np

# using genfromtxt()
arr = np.genfromtxt("firstarray.csv",
                    delimiter=",", dtype=str)
print(arr)
