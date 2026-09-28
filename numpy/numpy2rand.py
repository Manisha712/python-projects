import numpy as np
arr1=np.array([[1,2],
              [4,5],
              [7,8]])
# 1. Grab a single specific value (Row Index 0, Column Index 0)
print("Single Value:", arr1[0, 0])
print("Single Value:", arr1[2, 1])
# 2. Grab an ENTIRE row (Row Index 0 -> )
print("First Row:", arr1[0, :])
# 3. Grab an ENTIRE column (Column Index 1 across all rows -)
print("Second Column:", arr1[:, 1])
print(arr1[:])
#RUle: Slicing syntax start:stop includes the start index, but excludes the stop index.
print(arr1[0:2, 1:3])

arr3=arr1.reshape(2, 3)
print(arr3)


arr5 = np.random.randint(1, 10, size=(5,10))

print(arr5)


print(np.zeros((3, 3)))
print(np.ones((2, 5)))

arr6 =np.arange(15) #(0,n-1)
print(arr6)

#np.arange(0, 10, 2)  #you contol step not how many nummber
#np.linspace(start, stop, num) # you controll number

print(np.linspace(0, 10, 5))
print(np.linspace(0, 10, 4))