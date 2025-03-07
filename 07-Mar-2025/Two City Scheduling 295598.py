# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x : x[0] - x[-1])

        min_dis = 0

        for i in range(n// 2):
            min_dis += costs[i][0]
        
        for i in range(n//2, n):
            min_dis += costs[i][1]
        
        return min_dis
      