class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        From https://www.youtube.com/watch?v=htX69j1jf5U
        Try to remove one divisor from dividend, if possible, try to reomve double of it
        iterate until dividend is smaller then divisor
        """
        positive = (dividend < 0) == (divisor < 0) 
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            temp, i = divisor, 1  # temp is the amout that is going the be remove in the next round, i is the rank of 2
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        
        return min((max(-2147483648, res), 2147483647)
