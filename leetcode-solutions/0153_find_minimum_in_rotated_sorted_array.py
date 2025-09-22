# LeetCode 153: Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Approach: Binary search, compare mid with high
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

# Example run
print(Solution().findMin([3,4,5,1,2]))   # Output: 1
print(Solution().findMin([4,5,6,7,0,1,2])) # Output: 0
print(Solution().findMin([11,13,15,17])) # Output: 11
