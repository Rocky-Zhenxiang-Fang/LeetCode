from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Idea:
            DFS can find all nodes in a connected component
        """
        ans = 0

        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                ans += 1
                stack = [i]
                while stack:
                    curr = stack.pop()
                    if curr not in visited:
                        visited.add(curr)
                        for j in range(len(isConnected[curr])):
                            if isConnected[curr][j] == 1:
                                stack.append(j)
        return ans


if __name__ == '__main__':
    isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    sol = Solution()
    print(sol.findCircleNum(isConnected))
