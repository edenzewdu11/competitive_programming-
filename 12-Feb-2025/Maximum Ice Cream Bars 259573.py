# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        sum=0
        for i in range(len(costs)):
            
            sum+=costs[i]
            if sum>coins:
                break
            else:
                 count+=1
        return count

        