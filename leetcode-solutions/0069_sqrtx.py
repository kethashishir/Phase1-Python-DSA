# LeetCode 69: Sqrt(x)
# Link: https://leetcode.com/problems/sqrtx/
# Approach: Binary search between 0 and x
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x

        if x < 2:
            return x

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high

# Example run
print(Solution().mySqrt(4))   # Output: 2
print(
