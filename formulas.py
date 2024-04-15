# f(p, a, m) => get vector terminus

import numpy as np
import matplotlib.pyplot as plt

# Define the grid of points where you want to calculate the vector field
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)

# Define the vector components at each point
U = X  # x-component of the vector field
V = Y  # y-component of the vector field

# Create a quiver plot to visualize the vector field
plt.quiver(X, Y, U, V, scale=20)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
