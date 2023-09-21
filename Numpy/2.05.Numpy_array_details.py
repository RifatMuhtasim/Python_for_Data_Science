import numpy as np

## Shape and Reshape
# Create 1-D Numpy array and Reshape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

# Create 2-D Numpy array and get Shape (rows/columns)
np2 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
print(np2)
print(np2.shape)

# Reshape 2-D
np3 = np1.reshape(4,3)
print(np3)

# Reshpae 3-D
np4 = np1.reshape(2,2,3)
print("np4", np4)

# Flatten to 1-D
np5 = np4.reshape(-1)
print(np5)



## Iterating through Numpy Array
# 1-D Array
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
for x in arr1:
   print(x)

# 2-D Array
arr2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
for x in arr2:
   for y in x:
      print(y)

# 3-D Array
arr3 = np.array([[[1,2,3],[2,5,6]],[[7,8,9],[10,11,12]]])
for x in arr3:
   for y in x:
      for z in y:
         print(z)

# Using np.nditer()
print("np.nditer()")
for x in np.nditer(arr3):
   print(x)
