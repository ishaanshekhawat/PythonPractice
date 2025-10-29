d1 = {1: "apple", 2: "banana", 3: "cherry", 4: "date"}

print(d1)

print(d1.get(3))
print(d1.get(5))

print(d1.keys())
print(d1.values())
print(d1.items())

for k,v in d1.items():
    print(f'Key is {k} and Value is {v}')

d2 = {5: 'fig', 6: 'grape', 7: 'honeydew'}

d3 = {}

d3.update(d2)

print(d3)

print(d3.pop(6))
print(d3)
print(d3.popitem())
print(d3)

d3.fromkeys([5,6,7])
print(d3)