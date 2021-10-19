"""
Computer Modelling Exercise 1

The purpose of this file is to replicate operations described in the python file vector but using numpy functionality as follows:

(1.) Create 3 random vectors vector1, vector2, vector3 and store them as arrays
(2.) Print out the three vectors and their magnitudes
(3.) The vector sum, dot product and cross product of vector1 and vector2
(4.) Test some vector identities by calculating their left and right hand sides

Date started : 19/10/21
Author : E Forster, s1639706

"""

import numpy as np
import random

def main():

    # Creates three vectors as numpy arrays in form (x, y, z) as in (1.)

    vector1 = np.array([random.random(), random.random(), random.random()])
    vector2 = np.array([random.random(), random.random(), random.random()])
    vector3 = np.array([random.random(), random.random(), random.random()])

    print("\n")
    print(f"Vector 1 : {vector1}")
    print(f"Vector 2 : {vector2}")
    print(f"Vector 3 : {vector3}")

    # Uses numpy functionality to carry out (2.)

    print("\n")
    print("Modulus of Vector 1 : ", np.linalg.norm(vector1))
    print("Modulus of Vector 2 : ", np.linalg.norm(vector2))
    print("Modulus of Vector 3 : ", np.linalg.norm(vector3))

    # Uses numpy functionality to carry out (3.)

    print("\n")
    print("Sum of Vector 1 and Vector 2 : ", np.add(vector1, vector2))
    print("Cross Product of Vector 1 and Vector 2 : ", np.cross(vector1, vector2))
    print("Dot Product of Vector 1 and Vector 2 : ", np.inner(vector1, vector2))

    # Sets up a method using numpy functionality to determine if the LHS of an equation matches the RHS.

    def equality(vector, different_vector):

        if np.isclose(np.all(vector), np.all(different_vector), rtol = 1.e-7, atol = 1.e-8, equal_nan = False):
            print("The vectors are the same.  LHS is equal to RHS. ")

        else:
            print("The vectors are not the same.  LHS does not equal RHS. ")

    # Combines numpy functionality and written method to prove the identities as described in the main print statements, carrying out (4.)

    print("\n")
    lhs1 = np.cross(vector1, vector2)
    rhs1 = np.cross(vector2, vector1)
    print("Is Vector 1 x Vector 2 == - Vector 2 x Vector 1 ? ")
    equality(lhs1, rhs1)

    print("\n")
    lhs2 = np.cross(vector1, np.add(vector2, vector3))
    rhs2 = np.add(np.cross(vector1, vector2), np.cross(vector1, vector3))
    print("Is Vector 1 x (Vector 2 + Vector 3) == (Vector 1 x Vector 2) + (Vector 1 x Vector 3) ? ")
    equality(lhs2, rhs2)

    print("\n")
    lhs3 = np.cross(vector1, np.cross(vector2, vector3))
    rhs3 = vector2 * np.inner(vector1, vector3) - vector3 * np.inner(vector1, vector2)
    print("Is Vector 1 x (Vector 2 x Vector 3) == (Vector 1 x Vector 3)(Vector 2) - (Vector 1 x Vector 2)(Vector 3) ? ")
    equality(lhs3, rhs3)

if __name__ == "__main__":
    main()
