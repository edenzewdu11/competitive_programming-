# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr=[]
        while columnNumber>0:
            reminder=columnNumber%26
            if reminder==0:
                reminder=26
            arr.append(chr(reminder+64))
            if columnNumber%26==0:
                columnNumber//=26
                columnNumber-=1
            else:
                columnNumber//=26
        arr.reverse()
        return "".join(arr)
        




        