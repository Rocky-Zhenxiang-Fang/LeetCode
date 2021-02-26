from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        count = Counter(arr)
        seen = set()
        for c in count:
            if count[c] in seen:
                return False
            else:
                seen.add(count[c])
        return True


if __name__ == '__main__':
    arr = [1, 2, 2, 1, 1, 3]
    sol = Solution()
    print(sol.uniqueOccurrences(arr))