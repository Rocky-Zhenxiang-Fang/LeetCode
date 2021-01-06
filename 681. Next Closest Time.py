class Solution:
    def nextClosestTime(self, time: str) -> str:
        """
        Idea:
            Starting from the last digit, see if it can be increase,
                if not, go to the next digit, and this digit will turn to the smallest possbile number
        """
        numbers = sorted(list({time[i] for i in [0, 1, 3, 4]}))
        original_time = time
        time = [time[i] for i in [0, 1, 3, 4]]
        for i in range(len(time) - 1, -1, -1):
            if time[i] != numbers[-1]:  # for this digit, this index can be increased
                j = numbers.index(time[i]) + 1
                while j < len(numbers):
                    time[i] = numbers[j]
                    if self.is_vaild(int("".join(time))):
                        return "".join(time[:2] + [":"] + time[2:])
                    j += 1
            time[i] = numbers[0]
        return "".join(time[:2] + [":"] + time[2:])

    def is_vaild(self, time: int) -> bool:
        if 0 <= time < 2400 and 0 <= (time % 100) < 60:
            return True


if __name__ == '__main__':
    sol = Solution()
    test_1 = "15:55"
    print(sol.nextClosestTime(test_1))
