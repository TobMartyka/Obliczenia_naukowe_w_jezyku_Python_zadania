import matplotlib.pyplot as plt
import numpy as np

#Parameters
L = 1.0
T = 1.0
Nx = 100
Nt = 300
c = 1.0
dx = L / Nx
dt = T / Nt

courant_number = c * dt / dx
assert courant_number <= 1

x = np.linspace(0, L, Nx+1)
t = np.linspace(0, T, Nt+1)

u = np.zeros((Nx+1, Nt+1))

u[:, 0] = np.sin(np.pi * x)

u[1:-1, 1] = u[1:-1, 0] + 0.5 * courant_number**2 * (u[2:, 0] - 2*u[1:-1, 0] + u[:-2, 0])

u[0, :] = 0
u[Nx, :] = 0

for n in range(1, Nt):
    u[1:-1, n+1] = 2*(1 - courant_number**2) * u[1:-1, n] - u[1:-1, n-1] + \
                   courant_number**2 * (u[2:, n] + u[:-2, n])


plt.imshow(u, cmap='hot', interpolation='nearest')

plt.title("1D Wave Equation")
plt.xlabel("t")
plt.ylabel("X")
plt.colorbar()
plt.show()
