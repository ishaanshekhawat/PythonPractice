import math

# Define a class to represent a point (or vector) in 3D space
class Points(object):
    def __init__(self, x, y, z):
        # Initialize a point with x, y, z coordinates
        self.x = x
        self.y = y
        self.z = z
    
    def __sub__(self, no):
        # Define subtraction between two Points (vector subtraction)
        # Returns a new Point representing the difference of coordinates
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        # Compute the dot product of two vectors
        return self.x * no.x + self.y * no.y + self.z * no.z
    
    def cross(self, no):
        # Compute the cross product of two vectors
        # Returns a new Point
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )
    
    def absolute(self):
        # Compute the magnitude (length) of the vector
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

# Main program starts here
if __name__ == '__main__':
    points = list()  # List to store the four input points
    
    # Read 4 lines of input, each containing 3 floating-point numbers
    for i in range(4):
        a = list(map(float, input().split()))  # Convert input to list of floats
        points.append(a)  # Add the point to the list

    # Unpack the list into four Point objects: a, b, c, d
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])

    # Compute two normal vectors using cross products
    # (b - a) and (c - b) define one plane; their cross product gives a normal vector 'x'
    x = (b - a).cross(c - b)
    # (c - b) and (d - c) define another plane; their cross product gives normal vector 'y'
    y = (c - b).cross(d - c)

    # Compute the angle between the two planes using the dot product formula:
    # cos(θ) = (x · y) / (|x| * |y|)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    # Convert the angle from radians to degrees and print it, formatted to 2 decimal places
    print("%.2f" % math.degrees(angle))
