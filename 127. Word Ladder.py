from collections import deque
from typing import List


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        https://leetcode.com/problems/word-ladder/discuss/40723/Simple-to-understand-Python-solution-using-list-preprocessing-and-BFS-beats-95
        """
        def construct_dict(word_list):
            """
            Idea: For each word, get all possible way to form different words, store it as the key of the dict,
            the value will be all words in the word list that can be written in this key
            """
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(set(wordList) | {beginWord, endWord})
        return bfs_words(beginWord, endWord, d)


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))
