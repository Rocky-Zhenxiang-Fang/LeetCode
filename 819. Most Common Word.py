from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        paragraph = paragraph.lower()
        banned = set(banned)
        banned.add(" ")
        punctuations = "!?',;."
        for p in punctuations:
            paragraph = paragraph.replace(p, " ")
        counter = Counter(paragraph.split())
        max_occur = 0
        res = " "
        for k in counter:
            v = counter[k]
            if k not in banned and v > max_occur:
                max_occur = v
                res = k
        return res


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))
