import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 400)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_exp = np.exp(-x)

plt.figure(figsize=(8, 5))

plt.plot(x, y_sin, color='red', linestyle='-', label='sin(x)')
plt.plot(x, y_cos, color='green', linestyle='--', label='cos(x)')
plt.plot(x, y_exp, color='blue', linestyle=':', label='exp(-x)')

plt.legend()

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(x), cos(x), and exp(-x)')

plt.show()
