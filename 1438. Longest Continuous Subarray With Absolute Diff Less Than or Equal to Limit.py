from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        left, right = 0, 0
        max_len = 0
        min_que, max_que = deque(), deque()
        while right < len(nums):
            while min_que and nums[right] <= nums[min_que[-1]]:
                min_que.pop()
            while max_que and nums[right] >= nums[max_que[-1]]:
                max_que.pop()
            min_que.append(right)
            max_que.append(right)

            while nums[max_que[0]] - nums[min_que[0]] > limit:
                left += 1
                if min_que[0] < left:
                    min_que.popleft()
                if max_que[0] < left:
                    max_que.popleft()

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len


if __name__ == '__main__':
    sol = Solution()
    t1_array = [8, 2, 4, 7]
    t2_array = [10, 1, 2, 4, 7, 2]
    t3_array = [4, 2, 2, 2, 4, 4, 2, 2]
    print(sol.longestSubarray(t1_array, 4))
    print(sol.longestSubarray(t2_array, 5))
    print(sol.longestSubarray(t3_array, 0))
