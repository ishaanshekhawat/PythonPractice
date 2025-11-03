# You know that phrase, how a chain is only as strong as its weakest link?

# Imagine you had a chain-link fence, represented as a matrix. For the chain-link at position (i, j), the input matrix strength[i][j] indicates how strong the chain is at that position (where stronger means a higher number). The numbers in the matrix are unique.

# The Weakest Strong Link is defined as the weakest chain-link in its row but also the strongest link in its column.

# Given a matrix strength, return the weakest strong link if it exists; otherwise, return -1. If a weakest strong link exists, it is always exactly one, and it can be proven that no other link will satisfy both conditions simultaneously.

# Example 1
# Input: strength = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# Output: 7

# Explanation:
# 7 is the weakest in its row [7, 8, 9] and the strongest in its column [1, 4, 7], making it the Weakest Strong Link.

# Example #2
# Input: strength = [[9, 8, 10],[6, 15, 4]]
# Output: -1

# Explanation:
# No chain-link satisfies the criteria of being the weakest in its row and the strongest in its column.

def weakest_strong_link(strength):
    # Initialize an empty list to store the weakest (minimum) value from each row
    row_ls = []
    
    # Loop through each row in the 2D list 'strength'
    for i in strength:
        weak = i[0]  # Start by assuming the first element is the weakest in the row
        for j in i:  # Check every element in the row
            if j < weak:  # If a smaller value is found, update 'weak'
                weak = j
        row_ls.append(weak)  # Append the smallest value from this row to row_ls

    # Initialize an empty list to store the strongest (maximum) value from each column
    col_ls = []
    
    # Loop through each column index (based on the first row's length)
    for i in range(len(strength[0])):
        strong = strength[0][i]  # Start by assuming the first element in the column is the strongest
        for j in range(len(strength)):  # Loop through all rows for this column
            if strength[j][i] > strong:  # If a larger value is found, update 'strong'
                strong = strength[j][i]
        col_ls.append(strong)  # Append the largest value from this column to col_ls

    # print(row_ls)  # Debug: print all row minimums
    # print(col_ls)  # Debug: print all column maximums

    # Check if there’s any value that is both the weakest in its row and the strongest in its column
    for i in row_ls:
        if i in col_ls:
            return i  # Return that value if found (the "weakest strong link")

    # If no such value exists, return -1
    return -1
