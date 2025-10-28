import math
import os
import random
import re
import sys

# Define a class for Rectangle
class Rectangle:
    # Constructor (__init__) initializes the dimensions of the rectangle (a and b)
    def __init__(self, a, b):
        # The constructor should store the dimensions of the rectangle, not return a value.
        # Returning a value here is incorrect.
        return a * b  # This should not be in the constructor. Constructors should initialize the object state.

    # Method to calculate the area of the rectangle (takes two parameters)
    def area(self, a, b):
        # Calculate and return the area of the rectangle (Area = length * breadth)
        return a * b

# Define a class for Circle
class Circle:
    # Constructor (__init__) initializes the radius of the circle (r)
    def __init__(self, r):
        self.r = r  # Store the radius value

    # Method to calculate the area of the circle
    def area(self, r):
        # Use the formula for the area of a circle: π * r²
        return math.pi * r * r
