# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal 
# to target by rotating mat in 90-degree increments, or false otherwise.

# Example #1
# Input: mat = [[1,0,1],[0,0,1],[1,0,1]], target = [[1,0,1],[1,0,0],[1,0,1]]
# Output: true
# Explanation: We can rotate mat 180 degrees to go from the input mat to the target

# Example #2
# Input: mat = [[0, 1],[1, 0]], target = [[1, 1],[0, 0]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat

# Rotate an n x n matrix 90 degrees clockwise
def rotate(matrix):
    rl = len(matrix[0])   # number of columns
    nr = len(matrix)      # number of rows

    # Step 1: Transpose the matrix (swap rows and columns)
    # m1[i][j] = matrix[j][i]
    m1 = []
    for _ in range(rl):
        m1.append([None] * nr)

    for i in range(rl):
        for j in range(nr):
            m1[i][j] = matrix[j][i]

    # Step 2: Reverse each row of the transposed matrix
    # This completes the 90° clockwise rotation
    m2 = []
    for _ in range(rl):
        m2.append([None] * nr)

    for i in range(rl):
        for j in range(nr):
            # Reverse the row by indexing from the end
            m2[i][j] = m1[i][-(j + 1)]

    return m2


# Check if rotating mat by 0°, 90°, 180°, or 270° can make it equal to target
def find_rotation(mat, target):
    # Try up to 4 rotations (including original orientation)
    for _ in range(4):
        if mat == target:     # if current orientation matches target
            return True
        mat = rotate(mat)     # rotate 90° and try again

    return False              # no rotation matched target
