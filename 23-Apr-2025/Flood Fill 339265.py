# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == original_color:
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image

        