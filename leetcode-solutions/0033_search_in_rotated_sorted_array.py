# LeetCode 33: Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Approach: Modified binary search to handle rotation
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

# Example run
print(Solution().search([4,5,6,7,0,1,2], 0))  # Output: 4
print(Solution().search([4,5,6,7,0,1,2], 3))  # Output: -1
print(Solution().search([1], 0))              # Output: -1
