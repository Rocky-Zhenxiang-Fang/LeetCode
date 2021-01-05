from typing import List, Tuple


class Solution:
    def prisonAfterNDays_naive(self, cells: List[int], N: int) -> List[int]:
        """
        Idea: Run though N days and return the result of last day
        """
        for _ in range(N):
            next_cell = self.next_day(cells)
            cells = next_cell
        return cells

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """
        Idea: Since we know that there are only eight cells, their only be 2^8 different combinations, and the rule
            only takes the current cells as input, making it possible to loop.
            Thus, we can memorize the paths, if we encounter a visited situation, we can fast forward
        """
        seen = {}
        day = 0
        isFasted = False
        while day < N:
            day += 1
            next_cell = self.next_day(cells)
            if tuple(next_cell) in seen and not isFasted:
                day += ((N - day) // (day - seen[tuple(next_cell)])) * (day - seen[tuple(next_cell)])
                isFasted = True
            else:
                seen[tuple(next_cell)] = day
            cells = next_cell
        return cells

    def next_day(self, cells: List[int]) -> List[int]:
        res = [0]
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]:
                res.append(1)
            else:
                res.append(0)
        res.append(0)
        return res


if __name__ == '__main__':
    cells = [1,0,0,1,0,0,1,0]
    N = 1000000000
    cells_2 = [0, 1, 0, 1, 1, 0, 0, 1]
    N_2 = 7
    sol = Solution()
    print(sol.prisonAfterNDays_naive(cells_2, N_2))
    print(sol.prisonAfterNDays(cells, N))
