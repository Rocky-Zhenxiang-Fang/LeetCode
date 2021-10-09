from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res = 0
        properties.sort()
        most_defense = -float("inf")
        most_attack = properties[-1][0]
        print(properties)
        print(most_defense)
        print(most_attack)
        for i in range(len(properties) - 2, -1, -1):
            most_defense = max(most_defense, properties[i + 1][1])
            if properties[i][1] < most_defense and properties[i][0] < most_attack:
                res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    arr = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
    print(sol.numberOfWeakCharacters(arr))