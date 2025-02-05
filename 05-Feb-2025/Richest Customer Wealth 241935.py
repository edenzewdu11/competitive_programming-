# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        count=0
        arr=[]
        for i in accounts:
            
            for j in i:
                count+=j
    
            arr.append(count)
            count=0
        return max(arr)

        