from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Idea:
            First, trim the string so that there is no extra " "
            Second, reverse the res string
            Last, reverse each words
        """
        res = []
        for i in range(len(s)):
            if s[i] != " ":
                res.append(s[i])
            else:
                if i != len(s) - 1 and res and res[-1] != " ":
                    res.append(" ")
        while res[-1] == " ":
            res.pop()
        # reverse the string
        self.reverse(res, 0, len(res) - 1)

        # reverse each word
        left = 0
        for right in range(len(res)):
            if res[right] == " ":
                self.reverse(res, left, right - 1)
                left = right + 1

        # reverse the last word
        self.reverse(res, left, len(res) - 1)

        return "".join(res)

    def reverse(self, s_list: List[str], start: int, end: int) -> None:
        while start < end:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    sol = Solution()
    s = "  hello world  "
    print(sol.reverseWords(s))
