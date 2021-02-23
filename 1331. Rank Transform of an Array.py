from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a_sorted = sorted(arr)
        ranks = {}
        res = []
        ranks[a_sorted[0]] = 1
        for i in range(1, len(a_sorted)):
            if a_sorted[i] not in ranks:
                ranks[a_sorted[i]] = ranks[a_sorted[i - 1]] + 1
        for i in range(len(arr)):
            res.append(ranks[arr[i]])

        return res


if __name__ == '__main__':
    sol = Solution()
    arr = [100, 100, 100]
    print(sol.arrayRankTransform(arr))



