# Given an integer n, generate all simplified fractions between 0 and 1 (exclusive) 
# where the denominator is less than or equal to n. 
# A fraction is simplified if the numerator and denominator have no common divisors other than 1.
# Return a sorted list of fractions, where each fraction is represented as [numerator, denominator].

# For example:
# If n = 3, return [[1, 2], [1, 3], [2, 3]]
# If n = 4, return [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
# If n = 5, return [[1, 2], [1, 31, [1, 4], [1, 5], [2, 3], [2, 5], [3, 4], [3, 5], [4, 5]]

def generate_fractions(n):
    ls = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            temp = [i,j]
            ls.append(temp)
    print(ls)
    
    ls1 = []
    for i in ls:
        if i[0] < i[1]:
            ls1.append(i)
    print(ls1)

    ls2=[]
    for i in ls1:
        for j in range(2, i[1]):
            if i[0]%j==0 and i[1]%j==0:
                ls2.append(i)
    for i in ls2:
        if i in ls1:
            ls1.remove(i)
    print(ls1)

generate_fractions(4)
    