class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for _ in range(n - 1):
            ans = self.helper(ans)
        return ans

    def helper(self, s: str) -> str:
        ind = 0
        count = 0
        res = ""
        prev = s[0]
        while ind + count < len(s):
            if s[ind + count] != prev:
                res += str(count) + prev
                prev = s[ind + count]
                ind = ind + count
                count = 1
            else:
                count += 1
        if count != 0:
            res += str(count) + prev
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.countAndSay(4))
