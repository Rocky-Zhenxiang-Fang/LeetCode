from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets = {}    # stores fruit: number
        fruits = [] # stores the index of each fruit
        res = 0
        for i, t in enumerate(tree):
            if t in baskets:
                baskets[t] += 1
                fruits.append(i)
            else:
                while len(baskets) >= 2:
                    removed = tree[fruits.pop()]
                    baskets[removed] -= 1
                    if baskets[removed] == 0:
                        baskets.pop(removed)
                baskets[t] = 1
                fruits.append(i)
            res = max(res, len(fruits))
        return res



if __name__ == '__main__':
    trees = [1,2,3,2,2]
    sol = Solution()
    print(sol.totalFruit(trees))
