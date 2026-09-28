import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(10)
print(data)
plt.hist(data, bins=30)
plt.title("Data Distribution")
plt.show()