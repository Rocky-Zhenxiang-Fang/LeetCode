from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        import math
        res = set()
        x_max = 1 if x == 1 else int(math.log(bound, x)) + 1
        y_max = 1 if y == 1 else int(math.log(bound, y)) + 1
        for i in range(x_max): 
            for j in range(y_max): 
                if x ** i + y ** j <= bound:
                    res.add(set)
        return list(res)

        


if __name__ == '__main__':
    pass



