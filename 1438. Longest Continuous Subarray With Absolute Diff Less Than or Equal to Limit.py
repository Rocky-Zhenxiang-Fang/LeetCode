from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Idea:
            For a subarray problem, left and right pointer are used
            as long as condition is satisfied, right += 1
            otherwise, left += 1
            We only care about the biggest and the smallest value, all possible values are stored in monotonic deque
            For min_deque, all values are stored in increasing order. If a value smaller then the end of min_deque,
            then the old end will never be considered a smallest value, so remove it
            Storing index for removing at when left updates
        """
        from collections import deque
        left = right = 0
        min_deque = deque()
        max_deque = deque()
        res = 0
        while right < len(nums):
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            min_deque.append(right)
            max_deque.append(right)
            if nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            res = max(res, right - left + 1)
            right += 1
        return res



if __name__ == '__main__':
    sol = Solution()
    t1_array = [8, 2, 4, 7]
    t2_array = [10, 1, 2, 4, 7, 2]
    t3_array = [4, 2, 2, 2, 4, 4, 2, 2]
    print(sol.longestSubarray(t1_array, 4))
    print(sol.longestSubarray(t2_array, 5))
    print(sol.longestSubarray(t3_array, 0))
