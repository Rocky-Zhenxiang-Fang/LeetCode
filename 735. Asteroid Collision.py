from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Idea:
            Use stack to store the ans
            if one asteroid is added, see if it will collide to the previous one,
            if will, append the result and iterate
            if not, append the asteroid
        """
        res = [asteroids[0]]
        for i in range(1, len(asteroids)):
            ast = asteroids[i]
            while res and res[-1] > 0 and ast < 0:
                last = res.pop()
                if last > -ast:
                    ast = last
                elif last == -ast:
                    ast = 0
            if ast != 0:
                res.append(ast)
        return res


if __name__ == '__main__':
    sol = Solution()
    aster = [-2, -1, 1, 2]
    print(sol.asteroidCollision(aster))
