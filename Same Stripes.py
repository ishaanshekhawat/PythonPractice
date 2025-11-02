# You are given an m x n matrix. Your task is to determine if the matrix has diagonal stripes where all elements in each diagonal from top-left to bottom-right are of the same stripe—that is, they are identical.

# In this context, each diagonal stripe runs from the top-left corner to the bottom-right corner of the matrix. Check if every diagonal stripe consists entirely of the same number.

# Return True if all diagonal stripes are of the same stripe, otherwise return False.

# Input: matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]

# Output: True

# Explanation:
# In this grid, the diagonals are:

# [1]
# [6, 6]
# [42, 42, 42]
# [7, 7, 7]
# [13, 13]
# [99]
# All elements in each diagonal ar identical. Thus, the answer is True.

def is_same_stripes(matrix):
    same_diagonal_elements = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s = set()
            # same_diagonal_elements[i-j] = s
            if (i-j) not in same_diagonal_elements.keys():
                s.add(matrix[i][j])
                same_diagonal_elements[i-j] = s
            elif (i-j) in same_diagonal_elements.keys():
                s1 = same_diagonal_elements[i-j]
                s1.add(matrix[i][j])
                same_diagonal_elements[i-j] = s1
    for k,v in same_diagonal_elements.items():
        if len(v) > 1:
            return False
    else:
        return True


