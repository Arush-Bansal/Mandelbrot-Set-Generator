import cProfile
import pstats

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ctypes
from numba import njit

# lib = ctypes.CDLL(r'\Users\Arush Bansal\OneDrive - IIT Delhi\Desktop\Simulating Mandelbroad Set\isConvergent.exe')
# lib.isConvergent.restype = ctypes.c_bool
# lib.isConvergent.argtypes = [ctypes.c_double, ctypes.c_double]

@njit
def checkConvergence(number : "complex", z : "complex" = 0) -> bool :
    iterNo = 0
    while (abs(z) < 1000) and (iterNo < 100):
        z = z*z + number
        iterNo += 1
    if abs(z) >=1000: return False
    else: return True
    # return lib.isConvergent(number.real, number.imag)

def linSpace(a, b, c):
    return np.linspace(a, b, c)

def complexMatrix(x_start : float, x_end : float, y_start : float, y_end : float, stepSize: 'float'):
    x_space = linSpace(x_start, x_end, int((x_end - x_start)/stepSize) + 1)
    y_space = linSpace(y_start, y_end, int((y_end - y_start)/stepSize) + 1)
    # matrix_dimension = int((x_end - x_start)/stepSize) + 1, int((y_end - y_start)/stepSize) + 1
    # matrix = np.zeros(matrix_dimension, np.complex512)
    # for i in range(len(matrix)):
    #     for j in range(len)

    # return [[j + i*1j for j in x_space] for i in y_space]
    return 1j * y_space[:, np.newaxis] +  x_space[np.newaxis, :]


def getConvergentMatrix(grid):
    return np.zeros((len(grid), len(grid[0])),dtype=bool)

@njit
def iterateOverConvergentMatrix(grid, isConvergent):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            isConvergent[i][j] = checkConvergence(grid[i][j])

def complexMatrixWrapper(grid):
    # isConvergent = np.vectorize(checkConvergence)(grid)
    # vectorCheckConvergence = np.vectorize(checkConvergence)

    # return vectorCheckConvergence(grid)

    isConvergent = getConvergentMatrix(grid)
    iterateOverConvergentMatrix(grid, isConvergent)

    return isConvergent




def main():

    grid = complexMatrix(-3, 1, -2, 2, 0.001)
    # print(pd.DataFrame(grid))
    isConvergent = complexMatrixWrapper(grid)

    # isConvergent= []
    # for i in range(len(grid)):
    #     subConvergent = []
    #     for j, complex in enumerate(grid[i]):
    #         subConvergent.append( checkConvergence(complex))
    #     isConvergent.append(subConvergent)
    plt.imshow(isConvergent, cmap='hot')
    plt.show()



if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.reverse_order()
    # stats.print_stats()
    stats.dump_stats(filename="hey.prof")
    # self reminder to use command "python -m snakeviz hey.prof" in command line to run the file

    

