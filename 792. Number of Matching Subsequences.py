from typing import List


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        iters = [[] for _ in range(26)]
        res = 0
        for w in words:
            it = iter(w)
            iters[ord(next(it)) - ord("a")].append(it)
        for ch in S:
            old_its = iters[ord(ch) - ord("a")]
            iters[ord(ch) - ord("a")] = []
            while old_its:
                it = old_its.pop()
                value = next(it, None)
                if not value:
                    res += 1
                else:
                    iters[ord(value) - ord("a")].append(it)
        return res


if __name__ == '__main__':
    sol = Solution()
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(sol.numMatchingSubseq(S, words))
