# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result=numBottles
        total=numExchange
        while total>=numExchange:
            full=numBottles//numExchange
            reminder=numBottles % numExchange
            total=full+reminder
           
            numBottles=total
            result+=full
            
        return result
