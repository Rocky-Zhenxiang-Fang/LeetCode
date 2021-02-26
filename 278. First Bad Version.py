# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(ver):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        Idea:
            Do a binary search, find the bad version that is next to good version
        """
        left, right = 0 , n
        while left <= right:
            mid = (left + right) // 2
            if (mid == 1 and isBadVersion(mid)) or (mid != 1 and not isBadVersion(mid - 1) and isBadVersion(mid)):
                return mid
            elif not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        return -1
