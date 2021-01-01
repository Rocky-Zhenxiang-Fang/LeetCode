from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        Insight:
            Since each element is distinct, if a element in arr is considered the head of pieces, there will only be one
            candidate, we only need to check if this piece can be put in place
        Pseudocode:
            store each p in pieces in dict with (head, index)
            assign a pointer to iterate arr
            while pointer in arr:
                find the piece that have the same head with arr[pointer]
                check if each element follows the order
                    if not:
                    return False
            return True
        """
        heads = {}
        for i in range(len(pieces)):
            heads[pieces[i][0]] = i
        ptr = 0
        while ptr < len(arr):
            if arr[ptr] not in heads:
                return False
            else:
                piece = pieces[heads[arr[ptr]]]
                for p in piece:
                    if p != arr[ptr]:
                        return False
                    else:
                        ptr += 1
        return True


if __name__ == '__main__':
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    sol = Solution()
    print(sol.canFormArray(arr, pieces))
