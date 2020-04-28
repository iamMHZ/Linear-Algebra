# this module calculates and plots a simple matrix transformation
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

A = np.array([[1, -3], [3, 5], [-1, 7]])
u = np.array([2, -1])

plt.scatter(*u, c='r')
plt.show()

# calculating matrix transformation
au = np.dot(A, u)
print(au)

axes = plt.axes(projection='3d')
# plot u
axes.scatter(*u, c='r')
# plot the transformed u
axes.scatter(*au, c='b')

plt.show()
