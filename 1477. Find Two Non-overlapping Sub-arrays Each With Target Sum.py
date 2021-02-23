from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """
        Idea:
            Same as finding a subarray with target sum.
            However, this time, when a subarray is found, see if there exists a non_overlapped subarray that have the same
            sum.
            Use a list to store the minimum length of subarray that sums to target before this index
        """
        left, right, running_sum = 0, 0, 0
        res = float("inf")
        prefix_len = [float("inf")] * len(arr)  # using this so that the sum will never be the answer
        while right < len(arr):
            running_sum += arr[right]
            while running_sum > target:
                running_sum -= arr[left]
                left += 1
            if running_sum == target:
                curr_len = right - left + 1
                min_prev = prefix_len[left - 1] if left != 0 else float("inf")
                res = min(res, curr_len + min_prev)
                prefix_len[right] = min(curr_len, prefix_len[right - 1]) if right != 0 else curr_len
            else:
                prefix_len[right] = prefix_len[right - 1]
            right += 1

        return res if res != float("inf") else -1


if __name__ == '__main__':
    sol = Solution()
    arr = [3, 2, 2, 4, 3]
    target = 3
    print(sol.minSumOfLengths(arr, target))
