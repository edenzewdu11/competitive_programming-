# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        ones = 0

        for c in s:
            if c == '1':
                ones += 1
            else:
                count += ones  
        return count
