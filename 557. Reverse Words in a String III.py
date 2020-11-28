class Solution:
    #     def reverseWords(self, s: str) -> str:
    #         stack = []  # only use append and pop
    #         res = []
    #         for c in s:
    #             if c == " ":
    #                 while stack:
    #                     res.append(stack.pop())
    #                 res.append(" ")
    #             else:
    #                 stack.append(c)
    #         while stack:
    #             res.append(stack.pop())
    #         return "".join(res)
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])[::-1]
