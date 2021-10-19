"""
Computer Modelling Exercise 1

The purpose of this file is to test the vector methods in the python file vector.  It will:

(1.) Create 3 random vectors vector1, vector2, vector3 and store them as lists
(2.) Print out the three vectors and their magnitudes
(3.) The vector sum, dot product and cross product of vector1 and vector2
(4.) Test some vector identities by calculating their left and right hand sides

Date started : 12/10/21
Author : E Forster, s1639706

"""

import random
import vector

def main() :

    # Creates the three random vectors as a list in form (x, y, z) as in (1.)

    vector1 = [random.random(), random.random(), random.random()]
    vector2 = [random.random(), random.random(), random.random()]
    vector3 = [random.random(), random.random(), random.random()]

    print("\n")
    print(f"Vector 1 : {vector1}")
    print(f"Vector 2 : {vector2}")
    print(f"Vector 3 : {vector3}")

    # Uses methods to carry out (2.)

    print("\n")
    print("Modulus of Vector 1 : ", vector.modulus(vector1))
    print("Modulus of Vector 2 : ", vector.modulus(vector2))
    print("Modulus of Vector 3 : ", vector.modulus(vector3))

    # Uses the more complex methods to carry out (3.)

    print("\n")
    print("Sum of Vector 1 and Vector 2 : ", vector.vector_addition(vector1, vector2))
    print("Cross Product of Vector 1 and Vector 2 : ", vector.cross_product(vector1, vector2))
    print("Dot Product of Vector 1 and Vector 2 : ", vector.dot_product(vector1, vector2))

    # Combines methods to prove the identities as described in the main print statements, carrying out (4.)

    print("\n")
    lhs1 = vector.cross_product(vector1, vector2)
    rhs1 = vector.cross_product((vector.scalar_multiplication(vector2, -1)), vector1)
    print("Is Vector 1 x Vector 2 == - Vector 2 x Vector 1 ?  I.e. : ")
    vector.equal_vectors(lhs1, rhs1)

    print("\n")
    lhs2 = vector.cross_product(vector1, (vector.vector_addition(vector2, vector3)))
    rhs2 = vector.vector_addition(vector.cross_product(vector1, vector2), vector.cross_product(vector1, vector3))
    print("Is Vector 1 x (Vector 2 + Vector 3) == (Vector 1 x Vector 2) + (Vector 1 x Vector 3) ?  I.e. : ")
    vector.equal_vectors(lhs2, rhs2)

    print("\n")
    lhs3 = vector.cross_product(vector1, vector.cross_product(vector2, vector3))
    rhs3 = vector.vector_subtraction(vector.scalar_multiplication(vector2, vector.dot_product(vector1, vector3)), vector.scalar_multiplication(vector3, vector.dot_product(vector1, vector2)))
    print("Is Vector 1 x (Vector 2 x Vector 3) == (Vector 1 x Vector 3)(Vector 2) - (Vector 1 x Vector 2)(Vector 3) ? I.e. : ")
    vector.equal_vectors(lhs3, rhs3)

if __name__ == "__main__" :
    main()
