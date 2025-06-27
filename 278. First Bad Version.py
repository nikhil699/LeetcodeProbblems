# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Type	Value	Why?
# Time Complexity	O(log n)	Binary search halves the range each time
# Space Complexity	O(1)	No extra data structure used


class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n

        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low  # or high, both are same here



