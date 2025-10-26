# Take an integer input from the user
# This represents the number of elements that will be entered next
n = int(input())

# Take a space-separated line of integers as input
# 'map(int, input().split())' converts each value from string to integer
# 'tuple(...)' then stores all those integers inside an immutable tuple
t = tuple(map(int, input().split()))

# Print the hash value of the tuple
# The 'hash()' function returns a unique integer that represents the tuple’s contents
print(hash(t))
