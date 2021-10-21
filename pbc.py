"""
Computer Modelling Exercise 1

The purpose of this file is to use Periodic Boundary Conditions (PBC) and Minimum Image Convention (MIC) to look at points of interest in a cube of edge l.

There will be two main methods :
1.) pbc which given x and l, returns the image of x inside the cube such that 0 <= x < l
2.) mic which given x and l, returns the image of x closest to the origin

Date Started : 19/10/21
Author : E Forster, s1639706

"""

import math
import numpy as np

def pbc(x1, x2, x3, length) :

    x_image = np.array([x1, x2, x3])
    x_real = np.mod(x_image, length)
    print("x inside the cube : ", x_real)

def main() :

    x1 = float(input("Input x1 of x : "))
    x2 = float(input("Input x2 of x : "))
    x3 = float(input("Input x3 of x : "))
    length = int(input("Input chosen length for cube : "))

    pbc(x1, x2, x3, length)


if __name__ == "__main__" :
    main()
