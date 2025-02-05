# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string=""
        for i in range(len(s)):
            string+=str(ord(s[i])-96)
       
        for j in range(k):
            summ=0
            for i in string:
                summ+=int(i)
                string=str(summ)
        return summ

        