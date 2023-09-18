import numpy as np
def madelung(L):
    r = np.math.floor(L ** (1 / 3)/2)# find the half of the length of each side of the cube
    # Generate arrays of indices using numpy
    i, j, k = np.meshgrid(np.arange(-r, r+1), np.arange(-r,r+1), np.arange(-r,r+1))

    # Mask the (0, 0, 0) point
    mask = (i != 0) | (j != 0) | (k != 0)

    distance = np.sqrt(i**2 + j**2 + k**2)
    sign = (-1.0) ** (i + j + k)

    # Calculate the Madelung constant
    x = np.sum(sign[mask] / distance[mask])

    return abs(x)
print("The Madelung constant of NaCl is",madelung(100))