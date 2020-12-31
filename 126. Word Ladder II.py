from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Idea:
            Since the ladder needed to be printed out, backtracking is good to use
            Also, there are rules for transformation, which can we consider as neighbor in graphs
            Finally, since it is finding the shortest path, BFS will be helpful
        """
        from collections import deque
        neighbor = {}
        res = []

        if endWord not in wordList:
            return res
        if beginWord not in wordList:
            wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                head = "".join(w[:i] + "-" + w[i + 1:])
                neighbor[head] = neighbor.get(head, []) + [w]
        que = deque()
        que.appendleft((beginWord, []))
        visited = {}
        while que:
            word, path = que.pop()
            layer = len(path)
            if res and len(res[0]) <= len(path):
                break
            if word not in visited or visited[word] == layer:
                if word == endWord:
                    res.append(path + [word])
                else:
                    visited[word] = layer
                    for j in range(len(word)):
                        head = "".join(word[:j] + "-" + word[j + 1:])
                        for n in neighbor[head]:
                            if n not in visited:
                                que.appendleft((n, path + [word]))
        return res


if __name__ == '__main__':
    begin = "red"
    end = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    sol = Solution()
    print(sol.findLadders(begin, end, wordList))
