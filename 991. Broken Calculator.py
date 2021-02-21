class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        """
        Idea:
            Greedy,
                If X >= Y: return X - Y
                Assuming Y is odd, the last term before Y will be Y +１
                If Y is even, the last term could be Y + 1 or Y / 2
                    If is Y + 1, the assumption will not be valid, So it can only be Y / 2
            https://leetcode.com/problems/broken-calculator/discuss/236565/Detailed-Proof-Of-Correctness-Greedy-Algorithm
        """
        if X >= Y:
            return X - Y
        elif Y % 2 == 0:
            return 1 + self.brokenCalc(X, Y // 2)
        else:
            return 1 + self.brokenCalc(X, Y + 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.brokenCalc(2, 3))