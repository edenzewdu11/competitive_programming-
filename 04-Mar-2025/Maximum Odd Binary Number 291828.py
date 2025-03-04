# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        arr=[0]*len(s)
        arr[-1]=1
        count=0
        for i in s:
            if i=="1":
                count+=1
        for i in range(count-1):
            arr[i]=1
        return "".join(map(str,arr))
       

        