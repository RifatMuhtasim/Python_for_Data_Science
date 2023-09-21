print("Hello Numpy")

import numpy as np


# Create A list in Python
list1 = [1,2,3,4,5]
print(list1)
print(list1[2])


list2 = ["Rifat", "Sakib", list1, "Muhtasim"]
print(list2)


## Using Numpy Array
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print("Shape", np1.shape)
 

## Numpy ARange
np2 = np.arange(10)
print(np2)


## Arange Step
np3 = np.arange(0,10,2)
print(np3)


## Numpy Zeros
np4 = np.zeros(10)
print(np4)


## Multi-Dimensional Zeros
np5 = np.zeros((2,10))
print(np5)


## Numpy Full Function
np6 = np.full((10), 6)
print(np6)


## Multidimensional Full
np7 = np.full((2,10), 1)
print(np7)


## Convert Python List to np
my_list = [2,4,6,8,10]
np8 = np.array(my_list)
print(np8)