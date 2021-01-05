from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        words_counter = Counter(words)
        ordered = sorted(list(words_counter.items()), key=lambda x: (x[1], x[0]))  # first sorted in alphabetical order to preserve this
        return [ordered[i][0] for i in range(-1, -k - 1, -1)]


if __name__ == '__main__':
    w = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    sol = Solution()
    print(sol.topKFrequent(w, k))
