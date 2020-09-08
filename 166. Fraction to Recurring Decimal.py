class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # corner case:
        if numerator == 0:
            return "0"
        if denominator == 0:
            return "False"
        sig = "-" if numerator * denominator < 0 else ""
        head, reminder = divmod(abs(numerator), abs(denominator))
        res = [sig + str(head), "."]
        seenReminder = {}
        i = 2
        while reminder != 0:
            if reminder not in seenReminder:
                seenReminder[reminder] = i
                reminder *= 10
                dig, reminder = divmod(reminder, abs(denominator))
                res.append(str(dig))
                i += 1
            else:
                res.insert(seenReminder[reminder], "(")
                res.append(")")
                break
        if res[-1] == ".":
            res.pop()
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(2, 3))
