# LeetCode 242: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Approach: Sort both strings and compare
# Time Complexity: O(n log n)
# Space Complexity: O(1) (ignoring sorting overhead)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

# Example run
print(Solution().isAnagram("anagram", "nagaram"))  # Output: True
print(Solution().isAnagram("rat", "car"))          # Output: False
