from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        """
        Idea:
            Straight forward, zip the data and sorted it reversely. Check if it is valid, update it.
        """
        data = {i: (src, tar) for i, src, tar in zip(indexes, sources, targets)}
        res = []
        s_id = 0
        while s_id < len(S):
            if s_id in data and S[s_id: s_id + len(data[s_id][0])] == data[s_id][0]:
                res += list(data[s_id][1])
                s_id += len(data[s_id][0])
            else:
                res.append(S[s_id])
                s_id += 1

        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    S = "abcd"
    indexes = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    print(sol.findReplaceString(S, indexes, sources, targets))
