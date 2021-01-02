from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        # 1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        # 2). split the string into words
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        # 3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        # 4). return the word with the highest frequency
        max_occur = 0
        res = ""
        for w in word_count:
            if word_count[w] > max_occur:
                max_occur = word_count[w]
                res = w
        return res


if __name__ == '__main__':
    paragraph = "Bob. hIt, baLl"
    banned = ["hit"]
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))
