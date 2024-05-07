import numpy as np


m1 = np.arange(20).reshape(4, 5)
print("m1: Two-dimensional array with shape (4,5)")
print(m1)

m2 = m1[:, ::-1]
print("m2: m1 rows in reverse order:")
print(m2)

m3 = m1[::-1, :]
print("m3: m1 columns in reverse order: ")
print(m3)

m4 = m1[1:-1, 1:-1]
print("m4: m1 without outer rows and columns):")
print(m4)

