# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# For numRows = 1, you should return [[1]].
# For numRows = 4, you should return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]].

def generate(numRows):
    ls = []
    for i in range(1, numRows + 1):
        ls1 = []
        for j in range(1, i+1):
            if j == 1:
                ls1.append(1)
            elif j == i:
                ls1.append(1)
            else:
                ls1.append(ls[i-2][j-2]+ls[i-2][j-1])
        ls.append(ls1)
    return ls