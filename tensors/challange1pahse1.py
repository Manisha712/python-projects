import numpy as np
import torch
#Create a 4x4 NumPy array containing numbers 1 through 16.
# 1. Create a flat 1D array of numbers 1 through 16 (17 is exclusive)
flat_array = np.arange(1, 17)

# 2. Reshape it into a 4x4 matrix
narry1 = flat_array.reshape(4, 4)
print("4x4 Matrix:\n", narry1)
#Reshape it into a 4x4 matrix using .reshape(4, 4)
narry2=narry1.reshape(4,4)
print(narry2)

#Extract the inner 2x2 square (numbers 6, 7, 10, 11) using slicing.
print(narry1[1:3, 1:3])

#Calculate the average of each column using axis=0.
print("average:",narry1.mean(axis=0))
