import numpy as np

## Slicing Numpy Array
np1 = np.array([1,2,3,4,5,6,7,8,9])

## Return 3,4,5,6,7
print(np1[2:7])

## Return from somethings till the end of the array? (3-9)
print(np1[2:])

## Return Negative Slicing [7,8]
print(np1[-3:-1])

## Steps
print(np1[1:7:2])

## Steps on the entire array
print(np1[::2])
print(np1[::3])


## Slicing a 2D Array
np2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
## Pull out a single item
print(np2[1][3])
print(np2[1,3])

## Slicing from both Rows 
print(np2[0:2, 1:3])



