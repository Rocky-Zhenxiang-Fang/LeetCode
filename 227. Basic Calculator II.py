class Solution:
    def calculate(self, s: str) -> int:
        curr, last_num, result, opt = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                curr = 10 * curr + int(c)
                continue
            if opt == '+':
                result += last_num
                last_num = curr
            elif opt == '-':
                result += last_num
                last_num = -curr
            elif opt == '*':
                last_num = last_num * curr
            elif opt == '/':
                last_num = int(last_num / curr)
            curr, opt = 0, c
        return result + last_num


if __name__ == '__main__':
    sol = Solution()
    s = "19 + 23 - 47 * 100 / 20 + 5"
    print(sol.calculate(s))
