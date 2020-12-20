from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}
        for s in strs:
            s_key = "".join(sorted(list(s)))
            sorted_map[s_key] = sorted_map.get(s_key, []) + [s]
        return list(sorted_map.values())


if __name__ == '__main__':
    sol = Solution()
    arr = ["ddddddddddg","dgggggggggg"]
    print(sol.groupAnagrams(arr))