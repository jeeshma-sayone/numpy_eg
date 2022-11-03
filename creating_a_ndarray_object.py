import numpy as np

a = ["J", "E", "E", "S", "H", "M", "A"]

a = np.array(a)
print(a)
print(type(a))
print(a.ndim)  # ndim function can be used to find the dimensions of the array.
print("Each item contains", a.itemsize,
      "bytes")  # to get the size of each array item. It returns the number of bytes taken by each array element
print("Each item is of the type", a.dtype)  # To check the data type of each array item, the dtype function is used
print("Array Size:", a.size)
print("Shape:",
      a.shape)  # To get the shape and size of the array, the size and shape function associated with the numpy array is used
line_sp = np.linspace(5, 15, 10)  # prints 10 values which are evenly spaced over the given interval 5-15
print(line_sp)
a = np.array([1, 2, 3, 10, 15, 4])
print("The array:", a)
print("The maximum element:", a.max())
print("The minimum element:", a.min())
print("The sum of the elements:", a.sum())

