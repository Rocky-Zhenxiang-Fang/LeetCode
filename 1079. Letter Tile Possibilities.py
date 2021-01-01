from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Example:
            Input: tiles = "AAB"
            Output: 8
            Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
        Idea: backtracking
            define a DFS function that fills a sub array with a remaining array
                AS long as the sub has been visited before, end this recursive call
                any long of sub can be added, so no need to check remaining
                since the next element can be any from the remaining:
                for each element in remaining:
                    put it in the last of sub
                    call DFS recursively
        """
        res = []
        visited = set()

        def dfs(sub: str, remaining: str) -> None:
            if sub in visited:
                return
            else:
                visited.add(sub)
            res.append(sub)
            for i in range(len(remaining)):
                dfs(sub + remaining[i], remaining[:i] + remaining[i + 1:])

        dfs("", tiles)
        return len(res) - 1  # -1 for the empty set


if __name__ == '__main__':
    test1 = "AAB"
    test2 = "AAABBC"
    test3 = "v"
    sol = Solution()
    print(sol.numTilePossibilities(test1))
    print(sol.numTilePossibilities(test2))
    print(sol.numTilePossibilities(test3))
