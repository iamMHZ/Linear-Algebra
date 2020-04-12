# This module just plots a matrix and its transpose in the 3D space
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


matrix = np.array([[12, 55, 99], [78, 34, 3], [3, 50, 70]])
matrix_transpose = matrix.transpose()
ax = plt.axes(projection='3d')
ax.scatter(matrix[:1, :], matrix[1:2, :], matrix[2:3, :], 'blue')
ax.scatter3D(matrix_transpose[:1, :], matrix_transpose[1:2, :], matrix_transpose[2:3, :], 'red')

plt.show()
