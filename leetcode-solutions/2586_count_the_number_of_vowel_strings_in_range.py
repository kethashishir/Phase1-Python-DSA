# LeetCode 2586: Count the Number of Vowel Strings in Range
# Link: https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
# Approach: Iterate through range and check first & last char
# Time Complexity: O(n * k) where k = word length (usually small)
# Space Complexity: O(1)

class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowels = ['a','e','i','o','u']
        count = 0
        
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                count += 1
        return count

# Example run
print(Solution().vowelStrings(["are","amy","u"], 0, 2))  # Output: 2
print(Solution().vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4))  # Output: 3
