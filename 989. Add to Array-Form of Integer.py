from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res = []
        carry = 0
        a_ptr = len(A) - 1
        while K != 0 or a_ptr >= 0:
            val_a = A[a_ptr] if a_ptr >= 0 else 0
            val_k = K % 10
            value = val_a + val_k + carry
            carry = value // 10
            value %= 10
            res.append(value)
            K //= 10
            a_ptr -= 1
        if carry:
            res.append(carry)
        return res[::-1]


if __name__ == '__main__':
    sol = Solution()
    A = [1, 2, 0, 0]
    K = 34
    print(sol.addToArrayForm(A, K))


