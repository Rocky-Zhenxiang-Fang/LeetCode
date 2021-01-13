from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        running_sum = 0
        sums = {0: -1}
        k = abs(k)
        for i in range(len(nums)):
            running_sum += nums[i]
            n = running_sum // k if k != 0 else 1
            for j in range(n):
                target1 = running_sum - j * k if k != 0 else -running_sum
                if target1 in sums and i - sums[target1] > 1:
                    return True
            if running_sum not in sums:
                sums[running_sum] = i
        return False


if __name__ == '__main__':
    sol = Solution()
    arr_1 = [23, 2, 4, 6, 7]
    k_1 = 6
    arr_2 = [0, 0]
    k_2 = 0
    print(sol.checkSubarraySum(arr_1, k_1))
    print(sol.checkSubarraySum(arr_2, k_2))
