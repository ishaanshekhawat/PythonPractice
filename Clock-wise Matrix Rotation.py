def rotate(matrix):
    # Get the number of columns (rl) and rows (nr) of the input matrix
    rl = len(matrix[0])  # Number of columns
    nr = len(matrix)     # Number of rows

    # Step 1: Transpose the matrix (flip rows and columns)
    m1 = []
    for _ in range(rl):
        m1.append([None] * nr)  # Initialize an empty transposed matrix

    # Fill the transposed matrix
    for i in range(rl):
        for j in range(nr):
            m1[i][j] = matrix[j][i]  # Swap rows and columns

    # Step 2: Reverse each row of the transposed matrix to rotate it 90 degrees
    # Initialize the new matrix for the rotated result
    left = 0
    right = len(m1[0]) - 1  # Right index of the row (same as number of columns - 1)

    m2 = []
    for i in range(rl):
        m2.append([None] * nr)  # Initialize the matrix for the final rotated result

    # Reverse each row of the transposed matrix
    for i in range(rl):
        for j in range(nr):
            m2[i][j] = m1[i][-(j+1)]  # Reverse each column of the transposed matrix

    return m2  # Return the rotated matrix

# Test cases
print(rotate([[5, 1], [6, 2]]))  # Expected output: [[6, 5], [2, 1]]
print(rotate([[3, 6, 9], [2, 5, 8], [1, 4, 7]]))  # Expected output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
