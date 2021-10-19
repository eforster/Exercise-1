"""
Computer Modelling Exercise 1

The purpose of this file is to replicate operations described in the python file vector but using numpy functionality.

Date started : 19/10/21
Author : E Forster, s1639706

"""

import numpy as np
import random
import math

def main() :


    vector1 = np.array([random.random(), random.random(), random.random()])
    vector2 = np.array([random.random(), random.random(), random.random()])
    vector3 = np.array([random.random(), random.random(), random.random()])

    print("\n")
    print(f"Vector 1 : {vector1}")
    print(f"Vector 2 : {vector2}")
    print(f"Vector 3 : {vector3}")

    print("\n")
    print("Modulus of Vector 1 : ", np.linalg.norm(vector1))
    print("Modulus of Vector 2 : ", np.linalg.norm(vector2))
    print("Modulus of Vector 3 : ", np.linalg.norm(vector3))

    print("\n")
    print("Sum of Vector 1 and Vector 2 : ", np.add(vector1, vector2))
    print("Cross Product of Vector 1 and Vector 2 : ", np.cross(vector1, vector2))
    print("Dot Product of Vector 1 and Vector 2 : ", np.inner(vector1, vector2))

    print("\n")
    

if __name__ == "__main__" :
    main()