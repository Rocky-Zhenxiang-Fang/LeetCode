"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
"""



from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        """
        Since we know the boundary of x, y, we can draw the grid of answers, and the answer turns to find targets
        of sorted array
        If we found an answer, add it to the result set, and go for either direction.
        Also, if a cell is seen before, since we are using a DFS, ignore this cell
        """
        x_min, x_max = 1, 1000
        y_min, y_max = 1, 1000
        x, y = x_min, y_max
        stack = []
        res = []
        seen = set()
        while x <= x_max and y >= y_min:
            if (x, y) not in seen:
                seen.add((x, y))
                if customfunction.f(x, y) > z:
                    stack.append([x, y - 1])
                elif customfunction.f(x, y) < z:
                    stack.append([x + 1, y])
                else:
                    res.append([x, y])
                    stack.append([x, y - 1])
                    stack.append([x + 1, y])
            x, y = stack.pop()
        return res


if __name__ == '__main__':
    sol = Solution()
    cu = CustomFunction()
    print(sol.findSolution(cu, 5))
