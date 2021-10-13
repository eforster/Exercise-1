"""

Computer Modelling Exercise 1

The purpose of this file is to test the Vector class in vector.py

Date started : 12/10/21
Author : E Forster, s1639706

"""

import math
import random
import vector


def main() :

    vector1 = [(random.random(), random.random(), random.random())]
    vector2 = [(random.random(), random.random(), random.random())]

    print(f"Vector 1 : {vector1}")
    print(f"Vector 2 : {vector2}")


    v1 = [1, 1, 1]
    v2 = [1, 1, 1]
    gamma = 2

    print("Modulus squared v1 : ", vector.modulus_squared(v1))
    print("Modulus v1 : ", vector.modulus(v1))
    print("Scalar multiplication of v1 : ", vector.scalar_multiplication(v1, gamma))
    print("Scalar division of v1 : ", vector.scalar_division(v1, gamma))
    print("v1 + v2 sum : ", vector.vector_addition(v1, v2))
    print("v1 - v2 difference : ", vector.vector_subtraction(v1, v2))



if __name__ == "__main__":
    main()
