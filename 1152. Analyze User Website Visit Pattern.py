from typing import List, Set, Tuple


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_other = {}
        paths = set()
        path_counter = {}
        for i in range(len(username)):
            if username[i] not in user_other:
                user_other[username[i]] = [(timestamp[i], website[i])]
            else:
                user_other[username[i]] = user_other[username[i]] + [(timestamp[i], website[i])]
        for k in user_other:
            user_other[k].sort(key=lambda x: x[0])
            self.unique_paths(paths, user_other[k], [])
            for p in paths:
                path_counter[p] = path_counter.get(p, 0) + 1
            paths.clear()
        res, count = None, 0
        for p, c in path_counter.items():
            if c > count:
                res = p
                count = c
            elif c == count and res > p:
                res = p
        return res

    def unique_paths(self, paths: Set[Tuple[str]], webs, sub):
        if len(sub) == 3:
            t = tuple(sub)
            paths.add(t)
            return
        elif not webs:
            return
        else:
            for i in range(len(webs)):
                self.unique_paths(paths, webs[i + 1:], sub + [webs[i][1]])


if __name__ == '__main__':
    username = ["u1", "u1", "u1", "u2", "u2", "u2"]
    timestamp = [1, 2, 3, 4, 5, 6]
    website = ["a", "b", "c", "a", "b", "a"]
    sol = Solution()
    print(sol.mostVisitedPattern(username, timestamp, website))
