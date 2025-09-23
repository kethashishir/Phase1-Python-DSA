# LeetCode 1: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Approach: Use hash table (dictionary) to store complements
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in values:
                return [i, values[x]]
            else:
                values[nums[i]] = i

# Example run
print(Solution().twoSum([2,7,11,15], 9))   # Output: [1, 0] (order may vary)
print(Solution().twoSum([3,2,4], 6))       # Output: [2, 1]
print(Solution().twoSum([3,3], 6))         # Output: [1, 0]
