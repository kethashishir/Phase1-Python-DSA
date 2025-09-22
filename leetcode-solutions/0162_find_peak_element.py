# LeetCode 162: Find Peak Element
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-peak-element/
# Approach: Binary search, compare mid with mid+1
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        if low == high:
            return low
        if len(nums) == 2:
            return low if nums[low] > nums[high] else high

        while low < high:
            mid = (low + high) // 2 
            if nums[mid] < nums[mid + 1]:      
                low = mid + 1                  
            else:
                high = mid                     
        return low

# Example run
print(Solution().findPeakElement([1,2,3,1]))       # Output: 2
print(Solution().findPeakElement([1,2,1,3,5,6,4])) # Output: 5 (or 1, both valid peaks)
