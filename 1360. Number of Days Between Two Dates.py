class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        r1 = self.get_days(date1)
        r2 = self.get_days(date2)
        return abs(r2 - r1)

    def leap_year(self, year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        return True

    def get_days(self, date):
        y, m, d = map(int, date.split("-"))
        leaps = 0
        for year in range(1971, y):
            leaps += self.leap_year(year)
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = leaps + 365 * (y - 1971) + sum(months[:m]) + d
        if self.leap_year(y) and m > 2:
            res += 1
        return res