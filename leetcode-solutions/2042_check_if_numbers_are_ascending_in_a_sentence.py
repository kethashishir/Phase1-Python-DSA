# LeetCode 2042: Check if Numbers Are Ascending in a Sentence
# Link: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
# Approach: Split string, track last number, ensure strictly increasing
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = 0
        x = s.split()
        
        for token in x:
            if token.isdigit():
                val = int(token)
                if val <= num:
                    return False
                num = val
        return True

# Example run
print(Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))  # Output: True
print(Solution().areNumbersAscending("hello world 5 x 5"))  # Output: False
