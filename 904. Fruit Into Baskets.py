from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        """
        The only reason why we will get stuck is that both baskets are fulled,
        in this case, we want to take out fruits by order until we have a empty basket
        """
        collected = {
            -1: 0,
            -2: 0
        }   # [type of fruit: number], -1 and -2 are place holder
        start, end = 0, 0
        result = 0
        while end != len(tree):
            if tree[end] in collected:
                collected[tree[end]] += 1
                end += 1
            elif 0 in collected.values():
                for i in collected:
                    if collected[i] == 0:
                        collected[tree[end]] = 1
                        break
                collected.pop(i)
                end += 1
            else:
                result = max(result, sum(collected.values()))
                while 0 not in collected.values():
                    collected[tree[start]] -= 1
                    start += 1
        return max(result, sum(collected.values()))


if __name__ == '__main__':
    trees = [3,3,3,1,2,1,1,2,3,3,4]
    sol = Solution()
    print(sol.totalFruit(trees))
