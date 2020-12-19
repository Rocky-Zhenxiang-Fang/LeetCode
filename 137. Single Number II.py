from typing import List


class Solution:
    def singleNumber_map(self, nums: List[int]) -> int:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        for j in counter:
            if counter[j] == 1:
                return j
        return -1

    def singleNumber(self, nums: List[int]) -> int:
        """
        From:
        https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
        Instead using map, use a integer as a set
        """
        ones = 0  # stores the number that appears once
        twices = 0  # stores the number that appears twice
        for n in nums:
            twices ^= n & ones  # if n is in ones, toggle the change in twice
            ones ^= n  # if n is not in ones, add it into ones
            mask = ones & twices  # if one element appears in both ones and twices, this number appears three
            # times, remove it
            twices &= ~mask
            ones &= ~mask
        return ones


if __name__ == '__main__':
    sol = Solution()
    arr = [2, 2, 3, 2]
    print(sol.singleNumber(arr))
