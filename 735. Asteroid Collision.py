from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            while ans and ans[-1] > 0 and a < 0:
                last = ans.pop()
                if -a == last:
                    a = 0
                elif -a < last:
                    a = last

            if a != 0:
                ans.append(a)
        return ans


if __name__ == '__main__':
    sol = Solution()
    aster =[-2,-1,1,2]
    print(sol.asteroidCollision(aster))
