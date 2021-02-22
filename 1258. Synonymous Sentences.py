from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        """
        Since synonyms might have overlaps, it will need to be turned into a Union find to prevent redundant lookups
        Then, use backtracking to build the solutions
        """
        union_map = {}  # string: its representative

        def find(word: str) -> str:  # return which set does this word belongs to
            if word not in union_map:  # this word have not be added into a union, create a union for it
                union_map[word] = word
            return union_map[word]

        def union(w1: str, w2: str) -> None:
            r1, r2 = find(w1), find(w2)
            if r1 == r2:
                return
            # always use the smaller value to be the representative, make r1 the smallest
            elif r1 > r2:
                r1, r2 = r2, r1
            for k in union_map:
                if union_map[k] == r2:
                    union_map[k] = r1

        for s in synonyms:
            union(s[0], s[1])

        words = text.split(' ')
        res = []

        def bt(i, sequence):  # backtracking method
            if i == len(words):
                res.append(' '.join(sequence))  # reached end of sentence, so append current sequence to results
                return
            r = find(words[i])  # will add words[i] to union find, no matter if synonyme or not
            for s in sorted([x for x in union_map if find(x) == r]):  # find all synonyms
                bt(i + 1, sequence + [s])  # start backtracking at next word

        bt(0, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
    text = "I am happy today but was sad yesterday"
    print(sol.generateSentences(synonyms, text))
