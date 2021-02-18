from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        data = sorted(zip(indexes, sources, targets), key=lambda x: -x[0])
        res = []
        i = 0
        while i < len(S):
            if data and i == data[-1][0]:
                id, source, target = data.pop()


            else:
                res.append(S[i])
                i += 1

        return "".join(res)