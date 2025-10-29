l1 = [1,2,3,7,92,12,3,3,3]

l1.append(4)
print(l1)

l1.extend([3,2,2])
print(l1)

l1.extend((3,2,2))
print(l1)

print(l1.index(3, 9))

l1.insert(10, 5)
print(l1)

l1.pop(-3)
print(l1)

print(l1.count(2))

l1.remove(2)
print(l1)

l1.sort()
print(l1)

l1.reverse()
print(l1)