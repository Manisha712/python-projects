import numpy as np
import torch

np_matrix = np.array([
    [10.0, 20.0, 30.0],
    [40.0, 50.0, 60.0]
])

# 2. Convert to a PyTorch Tensor
tensor_matrix = torch.from_numpy(np_matrix)
print("Tensor Output:\n", tensor_matrix)

print("Shape:", tensor_matrix.shape)        # Rows and columns tracking
print("Data Type:", tensor_matrix.dtype)    # Numerical precision (e.g., float64)
print("Device:", tensor_matrix.device)      # Where the tensor lives (CPU or CUDA/GPU)

# Multiply every element by 2
tensor_doubled = tensor_matrix * 2

# Perform matrix aggregation (sum across columns)
column_sums = torch.sum(tensor_matrix, dim=0)
# 'dim' in PyTorch is equivalent to 'axis' in NumPy

print("\nDoubled Tensor:\n", tensor_doubled)
print("Column Sums:", column_sums)

#Note: In PyTorch, axes are referred to as dim (dimensions). So axis=0 in NumPy becomes dim=0 in PyTorch.
tensor_float32 = tensor_matrix.float()

print(tensor_float32.dtype)