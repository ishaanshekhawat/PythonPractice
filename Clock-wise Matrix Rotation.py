def rotate(matrix):
    rl = len(matrix[0])
    nr = len(matrix)
    m1 = []
    for _ in range(rl):
        m1.append([None] * nr)

    for i in range(rl):
        for j in range(nr):
            m1[i][j] = matrix[j][i]
    
    left = 0
    right = len(m1[0]) - 1

    m2 = []
    for i in range(rl):
        m2.append([None]*nr)

    for i in range(rl):
        for j in range(nr):
            m2[i][j] = m1[i][-(j+1)]

    return m2


print(rotate([[5, 1], [6, 2]]))
print(rotate([[3, 6, 9], [2, 5, 8], [1, 4, 7]]))