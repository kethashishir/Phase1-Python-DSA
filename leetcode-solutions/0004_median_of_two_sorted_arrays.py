# LeetCode 4: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Approach: Binary search on the smaller array
# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m  # ensure A is smaller

        total = m + n
        half = (total + 1) // 2 

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2       
            j = half - i             

            Aleft  = A[i-1] if i > 0 else float("-inf")
            Aright = A[i]   if i < m else float("inf")
            Bleft  = B[j-1] if j > 0 else float("-inf")
            Bright = B[j]   if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  
                    return float(max(Aleft, Bleft))
                else:          
                    left_max  = max(Aleft, Bleft)
                    right_min = min(Aright, Bright)
                    return (left_max + right_min) / 2.0

            if Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1

# Example run
print(Solution().findMedianSortedArrays([1,3], [2]))        # Output: 2.0
print(Solution().findMedianSortedArrays([1,2], [3,4]))      # Output: 2.5
print(Solution().findMedianSortedArrays([0,0], [0,0]))      # Output: 0.0
print(Solution().findMedianSortedArrays([], [1]))           # Output: 1.0
