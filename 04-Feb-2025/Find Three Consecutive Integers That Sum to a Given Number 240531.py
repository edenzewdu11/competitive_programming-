# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x=num//3
        
        if num%3!=0:
            return []
        else:
            return [x-1,x,x+1]

        return [x-1,x,x+1]
        
        