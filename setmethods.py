s1 = {1,2,3,7,92,12,3,3,3}
print(s1)

s1.add(8)
print(s1)

# s1.remove(4843)
s1.discard(4843)

print(s1.pop())
print(s1)

s2 = {2,34,6,2,6,3,1,7}
print(s1.union(s2))
print(s1 | s2)

print(s1.intersection(s2))
print(s1 & s2)

print(s1.difference(s2))
print(s1 - s2)

print(s1.symmetric_difference(s2))
print(s1^s2)

print(sorted(s1))

