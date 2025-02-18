# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.prefix_sum[i][j] = matrix[i-1][j-1] + self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] - self.prefix_sum[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       
        return (self.prefix_sum[row2+1][col2+1] 
                - (self.prefix_sum[row1][col2+1] if row1 > 0 else 0)
                - (self.prefix_sum[row2+1][col1] if col1 > 0 else 0)
                + (self.prefix_sum[row1][col1] if row1 > 0 and col1 > 0 else 0))
