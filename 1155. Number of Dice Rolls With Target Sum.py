class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        Idea:
            What I care about is the sum of dices and how many dices to get to this sum
            Record (sum, num_of_dices): ways to form this pair
            Do a Backtracking
        """
        memo = {}  # stores (sum, num_of_dices): ways

        def dp(num: int, sum_of_dice) -> int:
            """
            :param num: number of dices in this round
            :param sum_of_dice: sum of dices in this round
            :return: ways to get to this status
            """
            if num == d:
                return 1 if sum_of_dice == target else 0
            elif sum_of_dice >= target:
                return 0
            elif (sum_of_dice, num) in memo:
                return memo[(sum_of_dice, num)]
            else:
                bottom_sols = 0
                for i in range(1, f + 1):
                    bottom_sols += dp(num + 1, sum_of_dice + i)  # Do a DFS to get all possible solutions
                memo[(sum_of_dice, num)] = bottom_sols
                return bottom_sols

        return dp(0, 0) % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numRollsToTarget(2, 6, 7))
