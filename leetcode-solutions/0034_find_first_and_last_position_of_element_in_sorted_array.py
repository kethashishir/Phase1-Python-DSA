# LeetCode 34: Find First and Last Position of Element in Sorted Array
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Approach: Binary search twice (lower bound and upper bound)
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        low, high = 0, n

        # Find left boundary
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        left = low

        # Find right boundary
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        right = low

        if left == n or nums[left] != target:
            return [-1, -1]
        else:
            return [left, right - 1]

# Example run
print(Solution().searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
print(Solution().searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
print(Solution().searchRange([], 0))              # Output: [-1, -1]
