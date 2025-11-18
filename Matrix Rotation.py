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

def rotate(matrix):
    rl = len(matrix[0])
    nr = len(matrix)
    m1 = []
    for _ in range(rl):
        m1.append([None] * nr)

    for i in range(rl):
        for j in range(nr):
            m1[i][j] = matrix[j][i]

    m2 = []
    for i in range(rl):
        m2.append([None]*nr)

    for i in range(rl):
        for j in range(nr):
            m2[i][j] = m1[i][-(j+1)]

    return m2

def find_rotation(mat, target):
    for i in range(4):
        if target == rotate(mat):
            return True
        mat = rotate(mat)
        i += 1
    return False