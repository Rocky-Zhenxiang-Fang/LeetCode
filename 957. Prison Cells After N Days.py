from typing import List


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
        Idea: We know that if we found a status that have already been recorded, this means that we are already in a
        loop, we can fast forward
        """
        cell_day = {}
        remaining = 0   # if fast forwarded, stores the remaining day that cannot be fast forward
        for i in range(N):
            next_cell = self.next_day(cells)
            if tuple(next_cell) in cell_day:
                loop_length = i - cell_day[tuple(next_cell)]
                remaining = (N - cell_day[tuple(next_cell)] - 1) % loop_length
                cells = next_cell
                break
            else:
                cell_day[tuple(next_cell)] = i
                cells = next_cell

        for _ in range(remaining):
            next_cell = self.next_day(cells)
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
