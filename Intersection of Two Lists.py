# Write a function to get the intersection of two lists.

# For example, if A = [1, 2, 3, 4, 5], and B = [0, 1, 3, 7] then you should return [1, 3].

def intersection(a, b):
    inter1 = set()
    for i in a:
        if i in b:
            inter1.add(i)
    
    return list(inter1)

print(intersection([1, 2, 3, 4, 5],[0, 1, 3, 7]))