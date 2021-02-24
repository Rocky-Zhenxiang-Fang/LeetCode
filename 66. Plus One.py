import collections
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + carry
            carry = val // 10
            val %= 10
            digits[i] = val

        return digits if not carry else [carry] + digits
