class Solution:
    def strStrMy(self, haystack: str, needle: str) -> int:
        """
        Slow
        """
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                for j in range(i, len(needle) + i):
                    if j >= len(haystack):
                        return -1
                    if haystack[j] != needle[j - i]:
                        break

                    if j == len(needle) + i - 1:
                        return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Uses list comparision, also instead of check each substring when encounter, wwe store it's index,
        and check if it is valid
        """
        if needle not in haystack:
            return -1
        if len(needle) == 0:
            return 0
        l, b = [],[]
        x = list(haystack)
        y = list(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                l.append(i)
        for k in l:
            if k + len(needle) <= len(haystack):
                b.append(k)
        for j in b:
            if x[j:len(needle)+j] == y:
                break
        return j