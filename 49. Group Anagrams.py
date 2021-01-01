from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}
        for s in strs:
            key = tuple(sorted(s))
            sorted_map[key] = sorted_map.get(key, []) + [s]
        return list(sorted_map.values())

if __name__ == '__main__':
    sol = Solution()
    arr =  ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(arr))