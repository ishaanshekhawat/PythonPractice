import itertools

numbers_str = input()
numbers = []
for i in numbers_str:
    numbers.append(int(i))

# print(numbers)

# Example with a simple list of numbers
# numbers = [1, 2, 2, 2, 3, 1, 1]

ls = []
for key, group in itertools.groupby(numbers):
    tuplee = (len(list(group)), key)
    ls.append(str(tuplee))

print(' '.join(ls))