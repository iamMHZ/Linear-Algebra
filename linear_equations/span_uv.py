# This module just plots a matrix and its transpose in the 3D space
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


u = np.array([10, 20, 0])
v = np.array([12, 45, 0])

ax = plt.axes(projection='3d')
ax.scatter(*u, c='r')
ax.scatter(*v, c='r')


# plt.show()

marker_size =0.2

for i in range(20):
    for j in range(20):
        w = u.dot(i) + v.dot(j)

        ax.scatter(*w, c='b', s=marker_size)
        print('INFO: plotting the span')

plt.show()
