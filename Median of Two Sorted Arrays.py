# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3)%2 == 1:
            return nums3[len(nums3)//2]
        else:
            return (nums3[len(nums3)//2] + nums3[(len(nums3)//2)-1])/2
        
