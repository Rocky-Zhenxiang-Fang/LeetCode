class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        self.dfs(res, "", digits, 0, mapping)
        return res

    def dfs(self, res, current, digits, index, mapping):
        """
        If current has the length equals to digits, the it is finished, add it into res
        if not, get the string that correspond to mapping[digits[index]]
        iterate though all ch in the string
            recursive calls dfs and add ch into the last of current, increments index by one
        :param res: stores the answer
        :param current: the string that is be processing this round
        :param digits: digits that is passed in from the main function
        :param index: the index of digits that is going to be add into current
        :param mapping: maps digits to string
        """
        if index == len(digits):  # current is already finished
            res.append(current)
            return
        s = mapping[digits[index]]
        for i in range(len(s)):
            self.dfs(res, current + s[i], digits, index + 1, mapping)



