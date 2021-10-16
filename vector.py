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
    :param gamma: scalar factor
    :return: scaled vector (x*gamma, y*gamma, z*gamma)

    """
    return [vector[0]*gamma, vector[1]*gamma, vector[2]*gamma]

def scalar_division(vector, gamma) :

    """

    :param vector: vector (x, y, z)
    :param gamma: scalar factor
    :return: scaled vector (x/gamma, y/gamma, z/gamma)

    """
    return [vector[0]/gamma, vector[1]/gamma, vector[2]/gamma]

def vector_addition(vector, different_vector) :

    """

    :param vector: first vector
    :param different_vector: second vector
    :return: vector sum (vector + different_vector)

    """
    return [vector[0] + different_vector[0], vector[1] + different_vector[1], vector[2] + different_vector[2]]

def vector_subtraction(vector, different_vector) :

    """

    :param vector: first vector
    :param different_vector: second vector
    :return: vector difference (vector - different_vector)

    """
    return [vector[0] - different_vector[0], vector[1] - different_vector[1], vector[2] - different_vector[2]]
