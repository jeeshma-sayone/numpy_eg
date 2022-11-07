# Imports
import numpy as np

# Let's create a numpy array
nparray = np.array([[1, 2, 4],[1, 3, 9],[1, 4, 16]])

# Saving the array
np.savetxt("firstarray.csv", nparray, delimiter=",")

# Reading the csv into an array
firstarray = np.genfromtxt("firstarray.csv", delimiter=",")

print(firstarray)