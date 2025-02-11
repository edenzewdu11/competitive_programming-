# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row=len(mat)
        col=len(mat[0])
        for _ in range(4):
            transpose=[]
            for c in range(col):
                arr=[]
                for r in range(row-1,-1,-1):
                    arr.append(mat[r][c])
                transpose.append(arr)
            for row2, row1 in zip (transpose,target):
                if row1!=row2:
                    break
            else:
                return True

            mat=transpose
            
        return False

        