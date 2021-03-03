import collections
from typing import List, Dict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Idea:
            Shortest path with rules: Could use BFS
            Instead of finding the relationship between words, we first narrow the search space to possible words, then
            find out the words that matches
        """
        if beginWord not in wordList:
            wordList.append(beginWord)
        rules = self._construct_dict(wordList)
        visited = set()
        que = collections.deque([(beginWord, 1)])
        while que:
            curr, level = que.pop()
            if curr not in visited:
                visited.add(curr)
                if curr == endWord:
                    return level
                else:
                    for i in range(len(curr)):
                        s = curr[:i] + "_" + curr[i + 1:]
                        nei_words = rules.get(s, [])
                        for nei in nei_words:
                            que.appendleft((nei, level + 1))
        return 0

    def _construct_dict(self, word_list: List[str]):
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

    def ladderLength_2(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "dog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sol = Solution()
    print(sol.ladderLength_2(beginWord, endWord, wordList))

