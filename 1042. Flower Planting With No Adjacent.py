from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """
        Idea: 4-coloring -> NP-Complete: backtracking
        First, turn the paths into a adj list
        define a dfs function that gives color to each nodes
            if colored == n:    all colored
                return
            try to color the next node using color from 1 to 4
                if the color is the same of one of its neighbor. remove this color
            if unable to color in this round, remove the last item of colored
        """
        graph: List[List[int]] = [[] for _ in range(n)]
        colored = []

        def dfs() -> bool:
            if len(colored) == n:
                return True
            else:
                s = False
                curr = len(colored)
                used = set()
                for nei in graph[curr]:
                    if nei < curr:
                        used.add(colored[nei])
                unused = list({1, 2, 3, 4} - used)
                while unused:
                    color = unused.pop()
                    colored.append(color)
                    s = dfs()
                    if s:
                        break
                    colored.pop()
            return s
        for p in paths:
            graph[p[0] - 1].append(p[1] - 1)
            graph[p[1] - 1].append(p[0] - 1)

        dfs()
        return colored


if __name__ == '__main__':
    sol = Solution()
    n_1 = 3
    paths_1 = [[1, 2], [2, 3], [3, 1]]
    n_2 = 4
    paths_2 = [[1, 2], [3, 4]]
    n_3 = 4
    paths_3 = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
    print(sol.gardenNoAdj(n_1, paths_1))
    print(sol.gardenNoAdj(n_2, paths_2))
    print(sol.gardenNoAdj(n_3, paths_3))