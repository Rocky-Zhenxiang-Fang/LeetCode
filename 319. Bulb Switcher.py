
class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Idea:
            if a bulb is on after days, it will have a odd number of divisor
            If it has a odd number of divisor, the sqrt of number will be a int
            At any n, sqrt(n) will equal to the number of squared number between 1, n
        """
        return int(n ** 0.5)

if __name__ == '__main__':
    sol = Solution()
    arr = 5
    print(sol.bulbSwitch(arr))
