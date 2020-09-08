class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        0 comes from 10, and 10 comes from 2 * 5
        we will always have more 2 then 5, so we only need to count how many 5 do we have
        """
        ans = 0
        while n > 0:
            ans += n // 5
            n //= 5
        return ans
