class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        left, right = 0, len(A) - 1
        swapped = False
        need_swap = False
        while left < right:
            if A[left] == B[left]:
                left += 1
            elif A[right] == B[right]:
                need_swap = True
                right -= 1
            else:
                if A[left] == B[right] and A[right] == B[left] and not swapped:
                    left += 1
                    right -= 1
                    swapped = True
                    need_swap = False
                else:
                    return False
        return not need_swap


if __name__ == '__main__':
    sol = Solution()
    A = "ab"
    B = "ab"
    print(sol.buddyStrings(A, B))
