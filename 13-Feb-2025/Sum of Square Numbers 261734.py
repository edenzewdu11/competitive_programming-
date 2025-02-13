# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))

        while left <= right:
            square_sum = left * left + right * right
            
            if square_sum == c:
                return True
            elif square_sum < c:
                left += 1
            else:
                right -= 1

        return False

        
        