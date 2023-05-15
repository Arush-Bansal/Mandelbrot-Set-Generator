import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# arr = np.linspace(-5, 5, 1000)
# arr2 = np.linspace(-5, 5, 1000)
# X, Y = np.meshgrid(arr, arr2)
# print(Y)

def checkConvergence(number : complex, z : complex = 0) -> bool :
    iterNo = 0
    while (abs(z) < 1000) and (iterNo < 100):
        z = z*z + number
        iterNo += 1
    if abs(z) >=1000: return False
    else: return True

def complexMatrix(x_start : float, x_end : float, y_start : float, y_end : float, stepSize: 'float'):
    x_space = np.linspace(x_start, x_end, int((x_end - x_start)/stepSize) + 1)
    y_space = np.linspace(y_start, y_end, int((y_end - y_start)/stepSize) + 1)
    return [[j + i*1j for j in x_space] for i in y_space]


grid = complexMatrix(-2, 0.1, -2, 2, 0.01)
# print(pd.DataFrame(grid))

isConvergent= []
for i in range(len(grid)):
    subConvergent = []
    for j, complex in enumerate(grid[i]):
        subConvergent.append( checkConvergence(complex))
    isConvergent.append(subConvergent)

# print(isConvergent)

# print(isConvergent)
plt.imshow(isConvergent, cmap='hot')
plt.show()