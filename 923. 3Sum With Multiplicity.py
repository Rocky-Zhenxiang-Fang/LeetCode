import collections
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = collections.Counter(arr)
        keys = sorted(counter.keys())
        res = 0
        for i in range(len(keys)):
            left, right = i, len(keys) - 1
            while left <= right:
                if keys[i] + keys[left] + keys[right] == target:
                    if keys[i] == keys[left] == keys[right]:
                        res += counter[keys[i]] * (counter[keys[i]] - 1) * (counter[keys[i]] - 2) // 6
                    elif keys[i] == keys[left]:
                        res += (counter[keys[i]] * (counter[keys[i]] - 1) * counter[keys[right]]) // 2
                    elif keys[left] == keys[right]:
                        res += (counter[keys[i]] * (counter[keys[right]] - 1) * counter[keys[right]]) // 2
                    else:
                        res += counter[keys[i]] * counter[keys[left]] * counter[keys[right]]
                    left += 1
                    right -= 1
                elif keys[i] + keys[left] + keys[right] > target:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 1, 2, 2, 2, 2]
    tar = 5
    print(sol.threeSumMulti(arr, tar))