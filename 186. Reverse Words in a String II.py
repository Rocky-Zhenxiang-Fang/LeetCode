from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        left = 0
        for right in range(len(s)):
            if s[right] == " ":
                self.reverse(s, left, right - 1)
                left = right + 1
        self.reverse(s, left, len(s) - 1)

    def reverse(self, s: List[str], start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    sol = Solution()
    arr = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    sol.reverseWords(arr)
    print(arr)