import numpy as np 

np1 = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np1)

## Square Route of Each Elements
print("Sqrt", np.sqrt(np1))

## Absolute Value
print("Absolute", np.absolute(np1))

## Exponents
print("Exponents", np.exp(np1))

## Min/Max
print("Max", np.max(np1))
print("Min", np.min(np1))

## Sign Positive or Negative
print(np.sign(np1))

## Trig, Sin, Cos, Log
print("Sin", np.sin(np1))