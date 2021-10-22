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

    # The following gives the 'real' particle x that lies inside the cube of length given by the user.

    x_image = np.array([x1, x2, x3])
    x_real = np.mod(x_image, length)        # np.mod gives the remainder of x_image / length, which is the point inside the cube
    return x_real


def mic(x1, x2, x3, length):

    # The following calculates the 8 particles that lie around the origin, including the 'real' particle that exists in the first quadrant

    x_real = np.array(pbc(x1, x2, x3, length))

    x_image1 = x_real + np.array([0, 0, -length])

    x_image2 = x_real + np.array([-length, 0, -length])

    x_image3 = x_real + np.array([0, -length, 0])

    x_image4 = x_real + np.array([-length, -length, 0])

    x_image5 = x_real + np.array([-length, 0, -length])

    x_image6 = x_real + np.array([0, -length, -length])

    x_image7 = x_real + np.array([-length, -length, -length])

    # The following creates an array of all images distance to the origin

    images = np.array([np.linalg.norm(x_real),
                       np.linalg.norm(x_image1),
                       np.linalg.norm(x_image2),
                       np.linalg.norm(x_image3),
                       np.linalg.norm(x_image4),
                       np.linalg.norm(x_image5),
                       np.linalg.norm(x_image6),
                       np.linalg.norm(x_image7)])

    # The following gives the minimum distances from the images array and returns it, giving x closest to the origin

    x_near_origin = np.amin(images)

    return x_near_origin

def main() :

    # The terminal will prompt the user for the three components of x and the cube length

    x1 = float(input("Input x1 of x : "))
    x2 = float(input("Input x2 of x : "))
    x3 = float(input("Input x3 of x : "))
    length = int(input("Input chosen length for cube : "))

    # Given x and length, the image of x inside the cube such that 0 <= x_i < length is calculated and printed to terminal

    print("x inside the cube (0 <= x_i < length) : ", pbc(x1, x2, x3, length))

    # Given x and length, the image of x closest to the origin is calculated and printed to the terminal

    print("x closest to the origin : ", mic(x1, x2, x3, length))


if __name__ == "__main__" :
    main()
    