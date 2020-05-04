import matplotlib.pyplot as plt
import numpy as np

eye = np.eye(2, dtype=np.int)
# print(eye)

scale = 3
transformation_matrix = scale * eye
# print(transformation_matrix)


x = np.linspace(-40, 40, 20)
x = x.reshape((2, -1))
print(x[:, 0])

transformed_x = np.matmul(transformation_matrix, x)

with plt.xkcd():
    plt.scatter(x[0, :], x[1, :], label='x')
    plt.scatter(transformed_x[0, :], transformed_x[1, :], label='transformed')
    plt.legend()
    plt.show()
