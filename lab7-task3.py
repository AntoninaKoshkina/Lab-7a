import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3*np.pi,  3*np.pi, 100)

X, Y = np.meshgrid(x, np.cos(x))

Z = X/np.sin(X)

Z[Z > 10] = np.nan
Z[Z < -10] = np.nan

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_zlim(-10, 10)

ax.set_title('y=cos(x); z=x/sin(x)')
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')

plt.show()