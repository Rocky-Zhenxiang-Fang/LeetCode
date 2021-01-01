class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        B2 = B * 2
        for i in range(len(B)):
            if B2[i] == A[0]:
                a_ptr = 0
                b_ptr = i
                while a_ptr != len(A):
                    if A[a_ptr] == B2[b_ptr]:
                        a_ptr += 1
                        b_ptr += 1
                    else:
                        break
                if a_ptr == len(A):
                    return True
        return False


if __name__ == '__main__':
    A = 'abcde'
    B = 'abced'
    sol = Solution()
    print(sol.rotateString(A, B))
