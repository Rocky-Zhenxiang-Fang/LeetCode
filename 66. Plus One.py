import collections
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = collections.deque()
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + carry
            carry = val // 10
            val = val % 10
            res.appendleft(val)
        if carry == 1:
            res.appendleft(carry)
        return list(res)