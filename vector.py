"""
Computer Modelling Exercise 1

The purpose of this file is to create operations which can be used upon vectors.

Date Started : 12/10/21
Author : E Forster, s1639706

"""

import math

def modulus_squared(vector) :

    """
    Modulus Squared

    :param vector: vector (x, y, z)
    :return: square modulus x**2 + y**2 + z**2

    """
    return (vector[0] ** 2) + (vector[1] ** 2) + (vector[2] ** 2)

def modulus(vector) :

    """
    Modulus

    :param vector: vector (x, y, z)
    :return: modulus (x**2 + y**2 + z**2)**(1/2)

    """
    return math.sqrt(modulus_squared(vector))

def scalar_multiplication(vector, gamma) :

    """
    Multiplication of a vector with a scalar, gamma

    :param vector: vector (x, y, z)
    :param gamma: scalar factor, gamma
    :return: scaled vector (x*gamma, y*gamma, z*gamma)

    """
    return [vector[0]*gamma, vector[1]*gamma, vector[2]*gamma]

def scalar_division(vector, gamma) :

    """
    Division of a vector with a scalar, gamma

    :param vector: vector (x, y, z)
    :param gamma: scalar factor, gamma
    :return: scaled vector (x/gamma, y/gamma, z/gamma)

    """
    return [vector[0]/gamma, vector[1]/gamma, vector[2]/gamma]

def vector_addition(vector, different_vector) :

    """
    Addition of two vectors

    :param vector: first vector (x, y, z)
    :param different_vector: second vector (a, b, c)
    :return: vector sum (vector + different_vector)

    """
    return [vector[0] + different_vector[0], vector[1] + different_vector[1], vector[2] + different_vector[2]]

def vector_subtraction(vector, different_vector) :

    """
    Subtraction of two vectors

    :param vector: first vector (x, y, z)
    :param different_vector: second vector (a, b, c)
    :return: vector difference (vector - different_vector)

    """
    return [vector[0] - different_vector[0], vector[1] - different_vector[1], vector[2] - different_vector[2]]

def cross_product(vector, different_vector) :

    """
    Cross Product of two vectors

    :param vector: first vector (x, y, z)
    :param different_vector: second vector (a, b, c)
    :return: vector cross product (vector x different_vector) (y*c - z*b, x*c - z*a, x*b - y*a)

    """
    return [vector[1]*different_vector[2] - vector[2]*different_vector[1], (-1)*(vector[0]*different_vector[2] - vector[2]*different_vector[0]), vector[0]*different_vector[1] - vector[1]*different_vector[0]]

def dot_product(vector, different_vector) :

    """
    Dot product of two vectors

    :param vector: first vector (x, y, z)
    :param different_vector: second vector (a, b, c)
    :return: vector dot product (vector . different_vector) (x*a + y*b + z*c)

    """
    return vector[0]*different_vector[0] + vector[1]*different_vector[1] + vector[2]*different_vector[2]

def equal_vectors(vector, different_vector) :

    """
    Are two vectors the same?

    :param vector: first vector (x, y, z)
    :param different_vector: second vector (a, b, c)
    :return: statement if two vectors are equivalent or not

    """
    threshold = 1.0e-7

    equality = vector_subtraction(vector, different_vector)

    print(f"Is {vector} and {different_vector} the same?")

    if equality[0] < threshold :
        if equality[1] < threshold :
            if equality[2] < threshold :
                print("The vectors are the same.")

            else :
                pass
        else :
            pass

    else :
        print("The vectors are not the same.")
