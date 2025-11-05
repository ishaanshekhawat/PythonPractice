# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed from the array.
# A consecutive sequence consists of elements where each element is exactly 1 greater than the previous element. The elements in the sequence can be selected from any position in the array and do not need to appear in their original order.

# Example #1
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive is [1, 2, 3, 4] which have a length of 4

# Example #2
# Input: nums = [3, 2]
# Output: 2
# Explanation: The longest consecutive is [2, 3] which have a length of 2

def longest_consecutive(nums):
    # Initialize a list to store the length of each consecutive sequence encountered
    ls = []
    
    # Remove duplicates from nums (since duplicates don’t affect consecutive sequences)
    # and convert it back to a list
    nums = list(set(nums))
    
    # Sort the list to make consecutive numbers adjacent
    nums.sort()
    
    # Initialize a counter for current consecutive sequence length
    ct = 1
    
    # Loop through the list (up to the second-to-last element)
    for i in range(len(nums) - 1):
        # Check if the next number is exactly 1 greater than the current number
        if nums[i] + 1 == nums[i + 1]:
            ct += 1  # Increment the count for the consecutive sequence
        else:
            ct = 1   # Reset count if the sequence breaks
        
        # Append the current sequence length to ls
        ls.append(ct)
    
    # Return the maximum consecutive sequence length found
    # (Caution: If nums is empty, max(ls) would fail)
    return max(ls)

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # Expected output: 4 (sequence: 1,2,3,4)
print(longest_consecutive([3, 2]))                   # Expected output: 2 (sequence: 2,3)
print(longest_consecutive([1, 2, 0, 1]))             # Expected output: 3 (sequence: 0,1,2)
print(longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # Expected output: 7 (sequence: -1,0,1,3,..., etc.)

			
