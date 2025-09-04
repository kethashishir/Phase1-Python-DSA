# LeetCode 1: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Approach: Brute Force (check all pairs)
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Example run
print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
