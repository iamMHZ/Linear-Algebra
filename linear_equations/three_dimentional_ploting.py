# This module just plots a matrix and its transpose in the 3D space
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


v = np.array([12, 55, 99])
ax = plt.axes(projection='3d')
ax.scatter(*v, 'blue')

plt.show()
