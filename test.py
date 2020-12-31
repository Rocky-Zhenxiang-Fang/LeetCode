# This file is used to review done questions

# Definition for a binary tree node.
from typing import List, Set

import DS


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        decimal = set()

        def util(reminder: int) -> None:
            if reminder == 0:
                return
            else:
                if reminder >= denominator:
                    next_remin = reminder % denominator
                    if decimal:
                        if reminder // denominator in decimal:
                            res.insert(res.index(reminder // denominator), "(")
                            res.append(")")
                            return
                        else:
                            decimal.add(reminder // denominator)
                    res.append(str(reminder // denominator))
                else:
                    next_remin = reminder
                    if not decimal:
                        decimal.add(-1)
                        res.append("0.")
                    else:
                        res.append("0")
                        decimal.add(0)
                if decimal:
                    next_remin = next_remin * 10
            util(next_remin)

        util(numerator)
        return "".join(res)


if __name__ == '__main__':
    nums = 4
    den = 333
    sol = Solution()
    print(sol.fractionToDecimal(nums, den))
