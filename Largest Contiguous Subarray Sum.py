# Given an integer array, find the sum of the largest contiguous subarray within the array.
# For example, if the input is [−1, −3, 5, −4, 3, −6, 9, 2], then return 11 (because of [9, 2]).
# Note that if all the elements are negative, you should return 0.

# Given an integer array, find the sum of the largest contiguous subarray.
# If all numbers are negative, return 0.

def max_subarray_sum(input):
    # 'sum' tracks the current subarray sum we are building
    sum = 0
    
    # 'max' stores the maximum subarray sum found so far
    max = 0
    
    # 'ct' counts how many negative numbers are in the array
    # (used to detect if the entire array is negative)
    ct = 0

    # Iterate through each element in the input array
    for i in input:
        # Count negative numbers
        if i < 0:
            ct += 1

        # If adding the current number would make the current sum negative,
        # reset the sum to 0 (start a new subarray)
        if sum + i < 0:
            sum = 0
        else:
            # Otherwise, extend the current subarray
            sum += i

        # Update max if the current sum is the best seen so far
        if sum > max:
            max = sum

    # If all elements were negative, return 0 as required
    if ct == len(input):
        return 0

    # Otherwise, return the maximum subarray sum
    return max

# Example usage
print(max_subarray_sum([1, -1, 1, -1, 1, -1, 5]))
