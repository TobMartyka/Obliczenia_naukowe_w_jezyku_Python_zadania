import numpy as np
import matplotlib.pyplot as plt

n = 100

x = np.random.rand(n)
y = np.random.rand(n)

distances = np.sqrt(x**2 + y**2)
colors = ['green' if dist <= 1 else 'red' for dist in distances]

marker_sizes = (x + y) * 100

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=marker_sizes, alpha=0.5)

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Points in a Unit Square')

plt.show()
