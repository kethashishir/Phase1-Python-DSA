# LeetCode 35: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Approach: Binary search to find target or correct insert index
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        if low == high:
            if nums[low] == target:
                return low
            elif nums[low] < target:
                return low + 1
            else:
                return low

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return low

# Example run
print(Solution().searchInsert([1,3,5,6], 5))  # Output: 2
print(Solution().searchInsert([1,3,5,6], 2))  # Output: 1
print(Solution().searchInsert([1,3,5,6], 7))  # Output: 4
print(Solution().searchInsert([1,3,5,6], 0))  # Output: 0
