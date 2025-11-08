# Given an integer array and an integer n as input, return the top n integers in the array 
# (the ones that appear most frequently). Return the output in non-decreasing order. 
# The test cases are generated in such a way that there will be a unique answer.

# Example #1
# Input: nums = [2, 1, 2, 3, 2, 1, 2, 1, 3, 4], n = 3
# Output: [1, 2, 3]

# Explanation: The most frequent elements are: 2 with a frequency of 4, 1 with a frequency of 3, and 3 with a frequency of 2. Finally, the output is sorted in non-decreasing order.

# Example #2
# Input: nums = [3, 2], n = 2
# Output: [2, 3]

def most_popular(nums, n):
    # Create an empty dictionary to count occurrences of each number
    dict1 = {}

    # Loop through each number in the list
    for i in range(len(nums)):
        # If the number already exists in the dictionary, increment its count
        if nums[i] in dict1.keys():
            dict1[nums[i]] += 1
        # Otherwise, add it to the dictionary with an initial count of 1
        else:
            dict1[nums[i]] = 1

    # Sort the dictionary by values (counts) in descending order
    # dict1.items() → list of (key, value) pairs
    # key=lambda x: x[1] → sort by value (the count)
    # reverse=True → highest counts first
    dict2 = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))

    ct = 0          # Counter to keep track of how many top elements we've collected
    ls = []         # List to store the top n most frequent numbers

    # Loop through the sorted dictionary
    for k, v in dict2.items():
        ls.append(k)  # Add the number (key) to the list
        ct += 1
        if ct == n:   # Stop once we've collected n items
            break

    # Sort the top n numbers in ascending order before returning
    for i in range(len(ls)):
        for j in range(len(ls) - 1):
            if ls[j] > ls[i]:
                ls[j], ls[i] = ls[i], ls[j]

    return ls  # Return the list of most popular numbers
