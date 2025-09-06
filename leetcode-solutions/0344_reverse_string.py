# LeetCode 344: Reverse String
# Link: https://leetcode.com/problems/reverse-string/
# Approach: Two pointers swapping in-place
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # swap the characters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example run
arr = ["h","e","l","l","o"]
Solution().reverseString(arr)
print(arr)  # Output: ["o","l","l","e","h"]
