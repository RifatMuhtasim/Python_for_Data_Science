import numpy as np 

## Sorting Numpy - It's create a copy method not a view one
# Numerical
np1 = np.array([5,3,6,1,8,0])
print(np1)
print(np.sort(np1))

# Alphabatical
np2 = np.array(["Babu", "Alam",   "Zakir", "Rahim", "Nayem"])
print(np2)
print(np.sort(np2))

# Booleans T/F
np3 = np.array([True, True, False, False, True, True])
print(np3)
print(np.sort(np3))

# Sorting 2-D Numpy Array
np4 = np.array([[5,6,2],[1,9,3]])
print(np4)
print(np.sort(np4))



## Searching Numpy Array
# Find index number of the number 2
print("Search")
np5 = np.array([4,2,5,2,5,1,5,7,2,8,2,5,7])
x = np.where(np5 == 2)
print(np5)
print(x[0])

# Return Even Number index value
y = np.where(np5 %2 == 0)
print(y[0])

# Return Odd Number index value
z = np.where(np5 %2 == 1)
print(z[0])



## Filtering Numpy array
print("Filtering")
data = np.array([3,5,2,6,1,8,2,9,2,8,2,7,9,4,5,7,0,1,3])

filt = []
for i in data:
   if i%2 == 0:
      filt.append(True)
   else:
      filt.append(False)

print(data)
print(filt)
print(data[filt])


# Numpy Shortcut
filtered = data > 5
print(data[filtered])