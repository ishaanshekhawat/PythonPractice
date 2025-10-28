import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, a, b):
        return a*b
        
    def area(self, a, b):
        return a*b

class Circle:
    def __init__(self, r):
        self.r = r
        
    def area(self, r):
        return math.pi*r*r

print(Rectangle.area(4,5))
