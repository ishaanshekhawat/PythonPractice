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
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            neighbors = []

            for r in range(max(0, i-1), min(rows, i+2)):
                for c in range(max(0, j-1), min(cols, j+2)):
                    if r == i and c == j:
                        continue
                    neighbors.append(grid[r][c])

            if all(grid[i][j] > n for n in neighbors):
                count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
