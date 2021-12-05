from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Idea:
            Consider it a graph, find the longest acyclic path
            for each nums, if it havn't be assigned to a path, start from there, return the max
        """
        max_length = [0] * len(nums)
        for i in range(len(nums)):
            if max_length[i] == 0:
                path = set()
                order = []
                j = i
                while j not in path and max_length[j] == 0:
                    path.add(j)
                    order.append(j)
                    j = nums[j]
                offset = max_length[j]
                for k in range(len(order)):
                    max_length[order[k]] = len(order) - k + offset
        return max(max_length)
                    

if __name__ == '__main__':
    sol = Solution()
    arr = [5,4,0,3,1,6,2]
    print(sol.arrayNesting(arr))           
                    
                
                