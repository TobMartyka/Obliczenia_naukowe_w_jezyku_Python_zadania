import matplotlib.pyplot as plt
import numpy as np

#Parameters
L = 1.0
Nx = 100
Nt = 500
D = 0.04
T = 0.1

t = np.linspace(0, T, num=Nx+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)
dx = x[1] - x[0]
dt = t[1] - x[0]
r = D*dt/(dx*dx)
print("r={}".format(r))
assert r < 0.5
u = np.zeros((Nx+1,Nt+1), dtype=float )

#initial condition
u[:,0] = np.where(x < 0.5, 2*x, 2*(1-x))

#boundary condition
u[0,:] = 0.0
u[Nx,:] = 1.0

for j in range(Nt):
    u[1:-1,j+1] = r*u[0:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]

print(u)
plt.title("1D heat equation")
plt.xlabel("t")
plt.ylabel("x")

plt.imshow(u[:,::3], cmap='hot', interpolation='nearest')

plt.colorbar()
plt.show()
