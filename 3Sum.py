# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This list will store all unique triplets that sum to zero
        sol = []

        # Loop through each element as the first number of the triplet
        for i in range(len(nums) - 2):

            # Loop through elements after i as the second number
            for j in range(i + 1, len(nums) - 1):

                # Determine the value needed to reach a sum of zero
                # nums[i] + nums[j] + target == 0 → target = -(nums[i] + nums[j])
                target = -nums[i] - nums[j]

                # Loop through elements after j as the third number
                for k in range(j + 1, len(nums)):

                    # Check if nums[k] completes the triplet
                    if nums[k] == target:

                        # Sort the triplet to avoid duplicate permutations
                        triplet = sorted([nums[i], nums[j], nums[k]])

                        # Only add if this exact triplet hasn't been added before
                        if triplet in sol:
                            continue
                        else:
                            sol.append(triplet)

        # Return the list of unique triplets
        return sol
