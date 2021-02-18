from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        data = sorted(zip(indexes, sources, targets), key=lambda x: -x[0])
        res = list(S)
        for d in data:
            id, source, target = d[0], d[1], d[2]
            if S[id:id+len(source)] == source:
                res = res[:id] + list(target) + res[id + len(source):]
        return "".join(res)
