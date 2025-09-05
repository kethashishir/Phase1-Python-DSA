# LeetCode 217: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Approach: Use set to check duplicates
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_num = set(nums)

        if len(nums) != len(set_num):
            return True
        return False

# Example run
print(Solution().containsDuplicate([1, 2, 3, 1]))  # Output: True
print(Solution().containsDuplicate([1, 2, 3, 4]))  # Output: False
