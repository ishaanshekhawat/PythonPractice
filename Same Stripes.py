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
    # Dictionary to store the elements of each diagonal stripe identified by their key (i - j)
    same_diagonal_elements = {}
    
    # Loop through each element in the matrix using row (i) and column (j) indices
    for i in range(len(matrix)):  # Iterate through rows
        for j in range(len(matrix[i])):  # Iterate through columns in each row
            # Create a set to track unique values in each diagonal
            s = set()
            
            # Calculate the diagonal key using (i - j)
            diagonal_key = i - j
            
            # If the diagonal (i - j) is not in the dictionary, add it with the current element
            if diagonal_key not in same_diagonal_elements.keys():
                s.add(matrix[i][j])
                same_diagonal_elements[diagonal_key] = s
            # If the diagonal already exists, add the current element to the set
            elif diagonal_key in same_diagonal_elements.keys():
                s1 = same_diagonal_elements[diagonal_key]
                s1.add(matrix[i][j])
                same_diagonal_elements[diagonal_key] = s1
    
    # After collecting all diagonal elements, check if all diagonals contain identical values
    for k, v in same_diagonal_elements.items():
        # If the set has more than one element, the diagonal contains different numbers
        if len(v) > 1:
            return False
    
    # If all diagonals are uniform, return True
    return True

