# LeetCode 3: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Approach: Sliding window with hash map to track last seen positions
# Time Complexity: O(n)
# Space Complexity: O(min(n, a)) where a = alphabet size

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        best = 0

        for right in range(len(s)):
            c = s[right]
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            best = max(best, right - left + 1)
        return best

# Example run
print(Solution().lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(Solution().lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(Solution().lengthOfLongestSubstring("pwwkew"))    # Output: 3
print(Solution().lengthOfLongestSubstring(""))          # Output: 0
