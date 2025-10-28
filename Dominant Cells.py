#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.

def numCells(grid):
    count = 0  # Initialize count to track the number of cells that are larger than their neighbors.
    rows = len(grid)  # Get the number of rows in the grid.
    cols = len(grid[0])  # Get the number of columns in the grid.

    # Iterate through each cell in the grid.
    for i in range(rows):
        for j in range(cols):
            neighbors = []  # List to store the values of neighboring cells.

            # Iterate through neighboring cells, considering all 8 possible neighbors around the current cell.
            # Use max(0, i-1) and min(rows, i+2) to ensure we don't go out of bounds.
            for r in range(max(0, i-1), min(rows, i+2)):
                for c in range(max(0, j-1), min(cols, j+2)):
                    if r == i and c == j:
                        continue  # Skip the current cell itself.
                    neighbors.append(grid[r][c])  # Add the neighbor value to the list.

            # Check if the current cell is greater than all of its neighbors.
            # `all()` ensures that all neighbors are smaller than the current cell.
            if all(grid[i][j] > n for n in neighbors):
                count += 1  # Increment the count if the current cell is greater than all its neighbors.

    return count  # Return the total count of such cells.

if __name__ == '__main__':
    # Open the output file (this path is provided through environment variable OUTPUT_PATH)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of rows and columns for the grid
    grid_rows = int(input().strip())  # Get number of rows
    grid_columns = int(input().strip())  # Get number of columns

    # Initialize an empty list to store the grid
    grid = []

    # Read each row of the grid and append it to the grid list
    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))  # Convert each row to a list of integers

    # Call the numCells function to get the result
    result = numCells(grid)

    # Write the result to the output file (convert result to string before writing)
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()
