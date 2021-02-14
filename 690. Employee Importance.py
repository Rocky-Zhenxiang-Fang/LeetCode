# Definition for Employee.
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        emp_map = {}
        for e in employees:
            emp_map[e.id] = (e.importance, e.subordinates)
        remains = [id]
        while remains:
            val, sub = emp_map[remains.pop()]
            res += val
            for s in sub:
                remains.append(s)

        return res
