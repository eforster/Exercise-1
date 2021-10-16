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

    vector1 = [random.random(), random.random(), random.random()]
    vector2 = [random.random(), random.random(), random.random()]
    vector3 = [random.random(), random.random(), random.random()]

    print(f"Vector 1 : {vector1}")
    print(f"Vector 2 : {vector2}")
    print(f"Vector 3 : {vector3}")

    gamma = random.random()

    # print("Modulus squared of Vector 1 : ", vector.modulus_squared(vector1))
    print("Modulus of Vector 1 : ", vector.modulus(vector1))
    print("Modulus of Vector 2 : ", vector.modulus(vector2))
    print("Modulus of Vector 3 : ", vector.modulus(vector3))
    # print("Scalar multiplication of Vector 1 : ", vector.scalar_multiplication(vector1, gamma))
    # print("Scalar division of Vector 1 : ", vector.scalar_division(vector1, gamma))
    print("Sum of Vector 1 and Vector 2 : ", vector.vector_addition(vector1, vector2))
    # print("The difference between Vector 1 and Vector 2 : ", vector.vector_subtraction(vector1, vector2))


if __name__ == "__main__" :
    main()
