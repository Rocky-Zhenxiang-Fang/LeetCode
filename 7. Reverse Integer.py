import collections


class Solution:
    def reverse_list(self, x: int) -> int:
        xStr = str(x)
        res = collections.deque()
        negetive = False
        for i in range(len(xStr) - 1, -1, -1):
            if xStr[i] == "-":
                negetive = True
                continue
            res.append(xStr[i])

        while res[0] == "0" and len(res) > 1:
            res.popleft()
        if negetive:
            res.appendleft("-")
        ans = int("".join(list(res)))
        return ans if -2 ** 31 <= ans <= 2 ** 31 - 1 else 0

if __name__ == '__main__':
    sol = Solution()
    text = 123
    "{0:b}".format(text)
    print(sol.reverse(text))

