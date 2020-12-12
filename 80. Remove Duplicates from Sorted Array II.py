from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        From https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C%2B%2B-Java-Python-Ruby
        Just go through the numbers and include those in the result that haven't been included twice already.
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 1, 1, 2, 2, 3]
    ans = sol.removeDuplicates(arr)
    print(ans)
    print(arr)
