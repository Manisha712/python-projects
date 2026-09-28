import numpy as np
#1d array
numbers = [1, 2, 3, 4, 5]
arr = np.array([1, 2, 3, 4, 5])
doubled_arr = arr * 2
print("Doubled Array:", doubled_arr)

# 3. Reshaping Data (1D Array into a 2D Matrix: 2 rows, 3 columns)
flat_data = np.array([1, 2, 3, 4, 5, 6])
matrix = flat_data.reshape(2, 3)
print("\nReshaped 2D Matrix:\n", matrix)
print("\nMatrix Shape:", matrix.shape)

#2d array
matrix= np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr)
print(matrix)

print(matrix.shape) #(3,4)