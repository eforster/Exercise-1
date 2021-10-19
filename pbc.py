"""

The purpose of this file is to use Periodic Boundary Conditions (PBC) and Minimum Image Convention (MIC) to look at points of interest in a cube of edge l.

There will be two main methods :
- pbc which given x and l, returns the image of x inside the cube such that 0 <= x < l
- mic which given x and l, returns the image of x closest to the origin

Date Started : 19/10/21
Author : E Forster, s1639706

"""