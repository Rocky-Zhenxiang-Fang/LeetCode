class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        from collections import Counter
        if len(A) != len(B):
            return False
        if A == B:
            counter = Counter(A)
            for k in counter:
                if counter[k] > 1:
                    return True
            return False
        diff1, diff2 = -1, -1
        for i in range(len(A)):
            if A[i] != B[i]:
                if diff1 == -1:
                    diff1 = i
                elif diff2 == -1:
                    diff2 = i
                else:
                    return False
        if diff1 != -1 and diff2 == -1:
            return False
        return A[diff1] == B[diff2] and A[diff2] == B[diff1]


if __name__ == '__main__':
    sol = Solution()
    A = "ab"
    B = "ab"
    print(sol.buddyStrings(A, B))
