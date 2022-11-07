import numpy as np

# Reading csv file into numpy array
file_data = open('firstarray.csv')
l = []
for row in file_data:
    r = list(np.fromstring(row, sep=","))
    l.append(r)
# printing the array
print(np.array(l))
