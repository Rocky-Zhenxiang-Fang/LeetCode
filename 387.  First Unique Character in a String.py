class Solution:
    def firstUniqCharSlow(self, s: str) -> int:
        """
        Slow, Time O(2 * n)
        """
        if len(s) == 0:
            return -1
        visited = {}
        for i in range(len(s)):
            if s[i] in visited:
                visited[s[i]] = float("inf")
            else:
                visited[s[i]] = i
        ans = min(visited.items(), key=lambda x: x[1])
        return ans[1] if ans[1] != float("inf") else -1

    def firstUniqChar(self, s: str) -> int:
        """
        instead of using a map, since we know that there is only lowercase characters,
        we can use a list
        Time O(2 * n)
        """
        visited = [0 for _ in range(26)]

        for ch in s:
            visited[ord(ch) - int("a")] += 1
        for i in range(len(s)):
            if visited[int(s[i]) - int("a")] == 1:
                return i

        return -1