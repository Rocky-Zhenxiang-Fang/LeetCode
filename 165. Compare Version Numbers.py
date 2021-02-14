from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = self.clean_version(version1)
        v2 = self.clean_version(version2)
        i = 0
        while i < len(v1) or i < len(v2):
            val1 = v1[i] if i < len(v1) else 0
            val2 = v2[i] if i < len(v2) else 0
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
            i += 1
        return 0

    def clean_version(self, version: str) -> List[int]:
        inter = version.split(".")
        res = []
        for i in range(len(inter)):
            val = inter[i].lstrip("0")
            if len(val) > 0:
                res.append(int(val))
            else:
                res.append(0)
        return res


if __name__ == '__main__':
    sol = Solution()
    version1 = "0.1"
    version2 = "1.1"
    print(sol.compareVersion(version1, version2))
