# You’re given a list of integers nums of length n where each integer is in the range [1, n].
# One number appears twice, and one number is missing.

# Your task is to find both numbers.

nums = list(map(int, input().split()))

for i in range(1, len(nums) + 1):
    if i not in nums:
        missing = i
        break

for i in range(1, len(nums) + 1):
    if nums.count(i) == 2:
        repeated = i
        break

print(missing)
print(repeated)