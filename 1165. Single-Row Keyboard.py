class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        look_up = {}
        res = 0
        pos = 0
        for i, ch in enumerate(keyboard):
            look_up[ch] = i
        for w in word:
            res += abs(pos - look_up[w])
            pos = look_up[w]
        return res


if __name__ == '__main__':
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    sol = Solution()
    print(sol.calculateTime(keyboard, word))