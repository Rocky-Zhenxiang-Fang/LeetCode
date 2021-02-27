class Solution:
    def getMoneyAmount(self, n):
        """
        Idea:
            Start with small trees, we can see that two strategies:
            1. If there is only one left, the cost will be zero
            2. If there are two left, the cost will be the smaller one
            anything beyond 3 can be turn into 1 and 2 with the cost of pivot, where we pick either 1 or 2
            Thus, for each tree, we can test each partition, and return the minimum cost
            We also memorize it in case of future use
        """

        def helper(start, end) -> int:
            if (start, end) in memo:
                return memo[(start, end)]
            else:
                res = float("inf")
                if start == end:
                    res = 0
                elif start + 1 == end:
                    res = start
                else:
                    for i in range(start + 1, end):
                        res = min(res, i + max(helper(start, i - 1), helper(i + 1, end)))
                memo[(start, end)] = res
                return res

        memo = {}  # stores (start, end)
        res = helper(1, n)
        if n == 6:
            print(memo)
        return res


if __name__ == '__main__':
    for i in range(1, 20):
        sol = Solution()
        print(str(i) + ":" + str(sol.getMoneyAmount(i)))