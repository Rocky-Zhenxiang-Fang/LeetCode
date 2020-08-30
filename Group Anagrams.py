class Solution(object):
    # Time Limit Exceeded
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     res = []
    #     while len(strs) != 0:
    #         sub = self.findAnagrams(strs[0], strs)
    #         for s in sub:
    #             strs.remove(s)
    #         res.append(sub)
    #     return res
    #
    # def findAnagrams(self, tar, strs):
    #     from collections import Counter
    #     tarCounter = Counter(tar)
    #     subAns = []
    #     for s in strs:
    #         sCounter = Counter(s)
    #         if sCounter == tarCounter:
    #             subAns.append(s)
    #     return subAns

    def groupAnagrams(self, strs):
        """
        If two strings are anagrams, then after sorted, they will be the same
        """
        map = {}
        for s in strs:
            a = "".join(sorted(s))
            map[a] = map.get(a, []) + [s]
        return map.values()


if __name__ == '__main__':
    arr = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    print(sol.groupAnagrams(arr))
