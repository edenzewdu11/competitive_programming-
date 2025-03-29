# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def generate_row(n: int):
            if n == 0:
                return [1]
            prev_row = generate_row(n - 1)
            curr_row = [1] 
            for j in range(1, n):
                curr_row.append(prev_row[j - 1] + prev_row[j])
            curr_row.append(1)  
            return curr_row
        
        return generate_row(rowIndex)