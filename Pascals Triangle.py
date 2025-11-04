# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# For numRows = 1, you should return [[1]].
# For numRows = 4, you should return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]].

def generate(numRows):
    ls = []  # This will store all rows of Pascal's triangle

    # Loop through each row index from 1 to numRows (inclusive)
    for i in range(1, numRows + 1):
        ls1 = []  # This will store the current row

        # Build each row element by element
        for j in range(1, i + 1):
            # The first and last elements of every row are always 1
            if j == 1:
                ls1.append(1)
            elif j == i:
                ls1.append(1)
            else:
                # Each inner element is the sum of the two elements above it
                # The row above is ls[i-2] because 'i' starts at 1
                # Elements above are at positions (j-2) and (j-1)
                ls1.append(ls[i - 2][j - 2] + ls[i - 2][j - 1])

        # After constructing the current row, add it to the main list
        ls.append(ls1)

    # Return the completed Pascal's triangle
    return ls
