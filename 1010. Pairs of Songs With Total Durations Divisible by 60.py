from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        Idea: for each t in time, as long as there are visited song that is its complement, we can add their pair to the
        answer. Complement means that time[i]%60 + time[j]%60 = 0
        """
        visited = [0 for _ in range(60)]
        res = 0
        for t in time:
            i = t % 60
            com = 60 - i
            if com == 60:
                res += visited[0]
            else:
                res += visited[com]
            visited[i] += 1
        return res


if __name__ == '__main__':
    time = [60, 60, 60]
    sol = Solution()
    print(sol.numPairsDivisibleBy60(time))
