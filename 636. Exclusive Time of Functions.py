from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Idea:
            Since it only have one core, anytime a process is replace, the time it used can be added on
        """
        log_list = [l.split(":") for l in logs]
        res = [0 for _ in range(n)]
        task = -1
        time = 0
        for log in log_list:
            if task != -1:
                res[task] += int(log[2]) - time
                if log[1] == "end":
                    res[task] += 1
                    time += 1
            task = int(log[0])
            time = int(log[2])
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 2
    logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    print(sol.exclusiveTime(n, logs))
