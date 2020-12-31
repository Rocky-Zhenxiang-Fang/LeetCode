class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        reverse_flag = True
        for i in range(0, len(s), 2):
            sub = []
            for j in range(k):
                if i + j < len(s):
                    sub.append(s[i + j])
            if reverse_flag:
                res = res + sub[::-1]
            else:
                res = res + sub
            reverse_flag ^= 1
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    s = "abcdefg"
    k = 2
    print(sol.reverseStr(s, k))
