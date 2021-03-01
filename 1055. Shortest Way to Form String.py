class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        Idea:
            Starting from the head of target, find the next index of char that is in source
            If the index next index is at the head of source, res += 1
            if after searching for a round and a answer cannot be found, return -1
        """

        def find_next(s_id: int, tar):
            for i in range(s_id, len(source)):
                if source[i] == tar:
                    return i
            for i in range(s_id):
                if source[i] == tar:
                    return i
            return -1

        res = 1
        src_id = 0
        for i, t in enumerate(target):
            new_id = find_next(src_id, t)
            if new_id == -1:
                return -1
            if src_id > new_id or (new_id == len(source) - 1 and i != len(target) - 1):
                res += 1
            src_id = (new_id + 1) % len(source)

        return res



if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    t = "abcbc"
    print(sol.shortestWay(s, t))
