from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        From https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book
        Idea: On each element of
        nums, see if the subarray from start to itself can form the answer, also check if the answer can be form by
        subtracting a subarray from the start to another point, if can, add the number of its apperance
        """
        running_sum = 0
        res = 0
        seen = {}
        for n in nums:
            running_sum += n
            if running_sum == k:
                res += 1
            if running_sum - k in seen:
                res += seen[running_sum - k]
            seen[running_sum] = seen.get(running_sum, 0) + 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    sol = Solution()
    print(sol.subarraySum(nums, k))




