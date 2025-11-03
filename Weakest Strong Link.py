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
	row_ls = []
	for i in strength:
		weak = i[0]
		for j in i:
			if j < weak:
				weak = j
		row_ls.append(weak)

	col_ls = []
	for i in range(len(strength[0])):
		strong = strength[0][i]
		for j in range(len(strength)):
			if strength[j][i] > strong:
				strong = strength[j][i]
		col_ls.append(strong)

	# print(row_ls)
	# print(col_ls)
	for i in row_ls:
		if i in col_ls:
			return i
	return -1
			