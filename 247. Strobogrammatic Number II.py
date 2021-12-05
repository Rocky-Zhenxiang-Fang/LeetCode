class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        temp = self._findStrobogrammatic(n)
        res = []
        for t in temp:
            if t[0] != "0":
                res.append(t)
        return res
    
    def _findStrobogrammatic(self, n: int) -> List[str]:
        """
        Idea: The core will be either 1 or 2, expend from there
        """
        if n == 1:
            return ["0", "1", "8"]
        elif n == 2:
            return ["11","69","88","96", "00"]
        else:
            core = self._findStrobogrammatic(n - 2)
            res = set()
            pair = [["1", "1"], ["6", "9"], ["8", "8"], ["9", "6"], ["0", "0"]]
            for c in core:
                for p in pair:
                    res.add(p[0] + c + p[1])
            return list(res)