from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        """
        Idea:
            Straight forward, zip the data, sort it reversively to prevent touching unused data
        """
        data = sorted(zip(indexes, sources, targets), key=lambda x: -x[0])
        s_list = list(S)
        for d in data:
            ind, src, tar = d
            if S[ind:].startswith(src):
                s_list = s_list[:ind] + list(tar) + s_list[ind + len(src):]
        return "".join(s_list)



if __name__ == '__main__':
    sol = Solution()
    S = "abcd"
    indexes = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    print(sol.findReplaceString(S, indexes, sources, targets))
