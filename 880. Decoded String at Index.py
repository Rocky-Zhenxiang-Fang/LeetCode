class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        """
        Brute Force
        """
        res = []
        i = 0
        while i < len(S):
            if S[i].isalpha():
                res.append(S[i])
            else:
                res = res * int(S[i])
            i += 1
        return res[K - 1]


if __name__ == '__main__':
    test_str = "leet2code3"
    test_k = 10
    sol = Solution()
    print(sol.decodeAtIndex(test_str, test_k))
