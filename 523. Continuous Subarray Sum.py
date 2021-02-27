from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Idea:
            Similar to subarray sum to k
            Instead of storing the sum of visited subarray, we store sum % k.
            If we meet running_sum % k - (visited_sum % k) == 0, this means that this two sum to a multiplication of k
            Take care if k == 0
        """
        visited = {0: -1}
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if k != 0:
                running_sum %= k
            if running_sum in visited:
                if i - visited[running_sum] > 1:
                    return True
            else:
                visited[running_sum] = i
        return False


if __name__ == '__main__':
    sol = Solution()
    arr_1 = [23, 2, 4, 6, 7]
    k_1 = 6
    arr_2 = [0, 0]
    k_2 = 0
    print(sol.checkSubarraySum(arr_1, k_1))
    print(sol.checkSubarraySum(arr_2, k_2))
