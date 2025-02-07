# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        col=len(matrix[0])
        start_row=0
        end_row=row-1
        start_col=0
        end_col=col-1
        ans=[]
        while start_row<=end_row:
            for j in range(start_col,end_col+1):
                ans.append(matrix[start_row][j])

            if len(ans)==row*col:
                break
            for i in range(start_row+1,end_row+1):
                ans.append(matrix[i][end_col])
            if len(ans)==row*col:
                break
            for j in range(end_col-1,start_col-1,-1):
                ans.append(matrix[end_row][j])
            if len(ans)==row*col:
                break
            for i in range(end_row-1,start_row,-1):
                ans.append(matrix[i][start_col])
            if len(ans)==row*col:
                break

            start_row+=1
            start_col+=1
            end_row-=1
            end_col-=1
        return ans
        

            


            



        