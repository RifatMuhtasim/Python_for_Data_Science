import numpy as np 

## Copy Vs View
np1 = np.array([0,1,2,3,4,5])


## Create A View (Change both np1 and np2)
# np2 = np1.view()
np2 = np1
print(f'Original NP1 is: {np1} and Original NP2 is: {np2}')
np2[0] = 12
print(f'Changed NP1 is: {np1} and Original NP2 is: {np2}')


## Create a Copy (Change only)
np2 = np1.copy()
print(f'Original NP1 is: {np1} and Original NP2 is: {np2}')
np1[0] = 74
print(f'Changed NP1 is: {np1} and Original NP2 is: {np2}')