import matplotlib.pyplot as plt
import numpy as np

u = np.array([10, 20])

for i in range(100):
    w = u.dot(i)
    print(w)
    plt.scatter(*w, c='r')

# plt.xlim(0, 100)
plt.grid()
# plt.ylim(0, 100)
plt.show()
