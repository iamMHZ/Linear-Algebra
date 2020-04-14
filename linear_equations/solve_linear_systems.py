import pprint

import numpy as np

A = np.array([[13, 5, -4], [-3, -2, 4], [6, 1, -8]])
b = np.array([7, -16, -40])

x = np.linalg.solve(A, b)
pprint.pprint(x)

# below code rises exception for solving linear equation , because the determinant of matrix A is zero

A = np.array([[3, 5, -4], [-3, -2, 4], [6, 1, -8]])
determinant = np.linalg.det(A)
print(f'Determinant of A : {determinant}')
b = np.array([7, 1, -4])

x = np.linalg.solve(A, b)

pprint.pprint(x)
