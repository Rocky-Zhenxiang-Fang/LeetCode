class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        s_map, g_map = [0 for _ in range(10)], [0 for _ in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                s = int(secret[i])
                g = int(guess[i])
                s_map[s] += 1
                g_map[g] += 1
                if g_map[s] > 0:
                    g_map[s] -= 1
                    s_map[s] -= 1
                    b += 1
                if s_map[g] > 0:
                    s_map[g] -= 1
                    g_map[g] -= 1
                    b += 1
        return str(a) + "A" + str(b) + "B"


if __name__ == '__main__':
    se = "1807"
    gu = "7810"
    sol = Solution()
    print(sol.getHint(se, gu))