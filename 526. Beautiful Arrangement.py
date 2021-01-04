from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        """
        For each good arrangement, all elements are divisible by its index + 1 or its index + 1 is divisible by its element
        Idea:
            DFS and backtracking
            DFS:
                if all elements are used, ans += 1
                if not:
                    add the remaining elements one at a time:
                        if the element can be added:
                            digger further
                        if not:
                            try next number
        """
        self.res = 0

        def dfs(sub: List[int], remaining: List[int]):
            if not remaining:
                self.res += 1
            else:
                for i in range(len(remaining)):
                    if remaining[i] % (len(sub) + 1) == 0 or (len(sub) + 1) % remaining[i] == 0:
                        dfs(sub + [remaining[i]], remaining[:i] + remaining[i + 1:])

        dfs([], [ele + 1 for ele in range(n)])

        return self.res


if __name__ == '__main__':
    n = 2
    sol = Solution()
    print(sol.countArrangement(n))
