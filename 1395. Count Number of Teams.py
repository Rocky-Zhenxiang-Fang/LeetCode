from typing import List, Set, Tuple


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        Idea:
            For each solider, the number of team that it will be included is the less * greater + greater * less (left * right)
        Improved:
            https://leetcode.com/problems/count-number-of-teams/discuss/724711/Easiest-Code-Ever-Python-Top-97-Speed-O(-n-log-n-)-Combinatorial
        """
        res = 0
        for i in range(1, len(rating)):
            left_less, left_greater, right_less, right_greater = 0, 0, 0, 0
            for j in range(len(rating)):
                if i == j:
                    continue
                elif i > j:
                    if rating[i] > rating[j]:
                        left_less += 1
                    else:
                        left_greater += 1
                else:
                    if rating[i] > rating[j]:
                        right_less += 1
                    else:
                        right_greater += 1
            res += left_greater * right_less + left_less * right_greater
        return res

if __name__ == '__main__':
    sol = Solution()
    arr = [2, 5, 3, 4, 1]
    print(sol.numTeams(arr))
