from typing import List


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        """
        Idea:
            For each ch in s, if its head matches any string in dict, see it those two matches
            If so, store the head and end into a list, merge if necessary
        """
        res = []
        heads = {}
        ans = []
        s_list = list(s)
        for d in dict:
            heads[d[0]] = heads.get(d[0], []) + [d]
        for h in heads:
            heads[h].sort(reverse=True)
        for i in range(len(s)):
            if s[i] in heads:  # found a possible substring
                can = heads[s[i]]
                for c in can:
                    if s[i: i + len(c)] == c:
                        if res:
                            for m in self.merge(res.pop(), [i, i + len(c) - 1]):
                                res.append(m)
                        else:
                            res.append([i, i + len(c) - 1])
                        break
        i = 0
        for r in res:
            ans = ans + s_list[i: r[0]] + ["<b>"] + s_list[r[0]: r[1] + 1] + ["</b>"]
            i = r[1] + 1
        ans += s_list[i:len(s)]
        return "".join(ans)

    def merge(self, range1: List[int], range2: List[int]) -> List[List[int]]:
        if range1[0] <= range2[0] <= range1[1] + 1:
            return [[range1[0], max(range1[1], range2[1])]]
        else:
            return [range1, range2]


if __name__ == '__main__':
    s = "aaabbcc"
    dict = ["aaa", "aab", "bc"]
    sol = Solution()
    print(sol.addBoldTag(s, dict))
