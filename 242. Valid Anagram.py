class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        visited = {}
        for ch in s:
            if ch in visited:
                visited[ch] += 1
            else:
                visited[ch] = 1

        for ch in t:
            if ch not in visited or visited[ch] < 1:
                return False
            else:
                visited[ch] -= 1
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))