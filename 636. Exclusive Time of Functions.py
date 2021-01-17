from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Idea:
            1. Since it only have one core, anytime a process is replace, the time it used can be added on
            2. We can use a stack to save any tasks that is in background
            3. We need to treat start and end differently based on the time
        """
        ans = [0 for _ in range(n)]
        time = 0  # indicates the time of start
        stack = []
        for l in logs:
            name, typ, t = l.split(":")
            if typ == "start":
                if stack:
                    ans[int(stack[-1])] += int(t) - time
                time = int(t)
                stack.append(name)
            else:
                ans[int(stack.pop())] += int(t) - time + 1
                time = int(t) + 1
        return ans



if __name__ == '__main__':
    sol = Solution()
    n = 2
    logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    print(sol.exclusiveTime(n, logs))
