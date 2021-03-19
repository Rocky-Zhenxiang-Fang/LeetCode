from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Idea:
            We can have two kinds of wiggle: s, b, s, b, s, b or b, s, b, s, b, s
            If now I am searching for a small element but comes a big element, the last element in the list will be replaced
        """
        return max(self._wiggle(nums, True), self._wiggle(nums, False))

    def _wiggle(self, nums: List[int], small: bool) -> int:
        res = [nums[0]]
        for n in nums:
            if small:  # next element should be smaller
                if n < res[-1]:
                    res.append(n)
                    small = not small
                else:
                    res[-1] = n
            else:
                if n > res[-1]:
                    res.append(n)
                    small = not small
                else:
                    res[-1] = n
        return len(res)


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    print(sol.wiggleMaxLength(arr))
