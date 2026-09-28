#Challenge 2: Tensor Conversion Pipeline


#Calculate the maximum grade across each row
#using torch.max(tensor, dim=1)

import numpy as np
import torch
from dateutil.tz.win import valuestodict

#Create a 3x3 NumPy matrix representing student grades.
nump_matrix = np.random.randint(20, 100, size=(3,3))
print(nump_matrix)
#Convert it into a PyTorch Tensor using torch.from_numpy().
tor_matrix= torch.from_numpy(nump_matrix)
print(tor_matrix)
#Calculate the maximum grade across each row
# #using torch.max(tensor, dim=1)

max_score = torch.max(tor_matrix,dim=1).values
print("Max scores only:", max_score)


