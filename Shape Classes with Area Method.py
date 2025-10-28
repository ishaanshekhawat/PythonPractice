import math
import os
import random
import re
import sys

# Define a class for Rectangle
class Rectangle:
    # Constructor (__init__) initializes the length and breadth of the rectangle
    def __init__(self, a, b):
        self.a = a  # Store the length of the rectangle
        self.b = b  # Store the breadth of the rectangle

    # Method to calculate the area of the rectangle (this method should not require parameters)
    def area(self):
        # Calculate and return the area of the rectangle (Area = length * breadth)
        return self.a * self.b

# Define a class for Circle
class Circle:
    # Constructor (__init__) initializes the radius of the circle
    def __init__(self, r):
        self.r = r  # Store the radius of the circle

    # Method to calculate the area of the circle (this method should not require parameters)
    def area(self):
        # Calculate the area using the formula: π * r²
        return math.pi * self.r * self.r
