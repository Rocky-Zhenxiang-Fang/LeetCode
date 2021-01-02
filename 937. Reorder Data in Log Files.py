from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digs = []
        lets = []
        for l in logs:
            if l.split(" ")[1].isdigit():
                digs.append(l)
            else:
                lets.append(l)
        lets.sort(key=lambda x: x.split()[0])
        lets.sort(key=lambda x: x.split()[1:])
        return lets + digs


if __name__ == '__main__':
    sol = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(sol.reorderLogFiles(logs))
