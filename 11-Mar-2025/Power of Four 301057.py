# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        while n>1:
            n=n/4
        if n==1:
            return True
        return False
     
        