from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Idea:
            monotonic deque
            max_deque:
                monotonic decreasing deque. When something bigger comes, the one in front cannot be a maximum value anymore,
                also it will be remove earlier, so it is safe to remove it.
            min_deque:
                same idea
            Alg:
                Using two pointers to indicate the left and right of subarray
        """
        from collections import deque
        if not nums:
            return 0
        left, right = 0, 0
        max_deque = deque()
        min_deque = deque()
        res = 0
        while right < len(nums):
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            max_deque.append(right)
            min_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                while min_deque[0] < left:
                    min_deque.popleft()
                while max_deque[0] < left:
                    max_deque.popleft()
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    nums = [8, 2, 4, 7]
    limit = 4
    sol = Solution()
    print(sol.longestSubarray(nums, limit))

