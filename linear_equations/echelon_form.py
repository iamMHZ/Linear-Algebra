# this module computes the echelon and reduced echelon form of a linear system


import pprint

from sympy import Matrix

matrix = Matrix([[0, 3, -6, 6, 4, -5], [3, -7, 8, -5, 8, 9], [3, -9, 12, -9, 6, 15]])

pprint.pprint(matrix)

# compute echelon form
print('\nEchelon form:')
echelon_form = matrix.echelon_form()
pprint.pprint(echelon_form)

print('\nReduced echelon form and pivot columns:')
# reduced echelon form:
reduced_echelon_form = matrix.rref()
pprint.pprint(reduced_echelon_form)
