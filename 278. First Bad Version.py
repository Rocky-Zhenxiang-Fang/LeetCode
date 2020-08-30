# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(version):
    if version >= 4:
        return True
    else:
        return False


class Solution:
    def firstBadVersionRec(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(1, n)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        end = n
        while first <= end:
            if first == end or first == end - 1:
                if isBadVersion(first):
                    return first
                return end
            mid = (first + end)
            if isBadVersion(mid):
                end = mid
            else:
                first = mid
        return None

    def binarySearch(self, start, end):
        # if only have two number left, then it is
        # [false, false, ..., false, true, true, ...]
        # [                   start, end, ..........]
        # or
        # [true, true, ..., true, true, true, ...]
        # [start, end, ..........]
        if start == end - 1:
            if isBadVersion(start):
                return start
            return end
        half = (start + end) // 2
        if isBadVersion(half):
            return self.binarySearch(start, half)
        else:
            return self.binarySearch(half, end)


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstBadVersion(5))