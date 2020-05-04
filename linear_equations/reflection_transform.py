# this module shows the reflection transform on the unit square
import matplotlib.pyplot as plt
import numpy as np


def plot_rectangle(start_x, end_x, end_y, start_y, label, color='blue'):
    rect = plt.Rectangle((start_x, start_y), end_x, end_y, fc=color, label=label)
    plt.gca().add_patch(rect)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)


'''
    x =  start_x  start_y
          width   height   
          
    of the square      
'''

x = np.array([[0, 1], [1, 0]])
transformation_matrix = np.array([[-1, 0], [0, -1]])

transformed_x = np.matmul(x, transformation_matrix)

# plotting
fig = plt.figure()
plot_rectangle(*np.ravel(x, order='F'), label='x')
plot_rectangle(*np.ravel(transformed_x, order='F'), label=' transformed', color='red')

fig.legend()
fig.show()
