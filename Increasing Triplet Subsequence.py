class Solution(object):
    def increasingTriplet(self, nums):
        """
        Solution modified from:
        https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/discuss/79004/Concise-Java-solution-with-comments.
        """
        first, second = float("inf"), float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
