# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(m): 
            new_row = []
            for j in range(n):  
                new_row.append(matrix[j][i]) 
            arr.append(new_row)  
        
        return arr


        