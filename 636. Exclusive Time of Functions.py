from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Idea:
            start -> end, start -> pause, pause -> end are same things
            when any of above happens, update result time
            pop out element when id matches and start -> end
            treat start and end differently
        """
        stack = []  # stores [task, time(start)]
        res = [0] * n
        for line in logs:
            task, status, time = line.split(":")
            task = int(task)
            time = int(time)
            if stack:  # pause previous task
                if status == "start":
                    res[stack[-1][0]] += time - stack[-1][1]
                else:  # terminates the last task, and either updates the start time of previous task or wait for the next task
                    l_task, l_time = stack.pop()
                    res[l_task] += time + 1 - l_time  # +1 since this is the end time
                    if stack:
                        stack[-1][1] = time + 1
            if status == "start":
                stack.append([task, time])
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 2
    logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    print(sol.exclusiveTime(n, logs))
