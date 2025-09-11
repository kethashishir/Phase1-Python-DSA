# LeetCode 13: Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/
# Approach: Traverse from right to left, subtract when smaller than previous
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prev = 0
        
        # Traverse from right to left
        for char in reversed(s):
            curr = values[char]
            
            # If current value is smaller than previous, subtract it
            if curr < prev:
                total -= curr
            else:
                total += curr
            
            # Update previous
            prev = curr
        
        return total

# Example run
print(Solution().romanToInt("III"))     # Output: 3
print(Solution().romanToInt("IV"))      # Output: 4
print(Solution().romanToInt("IX"))      # Output: 9
print(Solution().romanToInt("LVIII"))   # Output: 58
print(Solution().romanToInt("MCMXCIV")) # Output: 1994
