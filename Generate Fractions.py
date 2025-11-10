# Given an integer n, generate all simplified fractions between 0 and 1 (exclusive) 
# where the denominator is less than or equal to n. 
# A fraction is simplified if the numerator and denominator have no common divisors other than 1.
# Return a sorted list of fractions, where each fraction is represented as [numerator, denominator].

# For example:
# If n = 3, return [[1, 2], [1, 3], [2, 3]]
# If n = 4, return [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
# If n = 5, return [[1, 2], [1, 31, [1, 4], [1, 5], [2, 3], [2, 5], [3, 4], [3, 5], [4, 5]]

def generate_fractions(n):
    # Step 1: Generate all possible pairs [i, j] where both i and j go from 1 to n
    ls = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            temp = [i, j]
            ls.append(temp)

    # Step 2: Keep only pairs where numerator < denominator
    # (i.e., fractions less than 1)
    ls1 = []
    for i in ls:
        if i[0] < i[1]:
            ls1.append(i)

    # Step 3: Identify reducible fractions (fractions that can be simplified)
    ls2 = []
    for i in ls1:
        # Check all possible divisors up to the denominator
        for j in range(2, i[1]):
            # If both numerator and denominator are divisible by j,
            # then the fraction can be simplified
            if i[0] % j == 0 and i[1] % j == 0:
                ls2.append(i)
                break  # optional: prevents adding duplicates if multiple divisors exist

    # Step 4: Remove reducible fractions from ls1,
    # leaving only fractions in simplest form
    for i in ls2:
        if i in ls1:
            ls1.remove(i)

    # Step 5: Return the list of irreducible (simplified) fractions
    return ls1
    
